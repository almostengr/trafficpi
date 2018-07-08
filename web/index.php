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
	$pseudofilepath = "/tmp/traffic_pseudo.txt";

	// update the file with program to run
	$file = file_put_contents($filepath, $action);
	if ($file === FALSE) {
		// throw error if not able to write to the file
		echo "<p id='error'>Error when attempting to open file.</p>";
	}
	else{
	       	// show success message if able to write to the file	
		echo "<p id='success'>Submitted $action</p>";
	} // end if else

	if ($action == "pseudocode") {
		$file2 = file_put_contents($pseudofilepath, $_POST['pseudocode']);
		if ($file2 === FALSE) {
			echo "<p id='error'>Error when attempting to open file.</p>";
		}			
	} // end if else
}
?>

<form method="post" action="index.php">
<p>
<strong>Select Program</strong><br />
<select name="program">
	<optgroup label="Run Signals">
		<option value="ustraffic" <?php if ($action=="ustraffic") echo 'selected="selected"'; ?>>US Traffic</option>
		<option value="uktraffic" <?php if ($action=="uktraffic") echo 'selected="selected"'; ?>>UK Traffic</option>
		<option value="russiatraffic" <?php if ($action=="russiatraffic") echo 'selected="selected"'; ?>>Russia Traffic</option>
	</optgroup>
	<optgroup label="Steady On/Off">
		<option value="all_on" <?php if ($action=="all_on") echo 'selected="selected"'; ?>>All On</option>
		<option value="redon" <?php if ($action=="redon") echo 'selected="selected"'; ?>>Red On</option>
		<option value="yellowon" <?php if ($action=="yellowon") echo 'selected="selected"'; ?>>Yellow On</option>
		<option value="greenon" <?php if ($action=="greenon") echo 'selected="selected"'; ?>>Green On</option>
		<option value="all_off" <?php if ($action=="all_off") echo 'selected="selected"'; ?>>All Off</option>
	</optgroup>
	<optgroup label="Games">
		<option value="redlightgreenlight" <?php if ($action=="redlightgreenlight") echo 'selected="selected"'; ?>>Red Light Green Light</option>
		<option value="redlightgreenlight2" <?php if ($action=="redlightgreenlight2") echo 'selected="selected"'; ?>>Red Light Green Light, with Yellow</option>
	</optgroup>
	<optgroup label="Flashers">
		<option value="flashred" <?php if ($action=="flashred") echo 'selected="selected"'; ?>>Flash Red</option>
		<option value="flashyel" <?php if ($action=="flashyel") echo 'selected="selected"'; ?>>Flash Yellow</option>
		<option value="flashgrn" <?php if ($action=="flashgrn") echo 'selected="selected"'; ?>>Flash Green</option>
		<option value="partymode4" <?php if ($action=="partymode4") echo 'selected="selected"'; ?>>Party Mode, Slow</option>
		<option value="partymode" <?php if ($action=="partymode") echo 'selected="selected"'; ?>>Party Mode</option>
		<option value="partymode2" <?php if ($action=="partymode2") echo 'selected="selected"'; ?>>Party Mode, Fast</option>
		<option value="partymode3" <?php if ($action=="partymode3") echo 'selected="selected"'; ?>>Party Mode, Faster</option>
	</optgroup>
	<optgroup label="Other">
		<option value="pseudocode" <?php if ($action=="pseudocode") echo 'selected="selected"'; ?>>Pseudocode</option>
	</optgroup>
	<optgroup label="Raspberry Pi Options">
		<option value="restart" <?php if ($action=="restart") echo 'selected="selected"'; ?>>Restart</option>
		<option value="shutdown" <?php if ($action=="shutdown") echo 'selected="selected"'; ?>>Shut Down</option>
	</optgroup>
</select>
</p>

<p>
<strong>Pseudocode</strong><br />
<textarea name="pseudocode" cols="50" rows="4">
<?php $action == "pseudocode" ? print $_POST["pseudocode"] : false; ?>
</textarea>
</p>

<p><input type="submit" name="submit" value="Submit" /></p>
</form>

<p style="text-align: center;">
Copyright &copy; 2017-<?php echo date("Y"); ?> @almostengr | 
<a href="index.php">Home</a> | 
<a href="https://github.com/bitsecondal/raspitraffic-stem" target="_blank">GitHub Repo</a>
</p>

</body>
</html>

