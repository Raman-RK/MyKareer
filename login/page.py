import allure
from selenium.webdriver import ActionChains
import pandas as pd
from helpers.base_page import *
import login.locators as loc


class Login(CommonClass):
    bp = Base()

    def click_login(self):
        self
        return text

    def send_phone(self, text):
        self.send_keys_to_element('CSS_SELECTOR', lo.phone_text_box, "")
        self.send_keys_to_element('CSS_SELECTOR', lo.phone_text_box, text)