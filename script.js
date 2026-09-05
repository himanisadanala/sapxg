const menuToggle = document.querySelector('.menu-toggle');
const mainNav = document.querySelector('.main-nav');
const contactForm = document.querySelector('#contact-form');
const formStatus = document.querySelector('.form-status');

function closeMenu() {
  if (menuToggle && mainNav) {
    menuToggle.setAttribute('aria-expanded', 'false');
    mainNav.classList.remove('is-open');
    document.body.classList.remove('nav-open');
  }
}

function openMenu() {
  if (menuToggle && mainNav) {
    menuToggle.setAttribute('aria-expanded', 'true');
    mainNav.classList.add('is-open');
    document.body.classList.add('nav-open');
  }
}

if (menuToggle && mainNav) {
  menuToggle.addEventListener('click', (e) => {
    e.preventDefault();
    e.stopPropagation();
    const isOpen = mainNav.classList.contains('is-open');
    if (isOpen) {
      closeMenu();
    } else {
      openMenu();
    }
  });

  // Close menu when clicking outside
  document.addEventListener('click', (e) => {
    if (mainNav.classList.contains('is-open') && !mainNav.contains(e.target) && !menuToggle.contains(e.target)) {
      closeMenu();
    }
  });

  // Close menu on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && mainNav.classList.contains('is-open')) {
      closeMenu();
      menuToggle.focus();
    }
  });
}

document.querySelectorAll('.main-nav a').forEach((link) => {
  link.addEventListener('click', () => {
    closeMenu();
  });
});


if (contactForm && formStatus) {
  contactForm.addEventListener('submit', (event) => {
    event.preventDefault();
    formStatus.textContent = 'Thank you. Your inquiry has been received.';
    contactForm.reset();
  });
}

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.style.animationPlayState = 'running';
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal').forEach((element) => {
  element.style.animationPlayState = 'paused';
  revealObserver.observe(element);
});
