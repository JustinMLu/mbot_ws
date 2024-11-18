# MBot Autonomy
## Description
This repo contains the SLAM and motion controller solution code.

## Installation

To install, we need to build and install binaries, then install the SLAM and motion controller services. You can use the install script, from the root of this repo:
```bash
./scripts/install.sh -t <TYPE> [--no-enable]
```
where `<TYPE>` is either `DIFF` for the classic (differential drive) MBot, or `OMNI` for the MBot Omni. If you don't want the services to be enabled on startup, use the `--no-enable` flag.

## Local Usage

To use MBot Autonomy locally (e.g. for development), do:
```bash
mkdir build
cd build
cmake -DMBOT_TYPE=<TYPE> ..  # Replace <TYPE> with OMNI or DIFF
make
```
where `<TYPE>` is either `OMNI` or `DIFF`. To install the binaries, do:
```bash
sudo make install
```

*TODO: Add documentation for how to run each binary.*

## Usage and Features

### Services

**Checking Service Status**:
```bash
sudo systemctl status <service-name>.service
```

**Enabling Services**:

After installing the MBot Autonomy code, if you used the `--no-enable` flag to skip enabling the services, you can enable the `mbot-motion-controller` service and `mbot-slam` service **manually** by running the following commands:
```bash
sudo systemctl enable mbot-motion-controller.service
sudo systemctl start mbot-motion-controller.service

sudo systemctl enable mbot-slam.service
sudo systemctl start mbot-slam.service
```

### template_generate.py

This file is used to generate `mbot_autonomy_template` repository with solutions subtracted.
By running `python3 template_generate.py`, a template codebase for student use will be generated.

To use it, firstly created a new branch `feature/template` from the `main` branch, then run the `template_generate.py` file.

```
// BEGIN task1
void myFunction1() {
    // Some code here...
}
// END task1
```
- Tag the relavent content like this

**Every time the the `main` branch get updated, the `mbot_autonomy_template` repository should be updated as well from the `feature/template` branch.**

## Authors and maintainers
The current maintainer of this project is ________. Please direct all questions regarding support, contributions, and issues to the maintainer.
