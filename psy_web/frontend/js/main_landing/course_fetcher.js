document.addEventListener("DOMContentLoaded", function() {
    // Получаем все контейнеры
    const containers = document.querySelectorAll(".courses-container");
    let courses = [];
    const indices = new Map(); // будем хранить текущий индекс для каждого контейнера

    // Загружаем данные один раз
    fetch('/wagtail_landing/api/study-results/')
        .then(response => response.json())
        .then(data => {
            courses = data;

            // Заполняем все контейнеры данными
            containers.forEach(container => {
                indices.set(container, 0); // индекс 0 для каждого контейнера
                showCourse(container, 0);
            });
        });

    // Функция для отображения курса в конкретном контейнере
    function showCourse(container, index) {
        if (!courses.length) return;
        const course = courses[index];
        container.innerHTML = `
            <h2 class="xp-docs-single-div__p">Курс: ${course.course_title}</h2>
            <p class="xp-docs-single-div__p">Платформа: ${course.course_platform}</p>
            <p class="xp-docs-single-div__p">Дата окончания: ${course.year_ended}</p>
            <p class="xp-docs-single-div__p">Полученные навыки:</p>
            <ul>
                ${course.study_results_li.map(item => `<li class="xp-docs-single-div__p">${item.skills_achieved}</li>`).join('')}
            </ul>
        `;
    }

    // Обработчик кликов на кнопки
    document.querySelectorAll(".prev-course, .next-course").forEach(button => {
        button.addEventListener("click", function() {
            // Идём вверх по DOM до родительской секции
            const section = button.closest(".xp-docs-single-div");
            if (!section) return;

            // Ищем контейнер внутри секции
            const container = section.querySelector(".courses-container");
            if (!container) return;

            // Получаем текущий индекс
            let currentIndex = indices.get(container) || 0;

            // Определяем направление
            if (button.classList.contains("prev-course")) {
                currentIndex = (currentIndex - 1 + courses.length) % courses.length;
            } else {
                currentIndex = (currentIndex + 1) % courses.length;
            }

            // Сохраняем индекс и обновляем контейнер
            indices.set(container, currentIndex);
            showCourse(container, currentIndex);
        });
    });
});
