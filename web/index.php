<!DOCTYPE html>
<html>
<head>
<title>TrafficPi Control Panel</title>
<meta name="copyright" content="Kenny Robinson, @almostengr" />
<meta name="author" content="Kenny Robinson, @almostengr" />
<meta name="robots" content="noindex,nofollow" />
<meta name="language" content="English" />
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
	background-color: #82FA58;
	color: #000;
	padding: 5px;
}
</style>
</head>
<body>

<h1>TrafficPi Control Panel</h1>

<?php
// only peform these actions if the form has been submitted
if ($_SERVER['REQUEST_METHOD'] == 'POST') {

	// get the program to run from the from
	$action = $_POST['program'];
	$filepath = "/tmp/traffic.txt";

	// update the file with program to run
	$file = file_put_contents($filepath, $action);
	if ($file === FALSE) {
		// throw error if not able to write to the file
		echo "<p id='error'>Error when attempting to open file.</p>";
	}
	else{
	       	// show success message if able to write to the file	
		echo "<p id='success'>Submitted $action</p>";
	}
}
?>

<form method="post" action="index.php">
<p>
<select name="program">
	<optgroup label="Run Signals">
	<option value="ustraffic">US Traffic</option>
	<option value="uktraffic">UK Traffic</option>
	<option value="russiatraffic">Russia Traffic</option>
	</optgroup>
	<optgroup label="Steady On/Off">
	<option value="all_on">All On</option>
	<option value="redon">Red On</option>
	<option value="yellowon">Yellow On</option>
	<option value="greenon">Green On</option>
	<option value="all_off">All Off</option>
	</optgroup>
	<optgroup label="Games">
	<option value="redlightgreenlight">Red Light Green Light</option>
	<option value="redlightgreenlight2">Red Light Green Light, with Yellow</option>
	</optgroup>
	<optgroup label="Flashers">
	<option value="flashred">Flash Red</option>
	<option value="flashyel">Flash Yellow</option>
	<option value="flashgrn">Flash Green</option>
	<option value="partymode4">Party Mode, Slow</option>
	<option value="partymode">Party Mode</option>
	<option value="partymode2">Party Mode, Fast</option>
	<option value="partymode3">Party Mode, Faster</option>
	</optgroup>
	<optgroup label="Raspberry Pi Options">
	<option value="restart">Restart</option>
	<option value="shutdown">Shut Down</option>
	</optgroup>
</select>
</p>
<p><input type="submit" name="Submit" value="Submit" /></p>
</form>

<p style="text-align: center;">
Copyright &copy; 2017-<?php echo date("Y"); ?> @almostengr | 
<a href="index.php">Home</a> | 
<a href="https:////github.com/bitsecondal/raspitraffic-stem" target="_blank">GitHub Repo</a>
</p>

</body>
</html>

