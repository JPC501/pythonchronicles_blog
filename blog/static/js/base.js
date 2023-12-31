

document.addEventListener('DOMContentLoaded', (event) => {
    const button = document.querySelector('[data-collapse-toggle="mega-menu-icons"]');
    const menu = document.getElementById('mega-menu-icons');
    
    button.addEventListener('click', () => {
        const isExpanded = button.getAttribute('aria-expanded') === 'true';
        button.setAttribute('aria-expanded', !isExpanded);
        menu.classList.toggle('hidden');
    });
});

document.addEventListener('DOMContentLoaded', (event) => {
    const menuButton = document.getElementById('mega-menu-icons-dropdown-button');
    const menuDropdown = document.getElementById('mega-menu-icons-dropdown');
    
    menuButton.addEventListener('click', () => {
        menuDropdown.classList.toggle('hidden');
        menuDropdown.classList.toggle('grid');
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const dropdownButton = document.getElementById("dropdown-button");
    const userDropdown = document.getElementById("user-dropdown");

    let isOpen = false;

    dropdownButton.addEventListener("click", function () {
        isOpen = !isOpen;
        userDropdown.style.display = isOpen ? "block" : "none";
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const toggleLinks = document.querySelectorAll(".toggle-link");

    toggleLinks.forEach((link) => {
        link.addEventListener("click", function(event) {
        event.preventDefault();
        const submenu = this.nextElementSibling;
        submenu.classList.toggle("hidden");
        });
    });
});
