# MBot Bridge

Server and API to bridge MBot functionality with student code.

Dependencies:
* Python 3 (tested on 3.10)
* LCM 1.4+ (tested on 1.5)
* [MBot messages](https://github.com/mbot-project/mbot_lcm_base) for Python and C++

See the [Documentation](docs/index.md) for more details.

## Install Instructions

To install the MBot Bridge, the API, and all the related services, do:
```bash
./scripts/install.sh
```

**Warning:** This globally installs the MBot Bridge API and its Python and C++ dependencies. Only do this on an MBot. In general, it's recommended to install Python packages in virtual environments instead.

## Usage

For development, it is best to use a virtual environment. From your virtual environment, do:
```bash
python -m pip install -e .
```

To run the server, do:
```bash
python -m mbot_bridge.server [--config [PATH/TO/CONFIG]]
```
The `--config` argument is optional and will default to `src/mbot_bridge/config/default.yml`.

**Import errors in your virtual environment?** If you get import errors (e.g. for NumPy and LCM) you need to share the system packages with the virtual environment. If you are using `venv`, you can do this with:
```bash
python3 -m venv --system-site-packages ~/.envs/my-mbot-env
```
Alternatively, set your `PYTHONPATH` variable to tell your Python interpreter to check the global path for libraries:
```bash
export PYTHONPATH=$PYTHONPATH:/usr/lib/python3/dist-packages/:/usr/local/lib/python3.X/dist-packages/
```
Make sure you replace `python3.X` with your installed Python version.

## C++ API

To use the C++ API, first install the websocket library at the latest release version:
```bash
wget https://github.com/zaphoyd/websocketpp/archive/refs/tags/0.8.2.tar.gz
tar -xzf 0.8.2.tar.gz
cd websocketpp-0.8.2/
mkdir build && cd build
cmake ..
make
sudo make install
```
Then, compile the C++ API:
```bash
cd mbot_bridge
mkdir build
cd build
cmake ../mbot_cpp/
make
```
To install the C++ API globally, do:
```bash
sudo make install
```
A test script is available at:
```bash
./build/mbot_cpp_test
```

## JavaScript API

The JavaScript API can be installed using NPM as follows:
```bash
cd mbot_js
npm install
npm run build
```
Then include the bundled script `mbot_js/dist/main.js` where you want to use the API. To create a MBot object, do:
```javascript
const mbot = new MBotAPI.MBot(mbotIP);
```
where `mbotIP` is the IP address of the mbot.

### Usage

To test the JS API, a test script is available in the `test` directory. To use it, start an HTTP server in the root of this repo:
```bash
python -m http.server
```
Then navigate to `http://[HOST_IP]:8000/test` in a browser. If running locally, use the IP `localhost`.
