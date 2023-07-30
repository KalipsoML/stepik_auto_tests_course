import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

# python -m pytest -s -v test_stepik_3_6_4.py


@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


def test_login(browser):
    link = "https://stepik.org/lesson/236895/step/1"
    browser.implicitly_wait(5)
    browser.get(link)

    login = browser.find_element(By.ID, 'ember33')
    login.click()

    login_email = browser.find_element(By.ID, 'id_login_email')
    login_email.send_keys("")
    login_pass = browser.find_element(By.ID, 'id_login_password')
    login_pass.send_keys("")

    login_button = browser.find_element(By.CLASS_NAME, "button_with-loader")
    login_button.click()

    WebDriverWait(browser, 12).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, 'ember-application.show-modal'))
    )


@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])  #
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.implicitly_wait(5)
    browser.get(link)

    answer = math.log(int(time.time()))
    answer_area = browser.find_element(By.CLASS_NAME, 'ember-text-area')
    answer_area.send_keys(answer)

    submit_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    submit_button.click()

    ember_view = WebDriverWait(browser, 12).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'smart-hints.ember-view'))
    )
    message = ember_view.text
    assert "Correct" in message, f"Text '{message}' is invalid"
