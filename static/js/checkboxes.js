// Simulating login state (replace with actual check in your app)
let isLoggedIn = true;  // Example login state (true or false)
let unitId = 123;  // Example unit ID (this should be dynamically provided in your template)

// Function to check if the user is logged in and on a unit
function checkLoginAndUnit() {
    if (isLoggedIn && unitId) {
        // Show checkboxes if logged in and viewing a unit
        document.getElementById('checkbox-section').style.display = 'block';
        
        // Load checkbox states from localStorage if available for the current unit
        loadCheckboxStates();
    } else {
        // Hide checkboxes if not logged in or not on a unit
        document.getElementById('checkbox-section').style.display = 'none';
    }
}

// Function to load checkbox states from localStorage based on the unit and user
function loadCheckboxStates() {
    // Generate unique keys for the unit and user
    const userId = 1;  // Replace with actual user ID (dynamically injected)
    
    const readState = localStorage.getItem(`user${userId}_unit${unitId}_readState`);
    const understoodState = localStorage.getItem(`user${userId}_unit${unitId}_understoodState`);
    
    // Set the checkbox states only if they exist in localStorage for this unit
    if (readState !== null) {
        document.getElementById('read').checked = (readState === 'true');
    }
    if (understoodState !== null) {
        document.getElementById('understood').checked = (understoodState === 'true');
    }
}

// Event listeners to save the state of checkboxes in localStorage
document.getElementById('read').addEventListener('change', function() {
    // Save the state of the "Read" checkbox
    const userId = 1;  // Replace with actual user ID (dynamically injected)
    localStorage.setItem(`user${userId}_unit${unitId}_readState`, this.checked);
});

document.getElementById('understood').addEventListener('change', function() {
    // If "Understood" is checked but "Read" is unchecked, automatically check "Read"
    if (this.checked && !document.getElementById('read').checked) {
        document.getElementById('read').checked = true;
        const userId = 1;  // Replace with actual user ID (dynamically injected)
        localStorage.setItem(`user${userId}_unit${unitId}_readState`, 'true');
    }
    
    // Save the state of the "Understood" checkbox
    const userId = 1;  // Replace with actual user ID (dynamically injected)
    localStorage.setItem(`user${userId}_unit${unitId}_understoodState`, this.checked);
});

// Run the checkLoginAndUnit function to update the page based on login and unit state
checkLoginAndUnit();
