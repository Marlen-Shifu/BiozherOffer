const nav = document.querySelector('.nav');
const menuBtn = document.querySelector('.menu-btn');
const navLinkItems = document.querySelector('.nav_link-items');
const headers = document.querySelectorAll("[data-name='accordeon-title']");

window.addEventListener("scroll", () => {
    let scrollPos = window.scrollY;

    if(scrollPos > 100) {
        nav.classList.add('active');
    } else {
        nav.classList.remove('active');
    }
})


let menuOpen = false;

menuBtn.addEventListener('click', () => {
    if (!menuOpen) {
        menuBtn.classList.add('menu_burger-open');
        navLinkItems.classList.add('active');
        document.body.style.overflow = "hidden";
        menuOpen = true;
    } else {
        menuBtn.classList.remove('menu_burger-open');
        navLinkItems.classList.remove('active');
        document.body.style.overflow = "visible";
        menuOpen = false;
    }
})


headers.forEach(function (item) {
    item.addEventListener('click', showContent);
})

function showContent() {
    this.nextElementSibling.classList.toggle('hidden');
}
