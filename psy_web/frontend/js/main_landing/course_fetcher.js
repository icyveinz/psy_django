window.addEventListener("load", function() {

    const containers = document.querySelectorAll(".courses-container");
    let courses = [];
    const indices = new Map();
    const intervals = new Map();
    const autoSwitchDelay = 7000; // 7 секунд
    const pauseAfterClick = 15000; // пауза после клика

    // Функция для установки фиксированной высоты на основе самого большого курса
    function setFixedHeight(container) {
        let maxHeight = 0;

        courses.forEach(course => {
            const tempDiv = document.createElement('div');
            tempDiv.style.visibility = 'hidden';
            tempDiv.style.position = 'absolute';
            tempDiv.innerHTML = `
                <h2 class="xp-docs-single-div__p">Курс: ${course.course_title}</h2>
                <p class="xp-docs-single-div__p">Платформа: ${course.course_platform}</p>
                <p class="xp-docs-single-div__p">Дата окончания: ${course.year_ended}</p>
                <p class="xp-docs-single-div__p">Полученные навыки:</p>
                <ul>
                    ${course.study_results_li.map(item => `<li class="xp-docs-single-div__p">${item.skills_achieved}</li>`).join('')}
                </ul>
            `;
            container.appendChild(tempDiv);
            maxHeight = Math.max(maxHeight, tempDiv.offsetHeight);
            container.removeChild(tempDiv);
        });

        container.style.height = `${maxHeight}px`;
    }

    // Показ курса с анимацией
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

    // Авто-переключение через рекурсивный setTimeout
    function startAutoSwitch(container, delay = autoSwitchDelay) {
        clearTimeout(intervals.get(container));
        const timeoutId = setTimeout(() => {
            let currentIndex = indices.get(container) || 0;
            currentIndex = (currentIndex + 1) % courses.length;
            indices.set(container, currentIndex);
            showCourse(container, currentIndex);
            startAutoSwitch(container); // запускаем следующий цикл
        }, delay);
        intervals.set(container, timeoutId);
    }

    // Получаем данные
    fetch('/wagtail_landing/api/study-results/')
        .then(response => {
            if (!response.ok) throw new Error('Network response was not ok');
            return response.json();
        })
        .then(data => {
            courses = data;
            if (!courses.length) return;

            containers.forEach(container => {
                indices.set(container, 0);

                // Ждем, пока шрифты полностью загрузятся, для точного измерения высоты
                document.fonts.ready.then(() => {
                    setFixedHeight(container); // один раз задаём высоту
                    showCourse(container, 0);  // показываем первый курс
                    startAutoSwitch(container); // запускаем авто-переключение
                });
            });
        })
        .catch(err => console.error(err));

    // Обработка кликов на стрелки
    document.querySelectorAll(".prev-course, .next-course").forEach(button => {
        const handleClick = (e) => {
            e.preventDefault();
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

            // пауза авто-переключения после клика
            startAutoSwitch(container, pauseAfterClick);
        };

        button.addEventListener("click", handleClick);
        button.addEventListener("touchstart", handleClick); // для мобильных
    });
});