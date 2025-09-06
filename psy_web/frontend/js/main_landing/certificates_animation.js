
document.addEventListener("DOMContentLoaded", function () {
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
                .from(layout, {
                    opacity: 0,
                    xPercent: -50,
                    transform: 'scale(0)'
                })
        })
});
