function article_animation () {
  gsap.from('.image-reveal img', {
    scrollTrigger: {
      trigger: '.image-reveal',
      start: 'top 80%',
      toggleActions: 'play none none reverse'
    },
    yPercent: 100,
    duration: 1.2,
    ease: 'power4.out'
  })
}

document.addEventListener('DOMContentLoaded', () => {
  article_animation()
})
