<html>
<head>
<title>Traffic Control</title>
</head>
<body>
<ul>
<?php

$scripts = scandir('/home/pi/raspitraffic-stem/*py');

foreach ($scripts as $script) {
	echo '<li>$script</li>';
}

?>

</body>
</html>

