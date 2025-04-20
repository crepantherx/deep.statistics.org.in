document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.getElementById('hamburger');
    const mobileNav = document.getElementById('mobile-nav');
    const profileButton = document.getElementById('profile-button');
    const profileMenu = document.getElementById('profile-menu');

    // Toggle mobile menu
    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        mobileNav.classList.toggle('active');
        // Close profile menu when opening mobile menu
        profileMenu.classList.remove('active');
    });

    // Toggle profile menu
    profileButton.addEventListener('click', () => {
        profileMenu.classList.toggle('active');
        // Close mobile menu when opening profile menu
        hamburger.classList.remove('active');
        mobileNav.classList.remove('active');
    });

    // Close menus when clicking outside
    document.addEventListener('click', (e) => {
        if (!hamburger.contains(e.target) && !mobileNav.contains(e.target)) {
            hamburger.classList.remove('active');
            mobileNav.classList.remove('active');
        }
        if (!profileButton.contains(e.target) && !profileMenu.contains(e.target)) {
            profileMenu.classList.remove('active');
        }
    });
});