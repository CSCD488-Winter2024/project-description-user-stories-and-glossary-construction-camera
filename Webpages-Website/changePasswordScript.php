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
$new_password = $_POST['newPassword'];
$confirm_password = $_POST['confirmPassword'];

// Check if passwords match
if ($new_password != $confirm_password) {
    die("New passwords do not match.");
}

// Hash the new password 
// $hashed_password = password_hash($new_password, PASSWORD_DEFAULT);
var_dump($email, $new_password, $sql);
// Update password in the database 
$sql = "UPDATE users SET password='$new_password' WHERE email='$email'";

if ($conn->query($sql) === TRUE) {
    echo "Password updated successfully!";
} else {
    echo "Error updating password: " . $conn->error;
}

// Close database connection
$conn->close();
?>

