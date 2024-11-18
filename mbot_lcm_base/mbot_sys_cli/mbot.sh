#!/bin/bash
set -e

# Dispatcher script for mbot commands

# Check if the user provided at least one argument
if [ $# -lt 1 ]; then
    echo "Usage: mbot {service|lcm-spy|lcm-msg} [args]"
    exit 1
fi

# The first argument determines the command
command=$1
shift  # Remove the first argument

case $command in
    service)
        /usr/local/bin/mbot-service "$@"
        ;;
    lcm-spy)
        /usr/local/bin/mbot-lcm-spy "$@"
        ;;
    lcm-msg)
        /usr/local/bin/mbot-lcm-msg "$@"
        ;;
    *)
        echo "Unknown command: $command"
        echo "Usage: mbot {service|lcm-spy|lcm-msg} [args]"
        exit 1
        ;;
esac
