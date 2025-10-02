import { move_from_the_left, move_from_the_top } from './landing_animation_template'

function xp_animation_desktop () {
  const trigger_node = document.querySelector('.xp-grid')
  const timeline = gsap.timeline({
    scrollTrigger: {
      trigger: trigger_node,
      start: 'top center',
      scrub: true,
      end: 'bottom center'
      // markers: true
    }
  })

  const firstAnimationIndices = [0, 1, 4] // индексы, для которых 1-я анимация

  trigger_node
    .querySelectorAll('section')
    .forEach((layout, index) => {
      if (firstAnimationIndices.includes(index)) {
        timeline.from(layout, move_from_the_left())
      } else {
        timeline.from(layout, move_from_the_top())
      }
    })
}

export default xp_animation_desktop
