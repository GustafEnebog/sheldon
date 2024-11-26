window.onload = function() {
    // Get the unit ID from the data attribute in the HTML
    const unitContainer = document.getElementById('unit-container');
    const unitId = unitContainer.getAttribute('data-unit-id');

    const unitMessage = document.getElementById('unit-message'); // Assuming you have a div with id "unit-message"

    // Check if the user has visited this unit before
    if (localStorage.getItem(`visited-${unitId}`)) {
        // If they have, show the message
        unitMessage.style.display = 'block';
    } else {
        // Otherwise, hide the message
        unitMessage.style.display = 'none';
        // Mark this unit as visited in localStorage
        localStorage.setItem(`visited-${unitId}`, 'true');
    }
};
