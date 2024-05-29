const form = document.getElementById("f1"); // Replace with your form ID

form.addEventListener("submit", function(event) {
  const username = document.getElementById("username").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const dobDay = document.getElementById("dob-day").value;
  const dobMonth = document.getElementById("dob-month").value;
  const dobYear = document.getElementById("dob-year").value;

  // Simple validation example
  if (username === "" || email === "" || password === "" || dobDay === "" || dobMonth === "" || dobYear === "") {
    alert("Please fill in all required fields.");
    event.preventDefault(); // Prevent form submission
  }
});
