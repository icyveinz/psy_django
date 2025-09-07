import { move_from_the_left, move_from_the_top } from "./landing_animation_template";

function xp_animation_mobile() {
    const trigger_node = document.querySelector('.xp-mobile-flex');

    const timeline = gsap.timeline({
        scrollTrigger: {
            trigger: trigger_node,
            start: 'top center',
            scrub: true,
            end: 'bottom center',
            // markers: true
        }
    });

    // Выбираем только нужные блоки первого уровня
    const blocks = trigger_node.querySelectorAll(
        ':scope > .xp-docs-single-div, :scope > .xp-about-me-mobile, :scope > .hours-container, :scope > .xp-quote-svg, :scope > .mobile-quote-p'
    );

    blocks.forEach(block => {
        if (!block.classList.contains('hours-container')) {
            // Все блоки кроме hours-container
            timeline.from(block, move_from_the_top());
        } else {
            // Только прямые потомки .hours-container__p
            const hoursItems = block.querySelectorAll(':scope > .hours-container__p');
            hoursItems.forEach(item => {
                timeline.from(item, move_from_the_left());
            });
        }
    });
}

export default xp_animation_mobile;
