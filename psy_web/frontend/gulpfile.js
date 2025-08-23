const path = require('path');
const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const concat = require('gulp-concat');
const cleanCSS = require('gulp-clean-css');
const rename = require('gulp-rename');
const imagemin = require('gulp-imagemin');

gulp.task('styles', function () {
    return gulp.src('sass/**/*.sass') // or 'sass/**/*.scss' if you're using SCSS
        .pipe(sass().on('error', sass.logError))
        .pipe(concat('main.css')) // combine all into one file
        .pipe(cleanCSS()) // minify the CSS
        .pipe(rename({ suffix: '.min' })) // add .min suffix: main.min.css
        .pipe(gulp.dest(path.resolve(__dirname, './static/css'))); // output to static folder
});


gulp.task('default', gulp.parallel('styles'));