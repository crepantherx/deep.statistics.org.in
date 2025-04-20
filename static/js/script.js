alert('Script is loading');

// Function to initialize the menu functionality
function initializeMenu() {
    alert('Trying to initialize menu');
    
    // Get elements
    const profileButton = document.getElementById('profile-button');
    const profileMenu = document.getElementById('profile-menu');
    const hamburger = document.getElementById('hamburger');
    const mobileNav = document.getElementById('mobile-nav');

    // Debug what elements were found
    alert('Found elements: ' + 
          '\nprofileButton: ' + (profileButton ? 'yes' : 'no') +
          '\nprofileMenu: ' + (profileMenu ? 'yes' : 'no') +
          '\nhamburger: ' + (hamburger ? 'yes' : 'no') +
          '\nmobileNav: ' + (mobileNav ? 'yes' : 'no'));

    // Only proceed if we have the necessary elements
    if (!profileButton || !profileMenu) {
        alert('Required elements not found!');
        return;
    }

    // Set up profile button click handler
    profileButton.onclick = function(e) {
        alert('Profile button clicked');
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

// Try different ways to ensure the script runs after DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeMenu);
} else {
    initializeMenu();
}

// Backup initialization
window.addEventListener('load', initializeMenu);