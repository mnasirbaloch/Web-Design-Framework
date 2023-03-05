<?php
$servername = "localhost";
$username = "root";
$password = "";
$database = "employee";

// Create connection
$conn = new mysqli($servername, $username, $password,$database);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
// // create a command and store it in variable
// $command = "CREATE DATABASE employee";

// // execute command and save result in variable
// $result = $conn->query($command);
// // lets check if command executed successfully or not
// if($result){
//   mysqli_query($conn,$command);
//   echo "Database created successfully";
// }else{
//   echo "Error Occured while creating DB";
// }


// create a table

$createTableCommand = "Create TABLE customers(id int AUTO_INCREMENT PRIMARY KEY,name varchar(50) NOT NULL,cname varchar(50) NOT NULL, address varchar(150) NOT NULL,city varchar(50) NOT NULL, postalcode varchar(50) NOT NULL, country varchar (20) NOT NULL);";

// lets run teh above command and store result in variable
$result = mysqli_query($conn,$createTableCommand);
if($conn){
  echo "<br>Table created successfully";
}else{
  echo "Table creation failed";
}
?>

