#ifndef MBOT_BRIDGE_JSON_HELPERS_H
#define MBOT_BRIDGE_JSON_HELPERS_H

#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <regex>


static inline std::string strip(const std::string& s)
{
    std::string r = s;
    r.erase(std::remove(r.begin(), r.end(), ' '), r.end());
    return r;
}

static inline std::string stripQuotes(const std::string& s)
{
    std::string r = s;
    r.erase(std::remove(r.begin(), r.end(), '\"'), r.end());
    r.erase(std::remove(r.begin(), r.end(), '\''), r.end());
    return r;
}

// split string
static inline std::vector<std::string> split(const std::string &s, char delim) {
    std::stringstream ss(s);
    std::string item;
    std::vector<std::string> tokens;
    while (std::getline(ss, item, delim)) {
        tokens.push_back(item);
    }
    return tokens;
}


static inline std::string fetchVal(const std::string& s, const std::string& keyword) {
    std::string exp_val = "\"" + keyword + "\":\\s*([^,$]+)";  // Looks for raw data.

    std::smatch sm;
    std::regex e_val(exp_val);

    if (std::regex_search(s, sm, e_val))
    {
        auto match = sm[sm.size() - 1];
        return match;
    }

    return "";
}


static inline std::string fetchString(const std::string& s, const std::string& keyword) {
    std::string exp_str = "\"" + keyword + "\":\\s*\"([^\"]+)";  // Looks for string data.

    std::smatch sm;
    std::regex e_str(exp_str);

    if (std::regex_search(s, sm, e_str))
    {
        auto match = sm[sm.size() - 1];
        return match;
    }

    return "";
}

static inline std::string fetchDict(const std::string& s, const std::string& keyword) {
    std::string exp_dict = "\"" + keyword + "\":\\s*\\{([^\\}]+)";  // Looks for dictionary data.

    std::smatch sm;
    std::regex e_dict(exp_dict);

    if (std::regex_search(s, sm, e_dict))
    {
        auto match = sm[sm.size() - 1];
        return match;
    }

    return "";
}


static inline std::string fetchList(const std::string& s, const std::string& keyword) {
    std::string exp_list = "\"" + keyword + "\":\\s*\\[([^\\]]+)";  // Looks for dictionary data.

    std::smatch sm;
    std::regex e_list(exp_list);

    if (std::regex_search(s, sm, e_list))
    {
        auto match = sm[sm.size() - 1];
        return match;
    }

    return "";
}

// fetch any data
static inline std::string fetch(const std::string& s, const std::string& keyword) {
    // Try to find any type of data. This function is not very efficient.
    std::string str = fetchString(s, keyword);
    if (str.size() > 0)
    {
        return str;
    }

    std::string dict = fetchDict(s, keyword);
    if (dict.size() > 0)
    {
        return dict;
    }

    std::string list = fetchList(s, keyword);
    if (list.size() > 0)
    {
        return list;
    }

    std::string val = fetchVal(s, keyword);
    if (val.size() > 0)
    {
        return val;
    }

    // By default, return nothing.
    return "";
}

template <class T>
static inline std::string keyValToJSON(const std::string& key, const T& val)
{
    std::ostringstream oss;
    oss << "\"" << key << "\":" << val;
    return oss.str();
}

static inline std::string keyStringToJSON(const std::string& key, const std::string& val)
{
    std::ostringstream oss;
    oss << "\"" << key << "\":" << val;
    return "\"" + key + "\":\"" + val + "\"";
}

template <class T>
static inline std::string vectorToJSON(const std::vector<T>& vals)
{
    std::ostringstream oss;

    if (vals.size() < 1)
    {
        oss << "[]";
        return oss.str();
    }

    oss << "[";
    for (size_t i = 0; i < vals.size() - 1; ++i)
    {
        oss << std::to_string(vals[i]) << ",";
    }
    oss << std::to_string(vals[vals.size() - 1]) << "]";

    return oss.str();
}

template <class T>
static inline std::string keyValsToJSON(const std::string& key, const std::vector<T>& vals)
{
    std::ostringstream oss;
    oss << "\"" << key << "\": ";
    oss << vectorToJSON(vals);

    return oss.str();
}

static inline std::string keyStringValsToJSON(const std::string& key, const std::vector<std::string>& vals)
{
    std::ostringstream oss;
    oss << "\"" << key << "\": [";
    for (size_t i = 0; i < vals.size() - 1; ++i)
    {
        oss << vals[i] << ",";
    }
    oss << vals[vals.size() - 1] << "]";

    return oss.str();
}

template <class T>
static inline std::string keyMapToJSON(const std::string& key, const std::map<std::string, T>& data)
{
    std::ostringstream oss;
    oss << "\"" << key << "\": {";
    for (auto const& x : data)
    {
        oss << "\"" << x.first << "\":" << x.second << ",";
    }
    // Remove last comma.
    oss.seekp(-1, oss.cur);
    oss << "}";
    return oss.str();
}

static inline std::map<std::string, std::string> jsonToMap(const std::string& in_data)
{
    std::map<std::string, std::string> data;
    // std::string raw = in_data;
    auto vals = split(in_data, ',');
    for (auto& str : vals)
    {
        auto key_val = split(str, ':');
        if (key_val.size() != 2)
        {
            std::cout << "[MBot API] ERROR: Can't parse data: " << str << std::endl;
            continue;
        }

        std::string key = strip(stripQuotes(key_val[0]));
        std::string val = strip(stripQuotes(key_val[1]));

        data.insert({key, val});
    }

    return data;
}

#endif // MBOT_BRIDGE_JSON_HELPERS_H
