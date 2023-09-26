from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class LoginPage:
    username_id = 'user-name'
    password_id = 'password'
    login_button_id = 'login-button'
    menus_id = "react-burger-menu-btn"
    home_page_xpath = '//div[@class="app_logo"]'
    logout_button_linktext = 'Logout'

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def userName(self,username):
        self.driver.find_element(By.ID,self.username_id).clear()
        self.wait.until(ec.visibility_of_element_located((By.ID,self.username_id))).send_keys(username)
        #self.driver.find_element(By.ID,self.username_id).send_keys(username)

    def passWord(self,password):
        self.driver.find_element(By.ID,self.password_id).clear()
        self.wait.until(ec.visibility_of_element_located((By.ID,self.password_id))).send_keys(password)
        #self.driver.find_element(By.ID,self.password_id).send_keys(password)

    def home_page(self,username):
        #self.wait.until(ec.visibility_of_element_located((By.XPATH,self.home_page)))
        self.driver.find_element(By.XPATH,self.home_page)


    def LoginButton(self,username):
        #self.driver.find_element(By.ID,self.login_button_id).click()
        self.wait.until(ec.element_to_be_clickable((By.ID,self.login_button_id))).click()


    def Menus(self):
        #self.driver.find_element(By.ID,self.menus_id).click()
        self.wait.until(ec.element_to_be_clickable((By.ID,self.menus_id))).click()

    def LogoutButton(self,username):
        #self.driver.find_element(By.LINK_TEXT,self.logout_button_linktext).click()
        self.wait.until(ec.element_to_be_clickable((By.ID,self.logout_button_linktext))).click()

    #def get_login_success_message(self):
    #    return "login successfully"

    #def get_error_message(self):
    #    return "invalid login credentials"