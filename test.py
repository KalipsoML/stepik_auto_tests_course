import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

#инициализируем файрфокс в проекте
# firefox = Service('./geckodriver.exe')
# driver = webdriver.Firefox(service=firefox)

#инициализируем хром в проекте
chrome = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=chrome)

driver.get('https://dev.valoaneducator.tv/login')
time.sleep(5)

textarea = driver.find_element(By.CLASS_NAME, "Input_input__M26nT")
textarea.send_keys("test")
time.sleep(5)