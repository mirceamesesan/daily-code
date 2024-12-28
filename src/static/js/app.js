// Function to validate the form
function validateForm() {
    var description = document.getElementById('description').value;
    var duration = document.getElementById('duration').value;
    var errorMessage = document.getElementById('error-message');

    if (description === 'Write your description here...' || duration === '0.00') {
        errorMessage.style.display = 'block';
        errorMessage.innerHTML = 'Please enter valid description and duration.';
        return false;
    }
    errorMessage.style.display = 'hidden';
    return true;
}

// Sudoku Screen
var sudoku = document.getElementById('sudoku');
var cells = document.querySelectorAll('.cell');
var options = document.getElementById('options');
var optionsCells = document.querySelectorAll('.item');

for (var i = 0; i < cells.length; i++) {
    // check for empty cells and check if][l[-,l]] any other cell is already 'selected'
    cells[i].addEventListener('click', function() {
        if (this.innerHTML === '') {
            if (document.querySelector('.selected')) {
                document.querySelector('.selected').classList.toggle('selected');
            }
            this.classList.toggle('selected');
            for (var j = 0; j < optionsCells.length; j++) {
                optionsCells[j].classList.add('selected');
            }
            console.log(options);
        }
    });
}