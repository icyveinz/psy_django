
document.addEventListener("DOMContentLoaded", function () {
    const trigger_node = document.querySelector('.services-card-grid');
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
        .querySelectorAll('.services-single-card-div')
        .forEach((layout, index) => {
            timeline
                .from(layout, {
                    opacity: 0,
                    yPercent: -50,
                    transform: 'scale(0)'
                })
        })
});
