<!DOCTYPE html>
<html>
<head>
    <title>Customer Form</title>
    <style>
        form {
            width: 500px;
            margin: auto;
            padding: 20px;
            background-color: #f5f5f5;
            border-radius: 5px;
            box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.3);
        }
        label {
            display: block;
            margin-bottom: 10px;
            font-weight: bold;
        }
        input[type="text"] {
            width: 100%;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
            margin-bottom: 15px;
            font-size: 16px;
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            margin-top: 10px;
        }
        input[type="submit"]:hover {
            background-color: #3e8e41;
        }
    </style>
</head>
<body>

    <form method="post" action="data_insert_script.php">
        <label for="customer_id">Customer ID:</label>
        <input type="text" id="customer_id" name="customer_id" required>

        <label for="company_name">Company Name:</label>
        <input type="text" id="company_name" name="company_name" required>

        <label for="contact_name">Contact Name:</label>
        <input type="text" id="contact_name" name="contact_name" required>

        <label for="address">Address:</label>
        <input type="text" id="address" name="address" required>

        <label for="city">City:</label>
        <input type="text" id="city" name="city" required>

        <label for="postalcode">Postal Code:</label>
        <input type="text" id="postalcode" name="postalcode" required>

        <label for="country">Country:</label>
        <input type="text" id="country" name="country" required>

        <input type="submit" value="Submit">
    </form>
</body>
</html>
