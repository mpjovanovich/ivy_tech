<?php

// Include the configuration file to define constants
require_once '../config.php';

// Define the page title before including the header - then it will 
// be available to the header template as local variable $pageTitle
$pageTitle = 'Other';
include_once TEMPLATES_PATH . DIRECTORY_SEPARATOR . 'header.php';

?>

<h2>Other Page</h2>

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
