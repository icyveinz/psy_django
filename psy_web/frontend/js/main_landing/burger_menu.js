document.addEventListener('DOMContentLoaded', function () {
  const hamb = document.querySelector('#hamb')
  const popup = document.querySelector('#popup')
  const body = document.body

  hamb.addEventListener('click', function (e) {
    e.preventDefault()
    popup.classList.toggle('open')
    hamb.classList.toggle('active')
    body.classList.toggle('noscroll')

    // Проверяем, есть ли меню в popup
    let menuClone = popup.querySelector('#menu-clone')
    if (!menuClone) {
      menuClone = document.querySelector('#menu').cloneNode(true)
      menuClone.id = 'menu-clone'
      popup.appendChild(menuClone)

      // Навешиваем закрытие при клике на пункт
      Array.from(menuClone.children).forEach(link => {
        link.addEventListener('click', () => {
          popup.classList.remove('open')
          hamb.classList.remove('active')
          body.classList.remove('noscroll')
        })
      })
    }
  })
})
