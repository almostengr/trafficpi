<html>
<head>
<title>Traffic Control</title>
<style type="text/css">
body{
	font-family: Arial;
	font-size: 10pt;
}

p#error {
	background-color: #c00;
	color: #fff;
	padding: 5px;
}

p#success {
	background-color: #0c0;
	color: #000;
	padding: 5px;
}
</style>
</head>
<body>

<h1>Traffic Control</h1>

<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        $action = $_POST['program'];
	$filepath = "/tmp/traffic.txt";

	$file = file_put_contents($filepath, $action);
	if ($file === FALSE) {
		// throw new Exception("Error when attempting to open file");
		echo "<p id='error'>Error when attempting to open file.</p>";
	}
	else{ 
		echo "<p id='success'>Running $action</p>";
	}
}
?>

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

