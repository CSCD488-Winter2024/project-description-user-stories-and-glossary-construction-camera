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
$email = $conn->real_escape_string($_POST['email']);
$new_username = $conn->real_escape_string($_POST['newUsername']);
$confirm_username = $conn->real_escape_string($_POST['confirmUsername']);

var_dump($_POST);

echo "Email: " . $email . "<br>";
echo "New Username: " . $new_username . "<br>";
echo "Confirm Username: " . $confirm_username . "<br>";

// Check if usernames match
if ($new_username != $confirm_username) {
    die("New usernames do not match.");
}

var_dump($email, $new_username, $sql);
// Update password in the database 
$sql = "UPDATE users SET username='$new_username' WHERE email='$email'";

if ($conn->query($sql) === TRUE) {
    echo "Username updated successfully!";
} else {
    echo "Error updating username: " . $conn->error;
}

// Close database connection
$conn->close();
?>

