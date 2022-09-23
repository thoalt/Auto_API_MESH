'''
    This module contain all variable and method for each page
'''
import time

from base.WEBLib import Web_Lib

class LoginPage(Web_Lib):
    # Get all locator
    txt_user_xpath = "//input[@id='LOGIN_USER']"
    txt_password_xpath = "//input[@id='LOGIN_PWD']"
    btn_login_xpath = "//input[@id='BTN_Login']"
    lnk_logout_xpath = "//a[contains(text(),'Logout')]"

    # Init method
    def __init__(self, driver):
        super().__init__(driver)

    # Action Method
    def set_username(self, username):
        self.wait_and_set_text_element_without_enter(self.txt_user_xpath, username)

    def set_password(self, password):
        self.wait_and_set_text_element_without_enter(self.txt_password_xpath, password)

    def click_login(self):
        self.wait_and_click_element(self.btn_login_xpath)

    def click_logout(self):
        self.wait_and_click_element(self.lnk_logout_xpath)

    def log_in_to_webgui(self, username=None, password=None):
        if username is not None:
            self.set_username(username)

        if password is not None:
            self.set_password(password)

        self.click_login()
        time.sleep(1)