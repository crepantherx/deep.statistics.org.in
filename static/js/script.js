document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.getElementById('hamburger');
    const mobileNav = document.getElementById('mobile-nav');
    const profileButton = document.getElementById('profile-button');
    const profileMenu = document.getElementById('profile-menu');

    console.log('Elements found:', {
        hamburger: !!hamburger,
        mobileNav: !!mobileNav,
        profileButton: !!profileButton,
        profileMenu: !!profileMenu
    });

    if (!profileButton || !profileMenu) {
        console.error('Profile elements not found:', {
            profileButton: !!profileButton,
            profileMenu: !!profileMenu
        });
        return;
    }

    // Toggle mobile menu
    hamburger?.addEventListener('click', (e) => {
        console.log('Hamburger clicked');
        e.stopPropagation();
        hamburger.classList.toggle('active');
        mobileNav.classList.toggle('active');
        // Close profile menu when opening mobile menu
        profileMenu.classList.remove('active');
    });

    // Toggle profile menu
    profileButton.addEventListener('click', (e) => {
        console.log('Profile button clicked');
        e.stopPropagation();
        profileMenu.classList.toggle('active');
        console.log('Profile menu active:', profileMenu.classList.contains('active'));
        // Close mobile menu when opening profile menu
        hamburger?.classList.remove('active');
        mobileNav?.classList.remove('active');
    });

    // Prevent menu close when clicking inside the menu
    profileMenu.addEventListener('click', (e) => {
        console.log('Click inside profile menu');
        e.stopPropagation();
    });

    // Close menus when clicking outside
    document.addEventListener('click', () => {
        console.log('Document clicked, closing menus');
        profileMenu.classList.remove('active');
        hamburger?.classList.remove('active');
        mobileNav?.classList.remove('active');
    });
});