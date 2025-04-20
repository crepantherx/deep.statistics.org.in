// Function to initialize the menu functionality
function initializeMenu() {
    // Get elements
    const profileButton = document.getElementById('profile-button');
    const profileMenu = document.getElementById('profile-menu');
    const hamburger = document.getElementById('hamburger');
    const mobileNav = document.getElementById('mobile-nav');

    // Only proceed if we have the necessary elements
    if (!profileButton || !profileMenu) {
        console.log('Required elements not found');
        return;
    }

    // Set up profile button click handler
    profileButton.onclick = function(e) {
        e.preventDefault();
        e.stopPropagation();
        profileMenu.classList.toggle('active');
        
        // Close mobile menu if it exists
        if (mobileNav) mobileNav.classList.remove('active');
        if (hamburger) hamburger.classList.remove('active');
    };

    // Prevent menu close when clicking inside
    profileMenu.onclick = function(e) {
        e.stopPropagation();
    };

    // Set up hamburger menu if it exists
    if (hamburger && mobileNav) {
        hamburger.onclick = function(e) {
            e.preventDefault();
            e.stopPropagation();
            hamburger.classList.toggle('active');
            mobileNav.classList.toggle('active');
            profileMenu.classList.remove('active');
        };
    }

    // Close menus when clicking outside
    document.onclick = function() {
        profileMenu.classList.remove('active');
        if (mobileNav) mobileNav.classList.remove('active');
        if (hamburger) hamburger.classList.remove('active');
    };
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeMenu);
} else {
    initializeMenu();
}

// Backup initialization
window.addEventListener('load', initializeMenu);