function faq_animation () {
  const articles = document.querySelectorAll('article')

  if (!articles.length) return

  const closeFAQ = (p, btn) => {
    const tl = gsap.timeline()
    tl.to(p, { opacity: 0, y: -10, duration: 0.3, ease: 'power2.in' })
      .to(p, {
        height: 0,
        duration: 0.5,
        ease: 'power2.in',
        onComplete: () => p.classList.add('faq-p-hidden')
      }, '-=0.2')

    gsap.to(btn, { rotation: 0, transformOrigin: '50% 50%', duration: 0.3, ease: 'power2.inOut' })
  }

  const openFAQ = (p, btn) => {
    p.classList.remove('faq-p-hidden')
    gsap.timeline().fromTo(
      p,
      { height: 0, opacity: 0, y: -10 },
      { height: 'auto', opacity: 1, y: 0, duration: 0.5, ease: 'power2.out' }
    )

    gsap.to(btn, { rotation: 45, transformOrigin: '50% 50%', duration: 0.3, ease: 'power2.inOut' })
  }

  articles.forEach((article) => {
    const btn = article.querySelector('.toggle-faq')
    const p = article.querySelector('p')
    const questionBlock = article.querySelector('.faq-question-block')

    if (!btn || !p || !questionBlock) return

    p.style.overflow = 'hidden'

    questionBlock.addEventListener('click', () => {
      const isHidden = p.classList.contains('faq-p-hidden')

      // закрываем все остальные FAQ
      articles.forEach((otherArticle) => {
        const otherP = otherArticle.querySelector('p')
        const otherBtn = otherArticle.querySelector('.toggle-faq')
        if (!otherP || !otherBtn) return

        if (otherP !== p && !otherP.classList.contains('faq-p-hidden')) {
          closeFAQ(otherP, otherBtn)
        }
      })

      // открываем или закрываем текущий
      if (isHidden) {
        openFAQ(p, btn)
      } else {
        closeFAQ(p, btn)
      }
    })
  })
}

export default faq_animation
