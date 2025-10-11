const gulp = require('gulp')
const sass = require('gulp-sass')(require('sass'))
const concat = require('gulp-concat')
const cleanCSS = require('gulp-clean-css')
const rename = require('gulp-rename')

function styles() {
  return gulp.src('sass/**/*.sass')
    .pipe(sass().on('error', sass.logError))
    .pipe(concat('main.css'))
    .pipe(cleanCSS())
    .pipe(rename({ suffix: '.min' }))
    .pipe(gulp.dest('../static/css'))
}

function watchStyles() {
  return gulp.watch('sass/**/*.sass', styles)
}

// Export tasks
exports.styles = styles
exports.watch = watchStyles
exports.default = styles
