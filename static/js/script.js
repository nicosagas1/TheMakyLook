// #region Función para abrir y cerrar el menú en móvil
function toggleMenu() {
    const mobileNav = document.querySelector('.mobile-nav');
    mobileNav.classList.toggle('active');
}

// Función para cerrar el menú cuando se hace clic en el ícono de cerrar
const closeMenu = document.querySelector('.close-menu');
closeMenu.addEventListener('click', () => {
    const mobileNav = document.querySelector('.mobile-nav');
    mobileNav.classList.remove('active');
});

// Cerrar el menú cuando se hace clic en un enlace dentro del menú móvil
const mobileLinks = document.querySelectorAll('.mobile-link');
mobileLinks.forEach(link => {
    link.addEventListener('click', () => {
        const mobileNav = document.querySelector('.mobile-nav');
        mobileNav.classList.remove('active');
    });
});
// #endregion

// #region Función para abrir y cerrar el modal de reserva
document.addEventListener("DOMContentLoaded", function () {
    const abrirModal = document.getElementById("abrirModal");
    const cerrarModal = document.getElementById("cerrarModal");
    const modal = document.getElementById("reservaModal");
    const reservaForm = document.getElementById("reservaForm");
  
    // Abrir el modal cuando se hace clic en el botón
    abrirModal.addEventListener("click", function () {
      modal.classList.remove("hidden");
      modal.classList.add("flex");
    });
  
    // Cerrar el modal cuando se hace clic en el botón de cerrar
    cerrarModal.addEventListener("click", function () {
      modal.classList.remove("flex");
      modal.classList.add("hidden");
    });
});
// #endregion

// #region Función para abrir y cerrar el modal de reserva
const abrirModal = document.getElementById("abrirModal");
const cerrarModal = document.getElementById("cerrarModal");
const modal = document.getElementById("reservaModal");

abrirModal.addEventListener("click", () => {
  modal.classList.remove("hidden");
  modal.classList.add("flex");
});

cerrarModal.addEventListener("click", () => {
  modal.classList.remove("flex");
  modal.classList.add("hidden");
});
// #endregion

// #region Función testimonios
const testimonials = document.querySelectorAll('.testimonial');
const dots = document.querySelectorAll('.slider-dot');
const leftArrow = document.querySelector('.left-arrow');
const rightArrow = document.querySelector('.right-arrow');

let currentIndex = 0;

function showTestimonial(index) {
        testimonials.forEach((t, i) => {
            t.style.display = i === index ? 'block' : 'none';
            dots[i].classList.toggle('active', i === index);
        });
    }

    function nextTestimonial() {
        currentIndex = (currentIndex + 1) % testimonials.length;
        showTestimonial(currentIndex);
    }

    function prevTestimonial() {
        currentIndex = (currentIndex - 1 + testimonials.length) % testimonials.length;
        showTestimonial(currentIndex);
    }

    rightArrow.addEventListener('click', nextTestimonial);
    leftArrow.addEventListener('click', prevTestimonial);
    dots.forEach((dot, i) => {
        dot.addEventListener('click', () => {
            currentIndex = i;
            showTestimonial(i);
        });
    });

    // Mostrar el primero al cargar
    showTestimonial(currentIndex);
// #endregion

