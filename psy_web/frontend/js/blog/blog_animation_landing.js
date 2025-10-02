import { move_from_the_top } from '../main_landing/gsap/landing_animation_template'

function blog_animation_landing () {
  const trigger_node = document.querySelector('.blog-grid')
  const timeline = gsap.timeline({
    scrollTrigger: {
      trigger: trigger_node,
      start: 'top bottom-=25%',
      scrub: true,
      end: 'bottom bottom-=25%'
      // markers: true
    }
  })
  const divChildren = trigger_node.querySelectorAll(':scope > div')
  divChildren
    .forEach(child => {
      timeline
        .from(child, move_from_the_top())
    })
}

export default blog_animation_landing
