/* This class shall be used to get
 * options from an cli call. This
 * variant shall serve as a light
 * weight option which does not
 * require external libraries and
 * is cross platform capable.
 */

#include "Utilities/GetOpt.h"
#include <string>
#include <vector>
#include <optional>
#include <unordered_map>
#include <iostream>

GetOpt::GetOpt(int argc, char* argv[]) {
    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        
        // Parse long options
        if (arg.rfind("--", 0) == 0) {
            std::string key = arg.substr(2);
            std::string value;

            if (i + 1 < argc && argv[i+1][0] != '-') {
                value = argv[i+1];
                ++i;
            }

            longOptions[key] = value;
        // Parse short options
        } else if (arg[0] == '-') {
            for (size_t j = 1; j < arg.size(); ++j) {
                shortOptions[arg[j]] = "";
            }
        // Parse positional argument
        } else {
            positionalArgs.push_back(arg);
        }
    }
}

bool GetOpt::hasLongOption(const std::string& key) const {
    return longOptions.find(key) != longOptions.end();
}

bool GetOpt::hasShortOption(char opt) const {
    return shortOptions.find(opt) != shortOptions.end();
}

const char* GetOpt::getLongOptionValue(const std::string& key) const {
    auto it = longOptions.find(key);
    if (it == longOptions.end())
        return nullptr;
    return it->second.c_str();
}

const char* GetOpt::getShortOptionValue(char opt) const {
    auto it = shortOptions.find(opt);

    if (it == shortOptions.end()) {
        return nullptr;
    }

    return it->second.c_str();
}

const std::vector<std::string>& GetOpt::getPositionalArgs() const {
    return positionalArgs;
}
