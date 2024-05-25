function myFunction() {
    var element = document.body;
    element.classList.toggle("dark-mode");
 }

let registeredUsername = "";
let registeredPassword = "";

document.getElementById("registerForm").addEventListener("submit", function(event) {
    event.preventDefault();
    alert("Your account has been successfully created!");
    registeredUsername = document.getElementById("regUsername").value;
    registeredPassword = document.getElementById("regPassword").value;
    document.getElementById("registrationForm").style.display = "none";
    document.getElementById("loginForm").style.display = "block";
});

document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const output = document.getElementById("output");

    if (username === registeredUsername && password === registeredPassword) {
        output.innerHTML = "Access Granted";
        const action = prompt("Launch Missiles, Request Supplies, Open Digital Library or Log Out?");
        handleAction(action);
    } else {
        output.innerHTML = "Access Denied";
    }
});

function handleAction(action) {
    const output = document.getElementById("output");
    switch(action) {
        case "Launch Missiles":
            output.innerHTML = "Choose a target";
            setTimeout(() => {
                output.innerHTML = "Launching Missiles...";
            }, 2000);  
            output.innerHTML = "Destroyed";   
            break;
        case "Request Supplies":
            output.innerHTML = "Requesting Supplies...";
            break;
        case "Log Out":
            output.innerHTML = "Logging Out...";
            break;
        case "Open Digital Library":
            output.innerHTML = "Opening Digital Library...";
            break;
        default:
            output.innerHTML = "Invalid Action";
    }
}


