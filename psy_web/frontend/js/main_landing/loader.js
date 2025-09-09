document.addEventListener("DOMContentLoaded", function () {
    const loaderContainer = document.querySelector('.loader-container');
    const loader = document.getElementById('lottie-loader');

    document.body.style.overflowY = "hidden";

    const animation = lottie.loadAnimation({
        container: loader,
        renderer: 'svg',
        loop: true,
        autoplay: true,
        path: loader.dataset.lottie
    });

    const hideLoader = () => {
        loaderContainer.style.transition = "opacity 0.7s ease";
        loaderContainer.style.opacity = "0";
        setTimeout(() => {
            loaderContainer.remove();
            document.body.style.overflowY = "";
        }, 500);
    };

    animation.addEventListener('DOMLoaded', () => {
        if (document.readyState === "complete") {
            hideLoader();
        } else {
            window.addEventListener("load", hideLoader);
        }
    });
});