# MBot System CLI

## Description
This folder contains command line tools for the MBot system:

- mbot-lcm-spy: A command line tool similar to lcm-spy, akin to `ros topic`.
- mbot-service: Similar to `ros node`, it uses systemctl and journalctl to manage and monitor MBot system services.
- mbot-lcm-msg: Functions like `ros msg`, used to inspect the data structure of MBot LCM messages.

## Installation
> If you have run the install.sh under the mbot_lcm_base folder, then you don't need to run this.
```bash
chmod +x install.sh
./install.sh
```

## Usage and Features
Usage instructions can be found in the README.md file within each tool's folder.

## Authors and maintainers
The current maintainer of this project is Shaw Sun. Please direct all questions regarding support, contributions, and issues to the maintainer. 