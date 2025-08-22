const path = require("path");

module.exports = {
    mode: "production",
    entry: {
        testing: "./js/testing/testing.js"
    },
    output: {
        filename: '[name]/bundled_[name].js', // <-- this creates subfolder `testing/`
        path: path.resolve(__dirname, '../static/js'),
    }
};