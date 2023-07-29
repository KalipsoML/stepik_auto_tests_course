import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Tests(unittest.TestCase):
    browser = None

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_Registration_1(self):
        browser = self.browser
        browser.get("http://suninjuly.github.io/registration1.html")

        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        input3.send_keys("test@test.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 'Registration failed')

    def test_Registration_2(self):
        browser = self.browser
        browser.get("http://suninjuly.github.io/registration2.html")

        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        input3.send_keys("test@test.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 'Registration failed')

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
