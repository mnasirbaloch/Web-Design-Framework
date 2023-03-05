<!DOCTYPE html>
<html>
<head>
  <title>Fetch Data Form</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }
    h1 {
      text-align: center;
    }
    table {
      margin: 0 auto;
      text-align: left;
      border: solid black 1px;
    }

    th, td {
      text-align: left;
      padding: 10px;
      border: solid black 1px;
    }

    form {
      margin: 20px auto;
      width: 50%;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }

    label {
      display: block;
      margin-bottom: 10px;
      font-weight: bold;
    }

    input[type="text"] {
      padding: 10px;
      border-radius: 5px;
      border: 1px solid #ccc;
      width: 100%;
      box-sizing: border-box;
      margin-bottom: 20px;
      font-size: 16px;
    }
    input[type="submit"] {
      padding: 10px 20px;
      border-radius: 5px;
      border: none;
      display: block;
      margin:  0 auto;
      background-color: #4CAF50;
      color: #fff;
      font-size: 16px;
      cursor: pointer;
    }
    input[type="submit"]:hover {
      background-color: #3e8e41;
    }
  </style>
</head>
<body>
  <h1>Fetch Data From Database</h1>
  <form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>">
    <label for="id">Enter ID:</label>
    <input type="text" id="id" name="id">
    <input type="submit" name="submit" value="Fetch Data">
  </form>
  
  <?php
    // Check if form is submitted
  if(isset($_POST['submit'])){
      // Create database connection
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "demo_customer";
    $table = "customers";
      // lets make a connection with our databse
    $conn = new mysqli($servername, $username, $password, $dbname);

      // Check connection
    if ($conn->connect_error) {
        // if connection failed show the message and die same as exit will show the message
        // and exit from current script.
      echo "<center>Connection : Disabled</center>";
      die("Connection failed: " . $conn->connect_error);
    }else{
      echo "<center>Connection : Available</center>";
    }
      // create a query to retrieve data 
      // Prepare SQL query
    $sql = "SELECT * FROM $table WHERE customerid = ?";
      // using try catch to catch any exception occured by prepare() function
    try{
      $stmt = $conn->prepare($sql);
    } catch (Exception $e) {
      echo 'Caught exception: ',  $e->getMessage(), "\n";
    }

   // get values passed in form
    $id = $_POST['id'];

  // bind that value with our request
    $stmt->bind_param("i", $id);

  // execute the prepared query / command.
    $stmt->execute();
    $stmt->store_result();
    // bind result with variables;
    $stmt->bind_result($customerid, $companyname, $contactname,$address,$city,$postalcode,$country);

    // fetch result and check if non-empty show the result in table.
    if($stmt->fetch()){
        // Display result
     echo "<table>";
     echo " <tr><th  style = 'text-align:center;' colspan='2'>Record</th></tr>";
     echo "<tr>";
     echo "<th>CustomerID</th>";
     echo "<td>" . $customerid . "</td>";
     echo "</tr>";
     echo "<tr>";
     echo "<th>CompanyName</th>";
     echo "<td>" . $companyname . "</td>";
     echo "</tr>";
     echo "<tr>";
     echo "<th>ContactName</th>";
     echo "<td>" . $contactname . "</td>";
     echo "</tr>";
     echo "<tr>";
     echo "<th>Address</th>";
     echo "<td>" . $address . "</td>";
     echo "</tr>";
     echo "<tr>";
     echo "<th>City</th>";
     echo "<td>" . $city . "</td>";
     echo "</tr>";
     echo "<tr>";
     echo "<th>PostalCode</th>";
     echo "<td>" . $postalcode . "</td>";
     echo "</tr>";
     echo "<tr>";
     echo "<th>Country</th>";
     echo "<td>" . $country . "</td>";
     echo "</tr>";
     echo "</table>";
   } else {
        // No data found
    echo "<center><p>No data found for ID " . $id . "</p></center>";
  }

      // Close statement and connection
  $stmt->close();
  $conn->close();
}else{
  echo "<center>Please enter id to fetch data </center>";
}
?>
</body>
</html>
