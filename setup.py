import os
from os.path import dirname
import platform
import re
import subprocess
import sys
from packaging.version import Version
import pybind11

# Find current python version for API compilation target
python_exe = sys.executable
python_root = dirname(dirname(python_exe))

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)

class CMakeBuild(build_ext):
    def run(self):
        try:
            out = subprocess.check_output(['cmake', '--version'])
        except OSError:
            raise RuntimeError("CMake must be installed to build the following extensions: " +
                               ", ".join(e.name for e in self.extensions))

        if platform.system() == "Windows":
            cmake_version_r_match = re.search(r'version\s*([\d.]+)', out.decode())

            if cmake_version_r_match is None:
                raise RuntimeError("No CMake version found")
            
            cmake_version = Version(cmake_version_r_match.group(1))
            if cmake_version < Version('3.1.0'):
                raise RuntimeError("CMake >= 3.1.0 is required on Windows")

        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        # required for auto-detection of auxiliary "native" libs
        if not extdir.endswith(os.path.sep):
            extdir += os.path.sep

        print(extdir)
        cmake_args = [
            f'-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}',
            f'-DPython_EXECUTABLE={python_exe}',
            f'-DPYTHON_EXECUTABLE={python_exe}',      # Legacy fallback
            f'-DPython_ROOT_DIR={python_root}',
            f'-DPython_FIND_STRATEGY=LOCATION',       # force exact match
            f'-DPython_FIND_IMPLEMENTATIONS=CPython', # avoid python brought by vcpkg
        ]

        # Checks if the current python installation is debug capable
        is_debug_python = hasattr(sys, "gettotalrefcount")
        cfg = 'Debug' if is_debug_python else 'Release'
        build_args = ['--config', cfg]

        if platform.system() == "Windows":
            cmake_args += ['-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{}={}'.format(cfg.upper(), extdir)]
            if sys.maxsize > 2**32:
                cmake_args += ['-A', 'x64']
                # For some reason Windows is always defaulting to build the
                # project with Ninja. This however does not support x64
                # architectures. Therefore this code will crash without
                # defining the correct building tool.
                cmake_args += ['-G', 'Visual Studio 17 2022']
            # Since `pip install pybind11` only imports the header file
            # and the program needs the cmake file, you need to give the
            # installer the concrete location:
            cmake_args += [f'-Dpybind11_DIR={pybind11.get_cmake_dir()}']
            build_args += ['--', '/m']
        else:
            cmake_args += ['-DCMAKE_BUILD_TYPE=' + cfg]
            build_args += ['--', '-j4']
        env = os.environ.copy()
        env['CXXFLAGS'] = '{} -DVERSION_INFO=\\"{}\\"'.format(env.get('CXXFLAGS', ''),
                                                              self.distribution.get_version())
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        subprocess.check_call(['cmake', ext.sourcedir] + cmake_args, cwd=self.build_temp, env=env)
        subprocess.check_call(['cmake', '--build', '.'] + build_args, cwd=self.build_temp)

setup(
    ext_modules=[CMakeExtension('roborobo')],
    zip_safe=False,
    cmdclass={"build_ext": CMakeBuild},
)
