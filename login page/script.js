// Hardcoded username and password
const username = 'admin';
const password = 'admin';

// Getting username and password elements
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');

// Getting the div element to print the error message
const errorDiv = document.getElementById('error-container');


// Adding an event listener to the login button
document.getElementById('login').addEventListener('click', function() {
    const enteredUsername = usernameInput.value.trim(); // Trim input for spaces before and after the input
    const enteredPassword = passwordInput.value.trim(); // Trim input for spaces before and after the input
    event.preventDefault();// Prevent the default form submission
    if (!enteredUsername || !enteredPassword) {
        errorDiv.style.color = 'red';
        errorDiv.style.display = 'block';
        errorDiv.innerHTML = 'Please fill in both fields'; // Handle empty inputs
        return;
    }

    if (enteredUsername === username && enteredPassword === password) {
        errorDiv.style.color = 'green';
        errorDiv.style.display = 'block';
        errorDiv.innerHTML = 'Login successful';
    } else {
        errorDiv.style.color = 'red';
        errorDiv.style.display = 'block';
        errorDiv.innerHTML = 'Invalid username or password';
    }
});