##############################################
## Setting up Selenium with WebDriver:
##############################################

from selenium import webdriver

# Initialize the WebDriver (e.g., Chrome, Firefox, Edge)
driver = webdriver.Chrome(executable_path="/path/to/chromedriver")

# Navigate to a web page
driver.get("https://example.com")

##############################################
## Locating Elements:
##############################################

from selenium.webdriver.common.by import By

# Find element by ID
element = driver.find_element(By.ID, "element_id")

# Find element by name attribute
element = driver.find_element(By.NAME, "element_name")

# Find element by CSS selector
element = driver.find_element(By.CSS_SELECTOR, "css_selector")

# Find element by XPath
element = driver.find_element(By.XPATH, "//xpath_expression")

##############################################
## Interacting with Elements:
##############################################

# Typing text into an input field
element.send_keys("Text to type")

# Clicking a button or link
element.click()

# Clearing an input field
element.clear()

##############################################
## Assertions and Assertions Library (e.g., unittest):
##############################################

import unittest


class MyTest(unittest.TestCase):
    def test_example(self):
        # Perform actions and retrieve results
        result = driver.find_element(By.ID, "result").text

        # Assert that a condition is True
        self.assertTrue(result == "Expected Result")

        # Assert that a condition is False
        self.assertFalse(result == "Unexpected Result")


##############################################
## Explicit Waits:
##############################################

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for an element to be clickable
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "element_id"))
)

##############################################
## Taking Screenshots:
##############################################

driver.save_screenshot("screenshot.png")

##############################################
## Handling Pop-Up Windows:
##############################################

# Switch to a new window
driver.switch_to.window(driver.window_handles[1])

# Close the current window
driver.close()

# Switch back to the main window
driver.switch_to.window(driver.window_handles[0])

##############################################
## Managing Cookies:
##############################################

# Get all cookies
cookies = driver.get_cookies()

# Add a new cookie
driver.add_cookie({"name": "cookie_name", "value": "cookie_value"})

# Delete a cookie by name
driver.delete_cookie("cookie_name")

# Delete all cookies
driver.delete_all_cookies()


###############################################################################################
## More unit tests:
###############################################################################################

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class MyTest(unittest.TestCase):
    def setUp(self):
        # Set up the WebDriver (Chrome in this example)
        self.driver = webdriver.Chrome(executable_path="/path/to/chromedriver")
        self.driver.get("https://example.com")

    def tearDown(self):
        # Close the WebDriver after each test
        self.driver.quit()

    def test_title(self):
        # Test if the page title is correct
        self.assertEqual(self.driver.title, "Example Domain")

    def test_element_visibility(self):
        # Test if a specific element is visible
        element = self.driver.find_element(By.ID, "example_element")
        self.assertTrue(element.is_displayed())

    def test_element_text(self):
        # Test if the text of an element matches the expected value
        element = self.driver.find_element(By.ID, "example_text")
        self.assertEqual(element.text, "Hello, World!")

    def test_input_field(self):
        # Test typing text into an input field and verifying its value
        input_field = self.driver.find_element(By.ID, "text_input")
        input_field.send_keys("Test Input")
        self.assertEqual(input_field.get_attribute("value"), "Test Input")

    def test_button_click(self):
        # Test clicking a button and verifying its effect
        button = self.driver.find_element(By.ID, "example_button")
        button.click()
        result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result, "Button Clicked!")


if __name__ == "__main__":
    unittest.main()
