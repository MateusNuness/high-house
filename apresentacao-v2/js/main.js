/* ============================================================
   HIGH HOUSE — apresentacao-v2 · main.js
   Scroll reveal + nav lateral ativa
   ============================================================ */

(function () {
  'use strict';

  /* ----------------------------------------------------------
     REVEAL ON SCROLL
     ---------------------------------------------------------- */
  const revealEls = document.querySelectorAll('.reveal');

  const revealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          revealObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12 }
  );

  revealEls.forEach((el) => revealObserver.observe(el));


  /* ----------------------------------------------------------
     NAV LATERAL — seção ativa
     ---------------------------------------------------------- */
  const sections   = document.querySelectorAll('section[id]');
  const navItems   = document.querySelectorAll('.side-nav__item');

  const navObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const id = entry.target.getAttribute('id');
          navItems.forEach((item) => {
            item.classList.toggle(
              'is-active',
              item.getAttribute('href') === '#' + id
            );
          });
        }
      });
    },
    { rootMargin: '-40% 0px -55% 0px' }
  );

  sections.forEach((sec) => navObserver.observe(sec));


  /* ----------------------------------------------------------
     SCROLL SUAVE para links da nav
     ---------------------------------------------------------- */
  navItems.forEach((item) => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
      const target = document.querySelector(item.getAttribute('href'));
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

})();
