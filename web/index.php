<html>
<head>
<title>Traffic Control</title>
</head>
<body>

<p>
<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        $action = $_POST['program'];
	$filepath = "/tmp/traffic.txt";

	$file = file_put_contents($filepath, $action);
	if ($file === FALSE) {
		// throw new Exception("Error when attempting to open file");
		echo "<p style='background-color: #c00; padding: 5px;'>Error when attempting to open file.</p>";
	}
	else{ 
		echo "<p style='background-color: #0c0; margin: 5px; padding: 5px;'>Running $action</p>";
	}
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

