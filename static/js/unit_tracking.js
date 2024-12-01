document.addEventListener('DOMContentLoaded', function () {
    const unitContainer = document.getElementById('unit-container');
    const unitMessage = document.getElementById('unit-message');

    // Check if the necessary elements exist
    if (!unitContainer || !unitMessage) {
        console.error('Required elements are missing!');
        return;
    }

    // Retrieve unitId from the container
    const unitId = unitContainer.getAttribute('data-unit-id');
    if (!unitId) {
        console.error('data-unit-id is missing on unit-container!');
        return;
    }

    // Show or hide the message based on visit status
    if (localStorage.getItem(`visited-${unitId}`)) {
        unitMessage.style.display = 'block';
    } else {
        unitMessage.style.display = 'none';
        localStorage.setItem(`visited-${unitId}`, 'true');
    }
});
