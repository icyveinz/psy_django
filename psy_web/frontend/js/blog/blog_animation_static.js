import {move_from_the_top} from "../main_landing/gsap/landing_animation_template";

function blog_animation_static() {
    const trigger_node = document.querySelector('.blog-grid');
    if (!trigger_node) return; // защита, если блока нет

    const timeline = gsap.timeline(); // без ScrollTrigger

    const divChildren = trigger_node.querySelectorAll(':scope > div');

    divChildren.forEach(child => {
        timeline.from(child, move_from_the_top());
    });
}

export default blog_animation_static;
