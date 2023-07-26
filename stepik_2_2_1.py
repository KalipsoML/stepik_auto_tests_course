from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

link = "http://suninjuly.github.io/selects1.html"
browser = None

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    x1 = num1.text
    num2 = browser.find_element(By.ID, "num2")
    x2 = num2.text

    y = str(int(x1) + int(x2))

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(y)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:

    time.sleep(5)
    browser.quit()
