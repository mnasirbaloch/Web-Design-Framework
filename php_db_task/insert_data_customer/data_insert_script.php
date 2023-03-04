<?php

// variables which contains the name of each column in database table #customers
$servername = "localhost";
$username = "root";
$password = "";
$database = "demo_customer";
$table_name = "customers";
$col_id = "customerid";
$col_compname = "companyname";
$col_contactname="contactname";
$col_address="address";
$col_city = "city";
$col_pcode="postalcode";
$col_country="country";

// lets establish a connection with database
$conn = new mysqli($servername, $username, $password,$database);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
// echo "Connected successfully";

// a command which will be used to insert data in databse
$insertCommand = "INSERT INTO $table_name ($col_id,$col_compname,$col_contactname,$col_address,$col_city,$col_pcode,$col_country) VALUES (?,?,?,?,?,?,?)";

// check if request method is post if yes lets insert data into databse
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
// acces all values and store in variables passed via form 
  $customer_id = $_POST['customer_id'];
  $company_name = $_POST['company_name'];
  $contact_name = $_POST['contact_name'];
  $address = $_POST['address'];
  $city = $_POST['city'];
  $postalcode = $_POST['postalcode'];
  $country = $_POST['country'];

  // prepare our insert commands
 $sqlcmd = $conn->prepare($insertCommand);

 // bind parameters with our command
  $sqlcmd->bind_param("sssssss",$customer_id,$company_name,$contact_name,$address,$city,$postalcode,$country);

// lets execute command using try-catch so that if error occured will be visible to user via echo
  try {
  $result=$sqlcmd->execute();
  echo "<br>";
  echo '<h1>Congratulation Data Inserted Successfully</h1>';
  echo 'customer-id: '.$customer_id . "<br>";
  echo 'company-name: '.$company_name. "<br>";
  echo 'contact-name: '.$contact_name. "<br>";
  echo 'address: '.$address. "<br>";
  echo 'city: '.$city. "<br>";
  echo 'postalcode: '.$postalcode. "<br>";
  echo 'country: '.$country. "<br>";
  echo "<br>";
  echo '<button onclick="window.history.back()">Go Back</button>';
} catch (mysqli_sql_exception $e) {
  echo "Error: " . $e->getMessage();
}
}
?>

