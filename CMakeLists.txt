cmake_minimum_required(VERSION 3.5)
project(Roborobo.4)

if (MSVC)
    add_compile_options(
        /EHsc # enable exceptions
        /wd4820 # disable padding warning
        /wd4365 # disable signed/unsigned warning
        /wd4244 # disable narrowing warning
        /wd4100 # disable unreferenced variable warning
        /wd5045 # disable strange python warning
        /wd4242 # disable type conversion warning
        /wd4623 # disable constructor implicit deleted warning
        /wd4626 # disable operator implicit deleted warning
        /wd4245 # disable return type conversion warning
        /wd4458 # disable hiding class member warning
        /wd4266 # disable no override available warning
        /wd4068 # disable unknown pragma warning
        /wd4456 # disable declaration hides previous local declaration warning
        /wd4868 # disable compiler may not enforce left-to-right evaluation warning
        /wd4866 # disable compiler may not enforce left-to-right evaluation warning
        /wd4189 # disable local variable is initialized but not referenced warning
        /wd4514 # disable unreferenced inline function has been removed warning
        /wd4101 # disable unreferenced local variable warning
        /wd4800 # disable implicit conversion warning
        /wd5039 # disable pointer or reference warning
        /wd4267 # disable conversion warning
        /wd4996 # disable unsafe function or variable warning
        /wd4459 # disable hides global declaration warning
        /wd4702 # disable unreachable code warning
        /wd5219 # disable implicit conversion warning
        /wd4996 # disable deprecation warning
        /WX- # disable "warning treaded as error"
        )
endif ()

set(CMAKE_CXX_STANDARD 17)

if (MSVC)
    add_compile_options(/O2)
else()
    add_compile_options(-O3 -Wall)
endif()

set(PYBIND11_FINDPYTHON ON)
find_package(Python COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 REQUIRED)

get_cmake_property(_variableNames VARIABLES)
list(SORT _variableNames)

message("Installing for ${PYTHON_EXECUTABLE}")

file(
        GLOB_RECURSE
        SOURCE_FILES
        src/*
        prj/*
)
SET(LIB_SOURCE_FILES ${SOURCE_FILES})
list(FILTER SOURCE_FILES EXCLUDE REGEX ".*pyroborobo/.*")

include_directories(include)
include_directories(include/contrib)
include_directories(include/core)
include_directories(include/ext)
include_directories(prj)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/build/")
if (NOT DEFINED CMAKE_LIBRARY_OUTPUT_DIRECTORY)
    set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/lib/")
endif()

# FindSDL2.cmake IMPORT
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake/")

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake/")

#find_package(SDL2 COMPONENTS main image REQUIRED)
find_package(SDL2 CONFIG REQUIRED)
find_package(SDL2_image CONFIG REQUIRED)
find_package(Boost REQUIRED COMPONENTS filesystem system)

find_package(Eigen3 REQUIRED NO_MODULE)

add_executable(roborobo ${SOURCE_FILES})
target_link_libraries(roborobo PRIVATE
                      SDL2::SDL2
                      SDL2::SDL2main
                      SDL2_image::SDL2_image
                      Boost::filesystem
                      Boost::system
                      Eigen3::Eigen
)

pybind11_add_module(pyroborobo ${LIB_SOURCE_FILES})
target_compile_definitions(pyroborobo PUBLIC PYROBOROBO=1)
target_link_libraries(pyroborobo PRIVATE
                      SDL2::SDL2
                      SDL2::SDL2main
                      SDL2_image::SDL2_image
                      Boost::filesystem
                      Boost::system
                      Eigen3::Eigen
)
