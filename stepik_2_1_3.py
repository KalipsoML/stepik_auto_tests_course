from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math



link = "https://suninjuly.github.io/math.html"
browser = None

try:
    browser = webdriver.Chrome()
    browser.get(link)

    people_radio = browser.find_element(By.ID, "peopleRule")
    people_radio_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_radio_checked)
    assert people_radio_checked is not None, "People radio is not selected by default"

    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None



finally:

    time.sleep(5)
    browser.quit()
