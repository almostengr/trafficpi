<html>
<head>
<title>Traffic Control</title>
</head>
<body>

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
<p><input type="submit" name="us" value="US Traffic" /></p>
<p><input type="submit" name="uk" value="UK Traffic" /></p>
<p><input type="submit" name="allon" value="All On" /></p>
<p><input type="submit" name="alloff" value="All Off" /></p>
<p><input type="submit" name="flashred" value="Flash Red" /></p>
<p><input type="submit" name="flashyel" value="Flash Yellow" /></p>
<p><input type="submit" name="flashgrn" value="Flash Green" /></p>
<p>&nbsp;</p>
<p><input type="submit" name="shutdown" value="Shut Down" /></p>
</form>

</body>
</html>

