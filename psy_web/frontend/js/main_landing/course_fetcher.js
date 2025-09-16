document.addEventListener("DOMContentLoaded", function() {
    const containers = document.querySelectorAll(".courses-container");
    let courses = [];
    const indices = new Map();
    const intervals = new Map(); // для хранения интервалов по контейнерам

    fetch('/wagtail_landing/api/study-results/')
        .then(response => response.json())
        .then(data => {
            courses = data;

            containers.forEach(container => {
                indices.set(container, 0);
                showCourse(container, 0); // первый курс без анимации

                // Запускаем автоматическое переключение
                const intervalId = setInterval(() => {
                    let currentIndex = indices.get(container) || 0;
                    currentIndex = (currentIndex + 1) % courses.length;
                    indices.set(container, currentIndex);
                    showCourse(container, currentIndex);
                }, 7000); // 7 секунд

                intervals.set(container, intervalId);
            });
        });

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

        const items = container.querySelectorAll('.xp-docs-single-div__p');
        gsap.set(items, { opacity: 0, y: -20 });
        gsap.to(items, {
            duration: 0.5,
            opacity: 1,
            y: 0,
            ease: "power2.out",
            stagger: 0.1
        });
    }

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

            // Сбрасываем интервал, чтобы 15 секунд начинались заново после клика
            clearInterval(intervals.get(container));
            const intervalId = setInterval(() => {
                let idx = indices.get(container) || 0;
                idx = (idx + 1) % courses.length;
                indices.set(container, idx);
                showCourse(container, idx);
            }, 15000);
            intervals.set(container, intervalId);
        });
    });
});
