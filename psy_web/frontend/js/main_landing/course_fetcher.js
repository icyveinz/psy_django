document.addEventListener("DOMContentLoaded", function() {


    const container = document.getElementById("courses-container");
    const previous = document.getElementById("prev-course");
    const next = document.getElementById("next-course");

    let courses = [];
    let currentIndex = 0;

    fetch('/wagtail_landing/api/study-results/')
        .then(response => response.json())
        .then(data => {
            courses = data;
            showCourses(currentIndex);
        });

    /**
    * Загружает курсы и отображает их на странице.
    *
    * @param {number} index - Индекс курса в массиве `courses` (0-based).
    * @returns {void}
    */
    function showCourses(index) {
        if (!courses.length) return;
        const course = courses[index];
        const html_template =
        `
        <h2 class="xp-docs-single-div__p">
            Курс: ${course.course_title}
        </h2>
        <p class="xp-docs-single-div__p">
            Платформа: ${course.course_platform}
        </p>
        <p class="xp-docs-single-div__p">
            Дата окончания: ${course.year_ended}
        </p>
        <p class="xp-docs-single-div__p">
            Полученные навыки:
        </p>
        <ul>
            ${course.study_results_li.map(item => `<li class="xp-docs-single-div__p">${item.skills_achieved}</li>`).join('')}
        </ul>
        `;
        container.innerHTML = html_template;
    }

    previous.addEventListener("click", function() {
        currentIndex = (currentIndex - 1 + courses.length) % courses.length;
        showCourses(currentIndex);
    });

    next.addEventListener("click", function() {
        currentIndex = (currentIndex + 1) % courses.length;
        showCourses(currentIndex);
    })
});