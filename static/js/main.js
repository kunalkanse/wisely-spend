// main.js — students will add JavaScript here as features are built

// Video Modal Functionality
document.addEventListener('DOMContentLoaded', function() {
    const howItWorksBtn = document.getElementById('how-it-works-btn');
    const videoModal = document.getElementById('video-modal');
    const modalOverlay = document.getElementById('modal-overlay');
    const modalClose = document.getElementById('modal-close');
    const videoIframe = document.getElementById('video-iframe');

    // Placeholder YouTube URL - replace with actual video URL later
    const videoUrl = 'https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1&rel=0';

    // Open modal
    function openModal() {
        videoIframe.src = videoUrl;
        videoModal.classList.add('active');
        document.body.style.overflow = 'hidden'; // Prevent background scrolling
    }

    // Close modal
    function closeModal() {
        videoIframe.src = ''; // Stop video by removing src
        videoModal.classList.remove('active');
        document.body.style.overflow = ''; // Restore scrolling
    }

    // Event listeners
    if (howItWorksBtn) {
        howItWorksBtn.addEventListener('click', function(e) {
            e.preventDefault();
            openModal();
        });
    }

    if (modalClose) {
        modalClose.addEventListener('click', closeModal);
    }

    if (modalOverlay) {
        modalOverlay.addEventListener('click', function(e) {
            // Only close if clicking the overlay itself, not its children
            if (e.target === modalOverlay) {
                closeModal();
            }
        });
    }

    // Close modal with Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && videoModal.classList.contains('active')) {
            closeModal();
        }
    });
});
