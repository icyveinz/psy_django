import {move_from_the_top} from "./gsap/landing_animation_template";

document.addEventListener("DOMContentLoaded", function() {
    const containers = document.querySelectorAll(".courses-container");
    let courses = [];
    const indices = new Map();

    fetch('/wagtail_landing/api/study-results/')
        .then(response => response.json())
        .then(data => {
            courses = data;

            containers.forEach(container => {
                indices.set(container, 0);
                showCourse(container, 0); // первый курс без анимации
            });
        });

    // Функция отображения курса с анимацией
    function showCourse(container, index) {
        if (!courses.length) return;
        const course = courses[index];

        const htmlContent = `
            <h2 class="xp-docs-single-div__p">Курс: ${course.course_title}</h2>
            <p class="xp-docs-single-div__p">Платформа: ${course.course_platform}</p>
            <p class="xp-docs-single-div__p">Дата окончания: ${course.year_ended}</p>
            <p class="xp-docs-single-div__p">Полученные навыки:</p>
            <ul>
                ${course.study_results_li.map(item => `<li class="xp-docs-single-div__p">${item.skills_achieved}</li>`).join('')}
            </ul>
        `;

        // Очищаем контейнер и вставляем новый контент сразу
        container.innerHTML = htmlContent;

        // Все элементы с классом для анимации
        const items = container.querySelectorAll('.xp-docs-single-div__p');

        // Сразу делаем начальное состояние
        gsap.set(items, { opacity: 0, y: -20 });

        // Timeline для последовательного появления
        gsap.to(items, {
            duration: 0.5,
            opacity: 1,
            y: 0,
            ease: "power2.out",
            stagger: 0.1
        });
    }


    // Кнопки переключения
    document.querySelectorAll(".prev-course, .next-course").forEach(button => {
        button.addEventListener("click", function() {
            const section = button.closest(".xp-docs-single-div");
            if (!section) return;

            const container = section.querySelector(".courses-container");
            if (!container) return;

            let currentIndex = indices.get(container) || 0;

            if (button.classList.contains("prev-course")) {
                currentIndex = (currentIndex - 1 + courses.length) % courses.length;
            } else {
                currentIndex = (currentIndex + 1) % courses.length;
            }

            indices.set(container, currentIndex);
            showCourse(container, currentIndex);
        });
    });
});
