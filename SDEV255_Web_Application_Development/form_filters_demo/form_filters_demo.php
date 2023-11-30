<?php
// Create an associative array to hold the filtered form data
// Initialize all fields to empty strings
$form = [
    'name' => '',
    'age' => '',
    'terms' => '',
];

// Make a copy of the form array to escape the values to display back to the form fields
$escaped_form = $form;

// Create an associative array to hold any error messages
$errors = $form;

// If the form was submitted...
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // When the checkbox is not checked, it doesn't send any value, so there's no 'terms' key in the $_POST array.
    // We can add it to the $_POST array and set it to false to make the filter_input_array() function work.
    if (!isset($_POST['terms'])) {
        $_POST['terms'] = false;
    }

    // Make an array of validation filters
    $validation_filters['name']['filter']              = FILTER_VALIDATE_REGEXP;
    $validation_filters['name']['options']['regexp']   = '/^[a-zA-Z]+$/';
    $validation_filters['age']['filter']               = FILTER_VALIDATE_INT;
    $validation_filters['age']['options']['min_range'] = 0;
    $validation_filters['age']['options']['max_range'] = 65;
    $validation_filters['terms']                       = FILTER_VALIDATE_BOOLEAN;


    // Get the filtered form data
    $filtered_form = filter_input_array(INPUT_POST, $validation_filters);

    // Get the filtered form data
    $form = filter_input_array(INPUT_POST, $validation_filters);

    // DEBUG - Uncomment to see the filtered form data
    // var_dump($form);

    // Name will be the entered string if validation passed, or false if validation failed
    $errors['name']  = $form['name']  ? '' : 'Name must only contain letters.';

    // Age will be the entered integer if validation passed, or false if validation failed
    // IMPORTANT NOTE: We cannot do this due to truthy/falsy values and the fact that 0 is a valid age:
    // $errors['terms'] = $form['terms'] ? '' : 'You must agree to the terms and conditions';
    // We have to use the triple-equals operator:
    $errors['age'] = $form['age'] !== false ? '' : 'Age must be a value 0-65';

    // terms will be true if validation passed
    $errors['terms'] = $form['terms'] ? '' : 'You must agree to the terms and conditions';

    // Create a filters array to sanitize the form data that will display back to the form fields.
    // The array_fill_keys() function creates an array using the keys of the first argument and the value of the second argument.
    $escape_filters = array_fill_keys(array_keys($_POST), FILTER_SANITIZE_FULL_SPECIAL_CHARS);
    $escaped_form = filter_input_array(INPUT_POST, $escape_filters);
}
?>

<!-- Present escaped form data for any values that originated from the user. -->
<!-- We don't need to escape the error messages because we know they are safe. -->
<form action="" method="POST">
    Name: <input type="text" name="name" value="<?= $escaped_form['name'] ?>">
    <span class="error"><?= $errors['name'] ?></span><br>
    Age: <input type="text" name="age" value="<?= $escaped_form['age'] ?>">
    <span class="error"><?= $errors['age'] ?></span><br>
    <input type="checkbox" name="terms" value="true" <?= $escaped_form['terms'] ? 'checked' : '' ?>> I agree to the terms and conditions
    <span class="error"><?= $errors['terms'] ?></span><br>
    <input type="submit" value="Save">
</form>