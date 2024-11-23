import time
import allure
import pytest
from login.page import Login
from utilities.read_properties import ReadConfig
from utilities.customlogger import LogGen
from helpers.conf_test import setup



class TestLogIn:
    @pytest.fixture(autouse=True)
    def var_setup(self, setup):
        self.driver = setup
        config_reader = ReadConfig()
        # Get configuration values
        self.baseURL = config_reader.get_application_url()