<?php
// Database connection parameters
$host = "localhost"; // Change this if your database is hosted elsewhere
$username = "test";
$password = "test123";
$database = "employees";

// Connect to the database
$connection = new mysqli_connect($host, $username, $password, $database);

// Check for connection errors
if ($connection->connect_error) {
    die("Connection failed: " . $connection->connect_error);
}

// Get username and password from the AJAX request
$username = $_POST['username'];
$password = $_POST['password'];

// SQL query to check if the username and password exist in the database
$sql = "SELECT * FROM users WHERE username = ? AND password = ?";
$stmt = $connection->prepare($sql);

$stmt->bind_param("ss", $username, $password);
$stmt->execute();

$result = $stmt->get_result();

if ($result->num_rows > 0) {
  echo "results greater than 0";
  // Username and password are correct
  header("Location: videoPage.html");
  echo "success";
  exit(); // Make sure to exit after redirection  
  //echo "success";
}   
else {
      // Username and password are incorrect
      echo "failure";
}


$stmt->close();

// Close database connection
$connection->close();
?>

