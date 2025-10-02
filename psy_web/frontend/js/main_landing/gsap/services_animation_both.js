import { move_from_the_top } from './landing_animation_template'

function services_animation_both () {
  const trigger_node = document.querySelector('.services-card-grid')
  const timeline = gsap.timeline({
    scrollTrigger: {
      trigger: trigger_node,
      start: 'top center',
      scrub: true,
      end: 'bottom center'
      // markers: true
    }
  })
  trigger_node
    .querySelectorAll('.services-single-card-div')
    .forEach((layout, index) => {
      timeline
        .from(layout, move_from_the_top())
    })
}

export default services_animation_both
