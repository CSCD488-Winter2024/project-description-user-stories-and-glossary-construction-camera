<?php
// Database connection parameters
$servername = "localhost";
$username = "test";
$password = "test123";
$dbname = "employees";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get form data
$email = $_POST['email'];
$new_phoneNumber = $_POST['newPhoneNumber'];
$confirm_phoneNumber = $_POST['confirmPhoneNumber'];

// Check if usernames match
if ($new_phoneNumber != $confirm_phoneNumber) {
    die("New numbers do not match.");
}

// Update username in the database
$sql = "UPDATE users SET phoneNumber='$new_phoneNumber' WHERE email='$email'";

if ($conn->query($sql) === TRUE) {
    echo "Phone Number updated successfully!";
} else {
    echo "Error updating Phone Number: " . $conn->error;
}

// Close database connection
$conn->close();
?>

