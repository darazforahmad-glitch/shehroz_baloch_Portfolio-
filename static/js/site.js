/* Portfolio interactions. Progressive enhancement only: every section is
   readable and usable with this file blocked. */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------------------------------------------------- scroll reveal */
  var revealables = document.querySelectorAll('.reveal');

  if (!('IntersectionObserver' in window) || reduceMotion) {
    revealables.forEach(function (el) { el.classList.add('is-visible'); });
  } else {
    var revealer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          revealer.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

    revealables.forEach(function (el) { revealer.observe(el); });
  }

  /* ------------------------------------- sticky nav + scroll progress */
  var nav = document.getElementById('nav');
  var progress = document.getElementById('nav-progress');
  var ticking = false;

  function onScroll() {
    var y = window.scrollY || window.pageYOffset;

    if (nav) { nav.classList.toggle('is-stuck', y > 12); }

    if (progress) {
      var height = document.documentElement.scrollHeight - window.innerHeight;
      var pct = height > 0 ? (y / height) * 100 : 0;
      progress.style.width = Math.min(100, Math.max(0, pct)) + '%';
    }
    ticking = false;
  }

  window.addEventListener('scroll', function () {
    if (!ticking) {
      window.requestAnimationFrame(onScroll);
      ticking = true;
    }
  }, { passive: true });
  onScroll();

  /* --------------------------------------------- active section link */
  var navLinks = Array.prototype.slice.call(document.querySelectorAll('[data-navlink]'));
  var sections = navLinks
    .map(function (link) { return document.getElementById(link.dataset.navlink); })
    .filter(Boolean);

  if (sections.length && 'IntersectionObserver' in window) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) { return; }
        navLinks.forEach(function (link) {
          link.classList.toggle('is-active', link.dataset.navlink === entry.target.id);
        });
      });
    }, { rootMargin: '-45% 0px -50% 0px', threshold: 0 });

    sections.forEach(function (section) { spy.observe(section); });
  }

  /* ----------------------------------------------------- mobile menu */
  var burger = document.getElementById('nav-burger');
  var links = document.getElementById('nav-links');

  function closeMenu() {
    if (!links || !burger) { return; }
    links.classList.remove('is-open');
    burger.setAttribute('aria-expanded', 'false');
    burger.setAttribute('aria-label', 'Open menu');
  }

  if (burger && links) {
    burger.addEventListener('click', function () {
      var open = links.classList.toggle('is-open');
      burger.setAttribute('aria-expanded', String(open));
      burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    });

    links.addEventListener('click', function (event) {
      if (event.target.closest('a')) { closeMenu(); }
    });

    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') { closeMenu(); }
    });

    window.addEventListener('resize', function () {
      if (window.innerWidth > 820) { closeMenu(); }
    });
  }

  /* --------------------------------------------- hero word rotator */
  var rotator = document.getElementById('rotator');

  if (rotator && !reduceMotion) {
    var words = (rotator.dataset.words || '')
      .split('|')
      .map(function (word) { return word.trim(); })
      .filter(Boolean);

    if (words.length > 1) {
      var index = 0;
      var chars = words[0].length;
      var deleting = false;

      var tick = function () {
        var word = words[index];
        chars += deleting ? -1 : 1;
        rotator.textContent = word.slice(0, chars);

        var delay = deleting ? 45 : 85;

        if (!deleting && chars === word.length) {
          deleting = true;
          delay = 1900;                      // hold the finished word
        } else if (deleting && chars === 0) {
          deleting = false;
          index = (index + 1) % words.length;
          delay = 320;
        }
        window.setTimeout(tick, delay);
      };

      window.setTimeout(tick, 1900);
    }
  }

  /* ------------------------------------- keep the form in view on error */
  var form = document.querySelector('.form');
  if (form && document.querySelector('.field__err, .notice--err')) {
    var firstError = document.querySelector('.field__err');
    if (firstError) {
      var field = firstError.closest('.field');
      var input = field && field.querySelector('input, textarea');
      if (input) { input.focus({ preventScroll: true }); }
    }
    form.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'center' });
  }

  /* ---------------- tidy the ?sent=1 marker out of the address bar ---- */
  if (window.history.replaceState && window.location.search.indexOf('sent=1') !== -1) {
    window.history.replaceState({}, '', window.location.pathname + '#contact');
  }
}());
