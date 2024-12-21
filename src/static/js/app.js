// Function to validate the form
function validateForm() {
    var description = document.getElementById('description').value;
    var duration = document.getElementById('duration').value;
    var errorMessage = document.getElementById('error-message');

    if (description === 'Write your description here...' || duration === '0') {
        errorMessage.style.display = 'block';
        errorMessage.innerHTML = 'Please enter valid description and duration.';
        return false;
    }
    errorMessage.style.display = 'hidden';
    return true;
}