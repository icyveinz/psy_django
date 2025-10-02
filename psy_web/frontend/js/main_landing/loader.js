document.addEventListener('DOMContentLoaded', () => {
  const loaderContainer = document.querySelector('.loader-container')
  const loader = document.getElementById('lottie-loader')

  const animation = lottie.loadAnimation({
    container: loader,
    renderer: 'svg',
    loop: true,
    autoplay: true,
    path: loader.dataset.lottie
  })

  // Функция скрытия лоадера
  const hideLoader = () => {
    loaderContainer.style.transition = 'opacity 0.7s ease'
    loaderContainer.style.opacity = '0'
    setTimeout(() => loaderContainer.remove(), 700) // время совпадает с transition
  }

  // После загрузки анимации и страницы скрываем лоадер
  animation.addEventListener('DOMLoaded', hideLoader)
})
