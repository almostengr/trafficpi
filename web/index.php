<html>
<head>
<title>Traffic Control</title>
</head>
<body>

<p>
<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        $action = $_POST['program'];

	try {
		// write the action to the file
        	$file = fopen('/var/tmp/traffic.txt', 'w');

		if (!$file) {
			throw new Exception("Unable to open file");
		}
	        
		// fwrite($file, $action) or die("Write failed");
		$writeFile = fwrite($file, $action);

		if (!$writeFile) {
			throw new Exception("Unable to write to file");
			echo "write error";
		}

        	fclose($file);
	
		echo "<p style='background-color: #0c0; margin: 5px; padding: 5px;'>Running $action</p>";
	} catch (Exception $e) {
		echo "<p style='background-color: #c00; padding: 5px;'>$e->getMessage()</p>";
	}
}
else{
	$action = "None";
}
?>
</p>

<form method="post" action="index.php">
<select name="program">
	<option value="ustraffic">US Traffic</option>
	<option value="uktraffic">UK Traffic</option>
	<option value="allon">All On</option>
	<option value="alloff">All Off</option>
	<option value="flashred">Flash Red</option>
	<option value="flashyel">Flash Yellow</option>
	<option value="flashgrn">Flash Green</option>
	<option value="shutdown">Shut Down</option>
</select>
<p><input type="submit" name="Submit" /></p>
</form>

</body>
</html>

