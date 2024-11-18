#!/bin/bash

# Function to print usage instructions and exit
usage() {
    echo "Usage: mbot service {list|status|log|start|stop|restart|enable|disable} [service_name]"
    echo "Actions:"
    echo "  list       List all mbot- services"
    echo "  status     Status of all mbot- services or a specific service"
    echo "  log        Show log for the service"
    echo "  start      Start the service"
    echo "  stop       Stop the service"
    echo "  restart    Restart the service"
    echo "  enable     Enable the service (not immediate start)"
    echo "  disable    Disable the service (not immediate stop)"
    echo ""
    echo "Examples:"
    echo "  mbot service list"              
    echo "  mbot service status"
    echo "  mbot service status mbot-xxx.service"  
    echo "  mbot service log mbot-xxx.service" 
    echo "  mbot service start mbot-xxx.service"  
    echo "  mbot service stop mbot-xxx.service"   
    echo "  mbot service restart mbot-xxx.service" 
    echo "  mbot service enable mbot-xxx.service"  
    echo "  mbot service disable mbot-xxx.service" 
    exit 1
}

# Check if the user provided at least one arguments
if [ $# -lt 1 ]; then
    usage
fi

action=$1
service_name=$2

# Validate the action
case $action in
    list|status|log|start|stop|restart|enable|disable)

        ;;
    *)
        usage
        ;;
esac

# Special handling for actions that require a service name
if [[ "$action" == "log" || "$action" == "start" || "$action" == "stop" || "$action" == "restart" 
                        || "$action" == "enable" || "$action" == "disable" ]]; then
    if [ -z "$service_name" ]; then
        echo "Error: Please specify a service name for the $action action."
        echo "Usage: mbot service $action service_name"
        exit 1
    else
        echo "$service_name $action"
        if [ "$action" == "log" ]; then
            journalctl -u $service_name --no-pager -n 20
        else
            systemctl $action $service_name
            if [ $? -eq 0 ]; then
                echo "$service_name $action succeeded"
            else
                echo "$service_name $action failed"
            fi
        fi
        exit 0
    fi
fi

# Handle the 'status' action
if [ "$action" == "status" ]; then
    if [ -n "$service_name" ]; then
        # Specific service status
        systemctl status $service_name --no-pager
    else
        # Find all services with mbot- prefix
        services=$(systemctl list-unit-files --type=service --no-pager --no-legend | grep "mbot-" | awk '{print $1}')
        
        # Loop through each service and print the status
        for service in $services; do
            echo "$service"
            systemctl status $service | grep -m 1 "Active:"
            echo ""
        done
    fi
    exit 0
fi

# Handle the 'list' action
if [ "$action" == "list" ]; then
    # Find all services with mbot- prefix
    services=$(systemctl list-unit-files --type=service --no-pager --no-legend | grep "mbot-" | awk '{print $1}')
    
    # Loop through each service and print its name
    for service in $services; do
        echo "$service"
    done
    exit 0
fi

# If no valid action was found, show usage
usage