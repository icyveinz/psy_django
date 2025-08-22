const path = require("path");

// module.exports = {
//     mode: "production",
//     entry: {
//         testing: "./js/testing/testing.js"
//     },
//     output: {
//         filename: '[name]/bundled_[name].js', // <-- this creates subfolder `testing/`
//         path: path.resolve(__dirname, '../static/js'),
//     }
// };

module.exports = {
  mode: 'production', // или 'development', чтобы не было предупреждений
  entry: {},          // пустой объект — нет точек входа
  output: {
    filename: '[name].js',                   // имя файла сборки (не будет создаваться, т.к. entry пустой)
    path: path.resolve(__dirname, '../static/js'), // куда Webpack "собрал бы" файлы
  }
};
