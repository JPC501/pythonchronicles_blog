

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

