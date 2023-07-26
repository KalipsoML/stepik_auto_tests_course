from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


link = "http://suninjuly.github.io/file_input.html"

browser = None

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Ivan")
    first_name = browser.find_element(By.NAME, "lastname")
    first_name.send_keys("Ivanov")
    first_name = browser.find_element(By.NAME, "email")
    first_name.send_keys("Ivan@test.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:

    time.sleep(5)
    browser.quit()
