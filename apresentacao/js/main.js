/**
 * HIGH HOUSE — Apresentação Interativa (v2)
 * Interações: scroll reveal, progress nav (11 seções), parallax, keyboard nav.
 * Sem dependências externas.
 */

(function () {
  'use strict';

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ==========================================
  // 1. SCROLL REVEAL (Intersection Observer)
  // ==========================================

  const revealElements = document.querySelectorAll('.reveal');

  if (!prefersReducedMotion && 'IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            revealObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -35px 0px' }
    );

    revealElements.forEach((el) => revealObserver.observe(el));
  } else {
    revealElements.forEach((el) => el.classList.add('is-visible'));
  }


  // ==========================================
  // 2. PROGRESS NAVIGATION
  // ==========================================

  const progressNav = document.getElementById('progressNav');
  const navDots = progressNav ? progressNav.querySelectorAll('.progress-nav__dot') : [];
  const sections = document.querySelectorAll('main > section[id]');

  // Click → smooth scroll
  navDots.forEach((dot) => {
    dot.addEventListener('click', () => {
      const targetId = dot.getAttribute('data-target');
      const target = document.getElementById(targetId);
      if (target) target.scrollIntoView({ behavior: 'smooth' });
    });
  });

  // Track active section
  if (sections.length > 0 && 'IntersectionObserver' in window) {
    const sectionObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const activeId = entry.target.id;
            navDots.forEach((dot) => {
              dot.classList.toggle('is-active', dot.getAttribute('data-target') === activeId);
            });
          }
        });
      },
      { threshold: 0, rootMargin: '-45% 0px -45% 0px' }
    );

    sections.forEach((s) => sectionObserver.observe(s));
  }


  // ==========================================
  // 3. PARALLAX ON HERO ORBS
  // ==========================================

  const heroOrbs = document.querySelectorAll('.hero__orb');

  if (!prefersReducedMotion && heroOrbs.length > 0) {
    let ticking = false;
    const speeds = [0.03, 0.05, 0.04];

    function updateParallax() {
      const scrollY = window.scrollY;
      if (scrollY < window.innerHeight * 1.5) {
        heroOrbs.forEach((orb, i) => {
          orb.style.transform = 'translateY(' + (scrollY * (speeds[i] || 0.03)) + 'px)';
        });
      }
      ticking = false;
    }

    window.addEventListener('scroll', () => {
      if (!ticking) { requestAnimationFrame(updateParallax); ticking = true; }
    }, { passive: true });
  }


  // ==========================================
  // 4. HIDE SCROLL INDICATOR ON SCROLL
  // ==========================================

  const scrollIndicator = document.querySelector('.hero__scroll');

  if (scrollIndicator && !prefersReducedMotion) {
    let hidden = false;
    window.addEventListener('scroll', () => {
      if (!hidden && window.scrollY > 80) {
        scrollIndicator.style.opacity = '0';
        scrollIndicator.style.transition = 'opacity 0.6s ease';
        hidden = true;
      }
    }, { passive: true });
  }


  // ==========================================
  // 5. KEYBOARD NAVIGATION
  // ==========================================

  document.addEventListener('keydown', (e) => {
    if (e.key !== 'ArrowDown' && e.key !== 'ArrowUp') return;

    const current = document.querySelector('.progress-nav__dot.is-active');
    if (!current) return;

    const idx = Array.from(navDots).indexOf(current);
    const next = e.key === 'ArrowDown'
      ? Math.min(idx + 1, navDots.length - 1)
      : Math.max(idx - 1, 0);

    if (next !== idx) {
      const target = document.getElementById(navDots[next].getAttribute('data-target'));
      if (target) { e.preventDefault(); target.scrollIntoView({ behavior: 'smooth' }); }
    }
  });

})();
