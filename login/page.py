import allure
from selenium.webdriver import ActionChains
import pandas as pd
from helpers.base_page import *
import login.locators as loc
import landing_page.locators as lpl


class Login(CommonClass):
    bp = Base()

# move this function to landing page later
    def click_login_lp(self):
        self.click_element('ID', lpl.login_id)

    def send_email(self, text):
        self.send_keys_to_element('NAME', loc.email_name, text)

    def send_password(self, text):
        self.send_keys_to_element('CSS_SELECTOR', loc.password_css, text)

    def click_login(self):
        self.click_element("XPATH", loc.login_xpath)