const path = require("path");
const TerserPlugin = require('terser-webpack-plugin'); // For minifying and removing comments

module.exports = {
    mode: "production",
    optimization: {
        minimize: true,
        minimizer: [
            new TerserPlugin({
                terserOptions: {
                    format: {
                        comments: false
                    }
                }
            })
        ]
    },
    entry: {
        libraries : [
            "./js/libraries/gsap.min.js",
            "./js/libraries/ScrollTrigger.min.js",
        ],
        main_landing: [
            "./js/main_landing/loader.js",
            "./js/blog/blog_animation_landing.js",
            "./js/main_landing/burger_menu.js",
            "./js/main_landing/gsap/certificates_animation_both.js",
            "./js/main_landing/course_fetcher.js",
            "./js/main_landing/gsap/landing_animation_media.js",
            "./js/main_landing/gsap/landing_animation_template.js",
            "./js/main_landing/gsap/services_animation_both.js",
            "./js/main_landing/gsap/xp_animation_desktop.js",
            "./js/main_landing/gsap/xp_animation_mobile.js",
        ],
        blog: [
            "./js/main_landing/loader.js",
            "./js/main_landing/burger_menu.js",
            "./js/blog/blog_animation_landing.js",
            "./js/blog/blog_animation_media.js",
            "./js/blog/blog_animation_static.js"
        ],
        docs: [
            "./js/main_landing/loader.js",
            "./js/main_landing/burger_menu.js"
        ],
    },
    output: {
        filename: '[name]/bundled_[name].js', // <-- this creates subfolder `testing/`
        path: path.resolve(__dirname, '../static/js'),
    }
};

// module.exports = {
//   mode: 'production', // или 'development', чтобы не было предупреждений
//   entry: {},          // пустой объект — нет точек входа
//   output: {
//     filename: '[name].js',                   // имя файла сборки (не будет создаваться, т.к. entry пустой)
//     path: path.resolve(__dirname, '../static/js'), // куда Webpack "собрал бы" файлы
//   }
// };
