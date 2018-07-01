<html>
<head>
<title>Traffic Control</title>
</head>
<body>
<ul>
<?php

<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        $action = "";
        if (isset($_POST['us'])) {
                $action = "us";
        }
        else if (isset($_POST['uk'])) {
                $action = "uk";
        }
        else if (isset($_POST['allon'])) {
                $action = "allon";
        }
        else if (isset($_POST['alloff'])) {
                $action = "alloff";
        }
        else if (isset($_POST['flashred'])) {
                $action = "flashred";
        }
        else if (isset($_POST['flashyel'])) {
                $action = "flashyel";
        }
        else if (isset($_POST['flashgrn'])) {
                $action = "flashgrn";
        }
        else if (isset($_POST['shutdown'])) {
                $action = "shutdown";
        }
	echo "<p style='background-color: #0c0; margin: 5px; padding: 5px;'>Running $action</p>";
	try {
		// write the action to the file
        	$file = fopen('/tmp/traffic.txt', 'w') or die("Can't open file");
	        fwrite($file, $action) or die("Write failed");
        	fclose($file);
	} catch (Exception $e) {
		echo "<p style='background-color: #c00; padding: 5px;'>$e->getMessage()</p>";
	}
}
?>

<form method="post" action="index.php">
<select name="program">
	<option value="us">US Traffic</option>
	<option value="uk">UK Traffic</option>
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

