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


// ✅ PASTE YOUR GOOGLE APPS SCRIPT WEB APP URL BELOW
const GOOGLE_SHEET_URL = 'https://script.google.com/macros/s/AKfycbxL4yKMIO9Me92_FB_9l3se0TOM36w-B2yLa0_ufM00JbjZ5AokPuW4QWMbC_kp1hXYSQ/exec';

if (contactForm && formStatus) {
  contactForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const submitBtn = contactForm.querySelector('button[type="submit"]');
    const originalText = submitBtn.innerHTML;

    // Collect form data as JSON
    const formData = {
      name: contactForm.querySelector('[name="name"]').value,
      email: contactForm.querySelector('[name="email"]').value,
      phone: contactForm.querySelector('[name="phone"]').value,
      service: contactForm.querySelector('[name="service"]').value,
      message: contactForm.querySelector('[name="message"]').value,
    };

    // Show loading state
    submitBtn.disabled = true;
    submitBtn.innerHTML = 'Sending… <span>⏳</span>';
    formStatus.textContent = '';
    formStatus.style.color = '';

    try {
      // Use text/plain (CORS-safelisted) with JSON body — Apps Script still parses it correctly
      await fetch(GOOGLE_SHEET_URL, {
        method: 'POST',
        mode: 'no-cors',
        headers: { 'Content-Type': 'text/plain;charset=utf-8' },
        body: JSON.stringify(formData),
      });

      formStatus.textContent = '✅ Thank you! Your inquiry has been submitted successfully.';
      formStatus.style.color = '#16804c';
      contactForm.reset();
    } catch (error) {
      formStatus.textContent = '❌ Something went wrong. Please try again or email us directly.';
      formStatus.style.color = '#dc2626';
      console.error('Form submission error:', error);
    } finally {
      submitBtn.disabled = false;
      submitBtn.innerHTML = originalText;
    }
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
