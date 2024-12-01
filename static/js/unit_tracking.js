window.onload = function() {
    const unitContainer = document.getElementById('unit-container');
    if (!unitContainer) {
        console.error('unit-container element is missing!');
        return;
    }
    
    const unitId = unitContainer.getAttribute('data-unit-id');
    const unitMessage = document.getElementById('unit-message');
    
    if (!unitMessage) {
        console.error('unit-message element is missing!');
        return;
    }

    if (localStorage.getItem(`visited-${unitId}`)) {
        unitMessage.style.display = 'block';
    } else {
        unitMessage.style.display = 'none';
        localStorage.setItem(`visited-${unitId}`, 'true');
    }
};
