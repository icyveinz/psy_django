document.addEventListener("DOMContentLoaded", function () {
    const hamb = document.querySelector("#hamb");
    const popup = document.querySelector("#popup");
    const body = document.body;

    // Клонируем меню для мобильной версии
    const menu = document.querySelector("#menu").cloneNode(true);

    // Обработчик на кнопку гамбургера
    hamb.addEventListener("click", hambHandler);

    function hambHandler(e) {
        e.preventDefault();
        popup.classList.toggle("open");
        hamb.classList.toggle("active");
        body.classList.toggle("noscroll");
        renderPopup();
    }

    function renderPopup() {
        if (!popup.contains(menu)) {
            popup.appendChild(menu);
        }
    }

    // Закрытие меню при клике на пункт
    const links = Array.from(menu.children);
    links.forEach((link) => {
        link.addEventListener("click", closeOnClick);
    });

    function closeOnClick() {
        popup.classList.remove("open");
        hamb.classList.remove("active");
        body.classList.remove("noscroll");
    }

    // Клик по контейнеру с логотипом → переход в Telegram
    const logoLink = document.querySelector(".logo-link-holder-flex");
    if (logoLink) {
        logoLink.addEventListener("click", function () {
            window.location.href = "https://t.me/ugo_bar";
        });
    }
});