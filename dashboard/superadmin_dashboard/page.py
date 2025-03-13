from selenium.common import TimeoutException
from helpers.base_page import *
import login.locators as loc
import landing_page.locators as landing_page
import dashboard.locators as dashboard
import dashboard.superadmin_dashboard.locators as ds_locator


class DashboardSuperAdmin(CommonClass):
    bp = Base()


    def click_login_lp(self):  # move this function to landing page later
        self.click_element('CSS_SELECTOR', landing_page.login_css)


    def click_new_event(self):
        self.click_element('XPATH', ds_locator.new_event_xpath)

    def enter_title(self, text):
        self.send_keys_to_element('CSS', ds_locator.title_css, text)

    def select_date(self, text):
        self.send_keys_to_element('ID', ds_locator.event_start_date_id, text)

    def check_for_all_day(self):
        self.click_element('CSS', ds)
