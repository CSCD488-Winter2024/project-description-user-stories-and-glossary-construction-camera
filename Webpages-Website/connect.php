<?php
// Database connection parameters
$host = "localhost"; // Change this if your database is hosted elsewhere
$username = "test";
$password = "test123";
$database = "employees";

// Connect to the database
$connection = new mysqli($host, $username, $password, $database);

// Check for connection errors
if ($connection->connect_error) {
    die("Connection failed: " . $connection->connect_error);
}

// Get username and password from the AJAX request
$username = $_POST['username'];
$password = $_POST['password'];

// SQL query to check if the username and password exist in the database
$sql = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
$result = $connection->query($sql);

echo "sql: " . $sql;

if($result === false){
  echo "Query error: " . $connection->error;
}
else{
  if ($result->num_rows > 0) {
    // Username and password are correct
    header("Location: videoPage.html");
    exit(); // Make sure to exit after redirection  
    //echo "success";
  }   
  else {
      // Username and password are incorrect
      echo "failure";
  }
}

// Check if there is a matching user


// Close database connection
$connection->close();
?>

