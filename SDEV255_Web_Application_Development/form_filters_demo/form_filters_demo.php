<?php
// Point to your own functions.php file
// If you don't have this you'll have to replace the debug function with var_dump()
include '..' . DIRECTORY_SEPARATOR . 'includes' . DIRECTORY_SEPARATOR . 'functions.php';

$raw_form = [
    'name' => '',
    'email' => '',
    'age' => '',
    'website' => '',
    'birthdate' => '',
    'gender' => '',
    'subscribe' => '',
    'interests' => '',
];

$errors = $raw_form;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    if (!isset($_POST['gender'])) {
        $_POST['gender'] = '';
    }
    if (!isset($_POST['subscribe'])) {
        $_POST['subscribe'] = '';
    }

    $raw_form = [
        'name' => $_POST['name'],
        'email' => $_POST['email'],
        'age' => $_POST['age'],
        'website' => $_POST['website'],
        'birthdate' => $_POST['birthdate'],
        'gender' => $_POST['gender'],
        'subscribe' => $_POST['subscribe'],
        'interests' => $_POST['interests'],
    ];

    // Make an array of validation filters
    $validation_filters['name']['filter'] = FILTER_VALIDATE_REGEXP;
    $validation_filters['name']['options']['regexp'] = '/^[a-zA-Z]+$/';
    $validation_filters['email']['filter'] = FILTER_VALIDATE_EMAIL;
    $validation_filters['age']['filter'] = FILTER_VALIDATE_INT;
    $validation_filters['age']['options']['min_range'] = 0;
    $validation_filters['age']['options']['max_range'] = 99;
    $validation_filters['website']['filter'] = FILTER_VALIDATE_URL;
    $validation_filters['birthdate']['filter'] = FILTER_VALIDATE_REGEXP;
    $validation_filters['birthdate']['options']['regexp'] = '/^\d{4}-\d{2}-\d{2}$/';
    $validation_filters['subscribe']['filter'] = FILTER_VALIDATE_BOOLEAN;

    // Do the validation
    $filtered_form = filter_input_array(INPUT_POST, $validation_filters);

    // Add custom check for gender and interests
    $gender_options = ['male', 'female'];
    $filtered_form['gender'] = in_array($_POST['gender'], $gender_options);
    $interest_options = ['coding', 'reading', 'gaming'];
    $filtered_form['interests'] = in_array($_POST['interests'], $interest_options);

    // DEBUG - comment if live
    pretty_dump($filtered_form, 'FILTERED OUTPUT');

    $errors['name'] = $filtered_form['name'] ? '' : 'FAIL';
    $errors['email'] = $filtered_form['email'] ? '' : 'FAIL';
    $errors['age'] = $filtered_form['age'] ? '' : 'FAIL';
    $errors['website'] = $filtered_form['website'] ? '' : 'FAIL';
    $errors['birthdate'] = $filtered_form['birthdate'] ? '' : 'FAIL';
    $errors['gender'] = $filtered_form['gender'] ? '' : 'FAIL';
    $errors['subscribe'] = $filtered_form['subscribe'] ? '' : 'FAIL';
    $errors['interests'] = $filtered_form['interests'] ? '' : 'FAIL';

    // DEBUG - comment if live
    pretty_dump($errors, 'ERRORS');
}

// DEBUG - comment if live
pretty_dump($raw_form, 'RAW FORM');
?>
<style>
    span {
        margin-left: 10px;
        color: red;
        font: bold 1rem sans-serif;
    }
</style>
<form method="post">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" value="<?= htmlspecialchars($raw_form['name']) ?>">
    <span><?= $errors['name'] ?></span>
    <br>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" value="<?= htmlspecialchars($raw_form['email']) ?>">
    <span><?= $errors['email'] ?></span>
    <br>

    <label for="age">Age:</label>
    <input type="number" id="age" name="age" value="<?= htmlspecialchars($raw_form['age']) ?>">
    <span><?= $errors['age'] ?></span>
    <br>

    <label for="website">Website:</label>
    <input type="url" id="website" name="website" value="<?= htmlspecialchars($raw_form['website']) ?>">
    <span><?= $errors['website'] ?></span>
    <br>

    <label for="birthdate">Birthdate (YYYY-MM-DD):</label>
    <input type="text" id="birthdate" name="birthdate" value="<?= htmlspecialchars($raw_form['birthdate']) ?>">
    <span><?= $errors['birthdate'] ?></span>
    <br>

    <label>Gender:</label>
    <input type="radio" id="male" name="gender" value="male" <?= $raw_form['gender'] === 'male' ? 'checked' : '' ?>> <label for="male">Male</label>
    <input type="radio" id="female" name="gender" value="female" <?= $raw_form['gender'] === 'female' ? 'checked' : '' ?>> <label for="female">Female</label>
    <span><?= $errors['gender'] ?></span>
    <br>

    <label>Subscribe to newsletter:</label>
    <input type="checkbox" id="subscribe" name="subscribe" value="true" <?= $raw_form['subscribe'] === 'true' ? 'checked' : '' ?>> <label for="subscribe">Subscribe</label>
    <span><?= $errors['subscribe'] ?></span>
    <br>

    <label for="interests">Interests:</label>
    <select id="interests" name="interests">
        <option value="coding" <?= $raw_form['interests'] === 'coding' ? 'selected' : '' ?>>Coding</option>
        <option value="reading" <?= $raw_form['interests'] === 'reading' ? 'selected' : '' ?>>Reading</option>
        <option value="gaming" <?= $raw_form['interests'] === 'gaming' ? 'selected' : '' ?>>Gaming</option>
    </select>
    <span><?= $errors['interests'] ?></span>
    <br>

    <input type="submit" value="Submit">
</form>