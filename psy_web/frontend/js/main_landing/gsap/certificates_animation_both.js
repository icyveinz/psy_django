import {move_from_the_left} from "./landing_animation_template";

function certificates_animation_both() {
    const trigger_node = document.querySelector('.certificates-card-grid');
    const timeline = gsap.timeline({
        scrollTrigger: {
            trigger: trigger_node,
            start: 'top center',
            scrub: true,
            end: 'bottom center',
            // markers: true
        }
    });
    trigger_node
        .querySelectorAll('.certificate-single-div')
        .forEach((layout, index) => {
            timeline
                .from(layout, move_from_the_left())
        })
}

export default certificates_animation_both;
