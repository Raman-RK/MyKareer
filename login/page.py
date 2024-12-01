import allure
from selenium.webdriver import ActionChains
# import pandas as pd
from helpers.base_page import *
import login.locators as loc
import landing_page.locators as landing_page
import dashboard.locators as dashboard


class Login(CommonClass):
    bp = Base()

    def click_login_lp(self):  # move this function to landing page later
        self.click_element('CSS_SELECTOR', landing_page.login_css)

    def send_email(self, text):
        self.send_keys_to_element('NAME', loc.email_name, text)

    def send_password(self, text):
        self.send_keys_to_element('CSS_SELECTOR', loc.password_css, text)

    def click_login(self):
        self.click_element("XPATH", loc.login_xpath)

    def click_profile_pic(self):  # will write in dashboard page
        self.click_element("CSS_SELECTOR", dashboard.profile_pic_css)

    def close_success_toast(self, driver):
        try:
            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, dashboard.login_toast_class))
            )
            self.click_element("CLASS_NAME", dashboard.login_toast_class)
            print("Element is visible")
        except:
            print("Element is not visible")

    def click_logout(self):  # will write in dashboard page
        self.click_element("XPATH", dashboard.logout_xpath)
