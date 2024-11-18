const path = require('path');

module.exports = {
  entry: './src/robot.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist'),
    library: 'MBotAPI'
  },
};