#!/bin/bash
set -e  # Quit on error.

# Install mbot-lcm-spy
echo "Installing mbot-lcm-spy..."
chmod +x mbot_lcm_spy/mbot_lcm_spy.py
sudo cp mbot_lcm_spy/mbot_lcm_spy.py /usr/local/bin/mbot-lcm-spy

# Install system tool mbot-service
echo "Installing mbot-service..."
chmod +x mbot_service/mbot-service.sh
sudo cp mbot_service/mbot-service.sh /usr/local/bin/mbot-service

# Install mbot-lcm-msg
echo "Installing mbot-lcm-msg..."
chmod +x mbot_lcm_msg/mbot_lcm_msg.py
sudo cp mbot_lcm_msg/mbot_lcm_msg.py /usr/local/bin/mbot-lcm-msg

# Install dispatcher script mbot
echo "Installing mbot cli tools..."
chmod +x mbot.sh
sudo cp mbot.sh /usr/local/bin/mbot

# Auto-completion script
cat << 'EOF' | sudo tee /etc/bash_completion.d/mbot > /dev/null
# mbot completion
_mbot()
{
    local cur prev commands servicespy msg
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    commands="service lcm-spy lcm-msg"

    if [[ ${COMP_CWORD} -eq 1 ]] ; then
        COMPREPLY=( $(compgen -W "${commands}" -- ${cur}) )
        return 0
    fi

    case "${prev}" in
        service)
            servicespy="list status log start stop restart enable disable"
            COMPREPLY=( $(compgen -W "${servicespy}" -- ${cur}) )
            return 0
            ;;
        lcm-spy)
            servicespy="--channels --rate --module"
            COMPREPLY=( $(compgen -W "${servicespy}" -- ${cur}) )
            return 0
            ;;
        lcm-msg)
            msg="list show"
            COMPREPLY=( $(compgen -W "${msg}" -- ${cur}) )
            return 0
            ;;
    esac
}

complete -F _mbot mbot
EOF

# Reload bash configuration
source ~/.bashrc

echo "MBot System CLI Installation completed successfully."