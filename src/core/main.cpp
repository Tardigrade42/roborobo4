/*
 *  main.cpp
 *  roborobo
 *
 *  Created by Nicolas on 16/01/09.
 *  See roborbo.cpp for description
 */

#include "RoboroboMain/main.h"
#include <cstdlib>
#include "Utilities/GetOpt.h"
#include <csignal>

// For getopt
extern char *optarg;
extern int  optind, opterr;

void displayGeneralInformation()
{
	std::cout << std::endl;
	std::cout << " =-= Roborobo! " << std::endl;
	std::cout << " =-= nicolas.bredeche(at)upmc.fr" << std::endl;
	std::cout << " =-= Current build name      : " << gCurrentBuildInfo << std::endl;
	std::cout << " =-= Official version tag    : " << gVersion << std::endl;
	std::cout << " =-= Compilation version tag : " << gCompileDate << " - " << gCompileTime << std::endl;
    
	std::cout << std::endl;
}


// Called when roborobo must quit
void quit(int signal)
{
	closeRoborobo();
	exit(0);
}

/** Print usage (e.g. when user enters bad command line options, or '-h' parameter) */
static void usage(char* argv0)
{
	std::cout << std::endl << "Roborobo! Command line help:" << std::endl << std::endl;
	std::cout << "  usage  : " << argv0 << " [-h] [-v] [-l <propertiesfilename>] [-o <path_to_log_files>] [-s] [-b]" << std::endl << std::endl;
	std::cout << "  options:" << std::endl;
	std::cout << "    h: print this help message." << std::endl;
	std::cout << "    v: print current version number." << std::endl;
	std::cout << "    l: specify location and name of the properties file." << std::endl;
	std::cout << "         next parameter should be the filename (e.g. ./roborobo -l config/MyConfigFile.properties\")" << std::endl;
	std::cout << "         default properties file is \"" << gPropertiesFilename << "\"" << std::endl;
	std::cout << "    o: specify path where log files will be written." << std::endl;
	std::cout << "         next parameter should be the (relative) path (e.g. ./roborobo (...) -o logs/myexperiment)" << std::endl;
	std::cout << "         roborobo will exit if the target directory does not exist." << std::endl;
	std::cout << "         default properties file is \"" << gPropertiesFilename << "\"" << std::endl;
	std::cout << "    s: do not verbose messages in console." << std::endl;
    std::cout << "    b: batch mode (no display, fastest mode)." << std::endl;

	std::cout << std::endl;
}

/** Print infos about this version of Roborobo */
static void versionInfos()
{
	std::cout << std::endl;
	std::cout << " =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" << std::endl;
	std::cout << " =-=-=-=-=-=-= Roborobo! =-= ver.3 =-=" << std::endl;
	std::cout << " =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" << std::endl;
	std::cout << std::endl;
	std::cout << "  description     : A lightweight collective robots/agents simulator written in C++/SDL2." << std::endl;
	std::cout << "  author          : nicolas.bredeche(at)upmc.fr" << std::endl;
	std::cout << "  started         : [Ver.1: 12/2008] [Ver.2: 09/2013] [Ver.3: 10/2015]" << std::endl << std::endl;
	std::cout << "  current build   : " << gCurrentBuildInfo << std::endl;
	std::cout << "  version tag     : " << gVersion << std::endl;
	std::cout << "  compilation tag : " << gCompileDate << " - " << gCompileTime << std::endl << std::endl;
}

// A helper function to simplify the main part.
template<class T>
std::ostream& operator<<(std::ostream& os, const std::vector<T>& v)
{
    copy(v.begin(), v.end(), std::ostream_iterator<T>(std::cout, " "));
    return os;
}

/** default demo mode with visualization. If at least one argument, launch demo in batch mode (ie. no display, fast pace). */
int main(int argc, char* argv[])
{
    // Parse Command line parameters (in argv), using self-implemented GetOpt
    GetOpt opt(argc, argv);
    bool commandline_propertiesfilename = false;
    
	// Install signal handler, to handle Ctrl-C and 'kill' signals
	signal(SIGINT, quit);
	signal(SIGTERM, quit);
    
    displayGeneralInformation();

    // no arguments? display usage.
    if (argc == 1)
    {
        std::cout << "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" << std::endl;
        std::cout << "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" << std::endl;
        std::cout << "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" << std::endl;
        std::cout << "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" << std::endl;
        std::cout << std::endl;
        std::cout << "IMPORTANT REMARK: " << std::endl;
        std::cout << std::endl;
        std::cout << "\tRoborobo has been launched without any parameters." << std::endl;
        std::cout << "\tRoborobo assumes that \"DEMO\" mode is requested."<< std::endl;
        std::cout << std::endl;
        std::cout << "\tRoborobo will behave as if the following command was entered:"<< std::endl;
        std::cout << "\t\t./roborobo -l " << gPropertiesFilename << " -o " <<  gLogDirectoryname << " -s" << std::endl;
        std::cout << std::endl;
        std::cout << "\tEnter ./roborobo -h for details on command line parameters."<< std::endl;
        std::cout << std::endl;
        std::cout << "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" << std::endl;
        std::cout << "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" << std::endl;
        std::cout << "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" << std::endl;
        std::cout << "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" << std::endl;
        std::cout << std::endl;
        
        // roborobo -s (...)
        gVerbose = false;
        gVerbose_commandlineargument = true;
        
        //return -1;
    }

    if (opt.hasShortOption('v') || opt.hasLongOption("version")) {
        versionInfos();
        return -1;
    }

    if (opt.hasShortOption('h') || opt.hasLongOption("help")) {
        usage(argv[0]);
        return -1;
    }

    if (opt.hasShortOption('s')) {
        gVerbose = false;
        gVerbose_commandlineargument = true;
    }

    if (opt.hasShortOption('b')) {
        gBatchMode = true;
        gDisplayMode = 2;
        gBatchMode_commandlineargument = true;
    }

    if (auto lval = opt.getShortOptionValue('l')) {
        if (!commandline_propertiesfilename) {
            gPropertiesFilename = *lval;
            std::cout << "[INFO] Command-line parameter: properties will be loaded from file \"" << gPropertiesFilename << "\"." << std::endl;
            commandline_propertiesfilename = true;
        } else {
            std::cout << "[INFO] Command-line parameter: properties file already set (\"" <<  gPropertiesFilename << "\"). Ignored." << std::endl;
        }
    }

    if (auto oval = opt.getShortOptionValue('o')) {
        // take only the first into account
        if (gLogDirectoryname_commandlineargument == false ) {
            gLogDirectoryname = *oval;
            std::cout << "[INFO] Command-line parameter: logs will be written in directory \"" <<  gLogDirectoryname << "\" (assume: directory exists)." << std::endl;
            gLogDirectoryname_commandlineargument = true;
        } else {
            std::cout << "[INFO] Command-line parameter: logs directory already set (\"" <<  gLogDirectoryname << "\"). Ignored." << std::endl;
        }
    }
    
    /**/
    char *path = nullptr;
    size_t size = 0;
    path = getcwd(path,size);
    std::cout << "[INFO] Current location : " << path << std::endl;
    //delete path;
    /**/
    
	std::cout << std::endl << std::endl;
    
	int returnValue = 0;
	returnValue = launchRoborobo();
    
	return returnValue;
}

