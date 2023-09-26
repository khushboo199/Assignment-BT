from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import pytest

BASE_URL = "https://www.saucedemo.com/"

@pytest.fixture
def driver():
    # Initialize WebDriver (Chrome)
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_item_to_cart(driver):
    driver.get(BASE_URL)
    driver.maximize_window()

    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys("standard_user")
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys("secret_sauce")

    # Click the login button
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    wait = WebDriverWait(driver,10)

    cart = driver.find_element(By.XPATH,"//button[@class='btn btn_primary btn_small btn_inventory']")
    cart.click()
    cart1 = driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket").click()
    cart2 = driver.find_element(By.ID,"add-to-cart-sauce-labs-onesie").click()
    time.sleep(2)


    items_cart =  driver.find_element(By.XPATH,'//a[@class="shopping_cart_link"]').click()
    time.sleep(3)

    cart_list = driver.find_elements(By.XPATH, '//div[@class="cart_list"]')
    for item in cart_list:
        item_name = item.find_element(By.CLASS_NAME, 'inventory_item_name').text
        print(f"Item in Cart: {item_name}")



    #logout
    wait = WebDriverWait(driver, 10)
    burger_menu = wait.until(ec.element_to_be_clickable((By.ID, 'react-burger-menu-btn')))
    burger_menu.click()

    logout_link = wait.until(ec.element_to_be_clickable((By.ID, 'logout_sidebar_link')))
    logout_link.click()
    time.sleep(2)

    #Again Login and checking the cart times
    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys("standard_user")
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    items_cart = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
    time.sleep(3)

def test_place_order(driver):
    driver.get(BASE_URL)
    driver.maximize_window()

    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys("standard_user")
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys("secret_sauce")

    # Click the login button
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    wait = WebDriverWait(driver, 10)
    c1 = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    c1.click()
    c2 = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    items_cart = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
    time.sleep(3)

    checkout= driver.find_element(By.ID,"checkout").click()
    time.sleep(3)

    #information page
    first_name =  driver.find_element(By.ID,"first-name").send_keys("ravi")
    last_name = driver.find_element(By.ID,"last-name").send_keys("teja")
    postal_code = driver.find_element(By.ID,"postal-code").send_keys(560063)
    time.sleep(3)

    overview_page = driver.find_element(By.ID, "continue").click()
    total_price = driver.find_element(By.XPATH,'//div[@class="summary_info_label summary_total_label"]').text
    print(total_price)
    #driver.execute_script("arguments[0].scrollIntoView();", overview_page)
    time.sleep(2)

    finish = driver.find_element(By.ID,"finish").click()
    back_home = driver.find_element(By.ID,"back-to-products").click()
    time.sleep(3)












