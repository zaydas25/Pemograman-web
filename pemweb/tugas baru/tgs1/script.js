// Slider Script
let sliderIndex = 0;

function showSlides() {
    const slides = document.querySelectorAll('.slide');
    slides.forEach((slide, index) => {
        slide.style.transform = `translateX(-${sliderIndex * 100}%)`;
    });
    sliderIndex = (sliderIndex + 1) % slides.length;
}

setInterval(showSlides, 3000);
