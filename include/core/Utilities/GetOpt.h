#pragma once

#include <string>
#include <vector>
#include <unordered_map>

class GetOpt {
    public:
        GetOpt(int argc, char* argv[]);

        bool hasLongOption(const std::string& key) const;
        bool hasShortOption(char opt) const;

        const char* getLongOptionValue(const std::string& key) const;
        const char* getShortOptionValue(char opt) const;

        const std::vector<std::string>& getPositionalArgs() const;

    private:
        std::unordered_map<std::string, std::string> longOptions;
        std::unordered_map<char, std::string> shortOptions;
        std::vector<std::string> positionalArgs;
};
