#ifndef MBOT_BRIDGE_MBOT_JSON_MSGS_H
#define MBOT_BRIDGE_MBOT_JSON_MSGS_H

#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>

#include "json_utils.h"

namespace mbot_bridge {

enum MBotMessageType
{
    INIT,
    REQUEST,
    PUBLISH,
    RESPONSE,
    ERROR,
    INVALID
};


class MBotJSONMessage
{
public:
    MBotJSONMessage() :
        data_(""),
        channel_(""),
        dtype_(""),
        rtype_(MBotMessageType::INVALID),
        as_bytes_(false)
    {};

    MBotJSONMessage(const std::string& data, const std::string& ch,
                    const std::string& dtype, const MBotMessageType& rtype,
                    const bool as_bytes = false) :
        data_(data),
        channel_(ch),
        dtype_(dtype),
        rtype_(rtype),
        as_bytes_(as_bytes)
    {};

    std::string encode() const
    {
        std::ostringstream oss;
        oss << "{";
        // Type info.
        oss << keyStringToJSON("type", typeToString(rtype_));

        if (channel_.length() > 0)
        {
            oss << "," << keyStringToJSON("channel", channel_);
        }
        if (dtype_.length() > 0)
        {
            oss << "," << keyStringToJSON("dtype", dtype_);
        }
        if (data_.length() > 0)
        {
            oss << "," << "\"data\":{" << data_ << "}";
        }
        if (rtype_ == MBotMessageType::REQUEST)
        {
            // If we are requesting data, include whether or not it should be in byte form.
            oss << "," << keyValToJSON("as_bytes", as_bytes_);
        }
        oss << "}";  // Close msg.

        return oss.str();
    }

    void decode(const std::string& msg)
    {
        std::string raw = msg;

        // Remove first and last brackets.
        raw.erase(0, 1);
        raw.erase(raw.length() - 1, raw.length());

        // Get the type.
        if (raw.find("type") == std::string::npos)
        {
            std::cout << "Error: No type attribute in message: " << msg << std::endl;
            rtype_ = MBotMessageType::INVALID;
            return;
        }
        rtype_ = stringToType(fetchString(raw, "type"));

        data_ = "";
        if (raw.find("data") != std::string::npos)
        {
            data_ = fetch(raw, "data");
        }

        channel_ = "";
        if (raw.find("channel") != std::string::npos)
        {
            channel_ = fetchString(raw, "channel");
        }

        dtype_ = "";
        if (raw.find("dtype") != std::string::npos)
        {
            dtype_ = fetchString(raw, "dtype");
        }
    }

    std::string data() const { return data_; }
    std::string channel() const { return channel_; }
    std::string dtype() const { return dtype_; }
    MBotMessageType type() const { return rtype_; }

private:
    std::string data_;
    std::string channel_;
    std::string dtype_;
    MBotMessageType rtype_;
    bool as_bytes_;

    std::string typeToString(const MBotMessageType& t) const
    {
        switch (t)
        {
            case INIT:
                return "init";
            case REQUEST:
                return "request";
            case PUBLISH:
                return "publish";
            case RESPONSE:
                return "response";
            case INVALID:
                return "invalid";
            case ERROR:
                return "error";
        }
        return "";
    }

    MBotMessageType stringToType(const std::string& s) const
    {
        if (s == "init") return MBotMessageType::INIT;
        else if (s == "request") return MBotMessageType::REQUEST;
        else if (s == "publish") return MBotMessageType::PUBLISH;
        else if (s == "response") return MBotMessageType::RESPONSE;
        else if (s == "error") return MBotMessageType::ERROR;

        // Default case.
        return MBotMessageType::INVALID;
    }
};

}   // namespace mbot_bridge

#endif // MBOT_BRIDGE_MBOT_JSON_MSGS_H
