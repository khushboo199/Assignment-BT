import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

# Define the URL of the Saucedemo website
BASE_URL = "https://www.saucedemo.com/"

@pytest.fixture
def driver():

    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_default_sort_order(driver):

    driver.get(BASE_URL)
    driver.maximize_window()

    # Find and fill the username and password fields
    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys("standard_user")
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys("secret_sauce")

    # Click the login button
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    # Wait for the inventory container to load
    wait = WebDriverWait(driver, 10)
    inventory_container = wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="header_container"]/div[2]/div/span/select')))

    # Verify the items are in default sort order (e.g., alphabetical order)
    inventory_container.click()
    time.sleep(5)


    #item_elements = inventory_container.find_elements(By.CLASS_NAME,'inventory_item_name')
    item_elements = driver.find_elements(By.CLASS_NAME,'inventory_item_name')
    item_names = [item.text for item in item_elements]
    print(item_names)

    # Check if the item names are sorted in ascending order
    assert item_names == sorted(item_names)


def test_sort_price_high_to_low(driver):
    # Log in with a user
    driver.get(BASE_URL)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    # Find and fill the username and password fields
    username_field = wait.until(ec.element_to_be_clickable((By.ID, 'user-name')))
    username_field.send_keys("standard_user")

    password_field = wait.until(ec.element_to_be_clickable((By.ID, 'password')))
    password_field.send_keys("secret_sauce")

    # Click the login button
    login_button = wait.until(ec.element_to_be_clickable((By.ID, 'login-button')))
    login_button.click()

    # Wait for the sorting dropdown to load
    inventory_container = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')))

    # Select the "Price (high to low)" option
    option = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'option[value="hilo"]')))
    option.click()
    time.sleep(5)

    # Verify that the items are sorted by price high to low
    item_prices = driver.find_elements(By.CSS_SELECTOR, '.inventory_item_price')
    item_prices_text = [price.text for price in item_prices]

    # Convert the item prices to integers for comparison
    item_prices_float = [float(price.strip('$')) for price in item_prices_text]
    print(item_prices_float)

    # Check if the item prices are sorted in descending order (high to low)
    assert item_prices_float == sorted(item_prices_float, reverse=True)










