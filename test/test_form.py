import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestHTMLForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up Chrome WebDriver
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://localhost:5000/signup")  # Change to your local server URL if needed

    def test_form_elements_presence(self):
        # Check if all form fields are present
        self.assertTrue(self.driver.find_element(By.NAME, "username"))
        self.assertTrue(self.driver.find_element(By.NAME, "email"))
        self.assertTrue(self.driver.find_element(By.NAME, "password"))
        self.assertTrue(self.driver.find_element(By.NAME, "confirm"))
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']"))

    def test_submit_empty_form(self):
        # Submit the form without entering any details
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        
        # Check for validation error messages (adapt selectors as necessary)
        username_error = self.driver.find_element(By.ID, "username-error")
        email_error = self.driver.find_element(By.ID, "email-error")
        
        self.assertIsNotNone(username_error)
        self.assertIsNotNone(email_error)

    def test_show_password_toggle(self):
        # Test if the show-password toggle changes the password field type
        password_field = self.driver.find_element(By.NAME, "password")
        show_password_checkbox = self.driver.find_element(By.ID, "show-password-checkbox")
        
        password_field.send_keys("test_password")
        show_password_checkbox.click()  # Toggle on

        # Check if password field type changes to 'text'
        self.assertEqual(password_field.get_attribute("type"), "text")
        show_password_checkbox.click()  # Toggle off
        self.assertEqual(password_field.get_attribute("type"), "password")

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
