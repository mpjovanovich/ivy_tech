<?php

// Include the configuration file to define constants
require_once '../config.php';

// Header HTML
include_once TEMPLATES_PATH . DIRECTORY_SEPARATOR . 'header.php';

?>

<h2>Home</h2>

<?php

// List our constants
echo "Application Name: " . APPLICATION_NAME . "<br>";
echo "Application Version: " . APPLICATION_VERSION . "<br>";
echo "Site Root: " . SITE_ROOT . "<br>";
echo "Application Path: " . APPLICATION_PATH . "<br>";
echo "Includes Path: " . INCLUDES_PATH . "<br>";
echo "Templates Path: " . TEMPLATES_PATH . "<br>";

// Footer HTML
include_once TEMPLATES_PATH . DIRECTORY_SEPARATOR . 'footer.php';
