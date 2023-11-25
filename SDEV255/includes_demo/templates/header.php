<!-- header.php -->

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Includes Demo<?php echo isset($pageTitle) ? ': ' . $pageTitle : ''; ?></title>
</head>

<body>
    <nav>
        <ul>
            <li><a href="index.php">Home</a></li>
            <li><a href="other_page.php">Other Page</a></li>
        </ul>
    </nav>