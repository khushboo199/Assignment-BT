import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the URL of the Saucedemo website
BASE_URL = "https://www.saucedemo.com/"

# Test data: valid usernames and passwords for multiple users
USERS = [
    {"username": "standard_user", "password": "secret_sauce"},
    {"username": "performance_glitch_user", "password": "secret_sauce"},
    {"username": "locked_out_user","password": "secret_sauce"}
    # Add more users as needed
]

@pytest.fixture
def driver():
    # Initialize WebDriver (Chrome)
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize("user_data", USERS)
def test_successful_login_and_logout(driver, user_data):

    driver.get(BASE_URL)


    #driver.find_element(By.ID, "user-name").send_keys(user_data["username"])
    driver.find_element(By.ID,'user-name').send_keys(user_data["username"])
    #driver.find_element(By.ID, 'password').send_keys(user_data["password"])
    driver.find_element(By.ID,'password').send_keys(user_data["password"])

    # Click the login button
    #driver.find_element(By.ID, 'login-button').click()
    driver.find_element(By.ID,'login-button').click()

    wait = WebDriverWait(driver, 10)
    burger_menu = wait.until(EC.element_to_be_clickable((By.ID, 'react-burger-menu-btn')))
    burger_menu.click()


    assert "inventory" in driver.current_url


    logout_link = wait.until(EC.element_to_be_clickable((By.ID, 'logout_sidebar_link')))
    logout_link.click()


    assert BASE_URL in driver.current_url

