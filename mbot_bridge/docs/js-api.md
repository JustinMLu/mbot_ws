# MBot Bridge API: Javascript

The Javascript API can be used either with Node.JS or in plain Javascript.

## Installation

### Node.JS (Recommended)

To use the MBot API in a Node project, clone this repo then do:
```bash
cd mbot_bridge/mbot_js
npm install
npm link
```
The command `npm link` makes a symlink of this package available to link in other packages. This is an alternative to registering this package as an official NPM package.

Then, in your own Node project, do:
```bash
cd my_project/
npm link mbot-js-api
```

To create a MBot object in your project, do:
```javascript
import { MBot } from "mbot-js-api";

const mbot = new MBot(mbotIP);
```
where `mbotIP` is the IP address of the mbot.

**Tip:** The IP of the robot is often the one you type into the browser to access the web app hosted on the robot. To get this IP, do:
```javascript
const mbotIP = window.location.host.split(":")[0]  // Grab the IP from which this page was accessed.
```

### Plain Javascript

#### Method 1: Use Latest Release (Recommended)

*TODO:* Add instructions to link to the latest release (when it is released).

#### Method 2: Build from source

Use this method if you are developing or if you need the latest (unreleased) version.

First, clone this repo, then do:
```bash
cd mbot_bridge/mbot_js
npm install
npm run build
```
Then include the bundled script `mbot_js/dist/main.js` in your HTML.

To create a MBot object, do:
```javascript
const mbot = new MBotAPI.MBot(mbotIP);
```
where `mbotIP` is the IP address of the mbot.

## Usage

For the full list of available functions, see [robot.js](../mbot_js/src/robot.js). For example usage, see [main.js](../test/main.js).

The Javascript API is based off of [*promises*](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), which are objects built for handling asynchronous tasks. Except for publishing, all the functions in the `MBot` class use promises. There are two ways to use this:

### Using Promises

You can use the `.then()` and `.catch()` promise attributes. When the promise returns (e.g. when the MBot Bridge server returns the requested data), the function passed to `.then()` will be called with the returned data as the argument. If an error is raised and the promise rejects, the function passed to `.catch()` will be called with the error message. For example, to read the hostname:
```javascript
mbot.readHostname().then((hostname) => { console.log("hostname:", hostname); });
```
The hostname will be printed once the data is received, which resolves the promise. This does not block the code execution. In this example, we are not catching errors.

### Using `async` / `await`
You can also use the `async` / `await` syntax, which is essentially a wrapper for promises. For this, you need to be in an `async` function. To read the hostname this way:
```javascript
async function readHostname(mbot) {
    const host = await mbot.readHostname();
    console.log("Async hostname:", host);
}
```

These do the same thing. In general, unless you are already using `async` / `await` in your code, use the promise syntax.
