from selenium import webdriver

# Set up the Selenium webdriver
driver = (
    webdriver.Chrome()
)

# Navigate to the web page
driver.get("https://example.com")

# Capture the final rendered HTML
rendered_html = driver.page_source

# Capture the final rendered CSS (assuming you have a way to access it)
# You might use another library or method to retrieve the CSS

# Close the webdriver
driver.quit()

# Now, 'rendered_html' contains the final rendered HTML of the web page.
