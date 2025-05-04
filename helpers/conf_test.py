import pytest
import allure
from selenium import webdriver
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from helpers.environment_writer import write_allure_environment
from utilities.read_credentials import CredentialManager
from utilities.read_properties import ConfigManager
from login.page import Login  # Make sure this import exists and is correct


# -------- WebDriver Setup Fixture --------
@pytest.fixture(scope="function")
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def setup(request):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    is_ci = os.getenv("GITHUB_ACTIONS") == "true"

    if is_ci:
        # Use pre-installed ChromeDriver on GitHub Actions
        service = Service("/usr/bin/chromedriver")
    else:
        # Use WebDriver Manager locally
        from webdriver_manager.chrome import ChromeDriverManager
        driver_path = ChromeDriverManager().install()
        service = Service(driver_path)

    driver = webdriver.Chrome(service=service, options=chrome_options)
    request.cls.driver = driver
    yield driver
    driver.quit()


# -------- Login Fixture --------
@pytest.fixture
def setup_login(setup, request):
    role = request.param
    credentials_manager = CredentialManager()
    config = ConfigManager()
    base_url = config.get_base_url()

    email = credentials_manager.get_email(role)
    password = credentials_manager.get_password(role)

    if not email or not password:
        pytest.fail(f"Missing credentials for role: {role}")

    driver = setup
    login_page = Login(driver)
    driver.get(base_url)
    driver.maximize_window()

    with allure.step(f"Logging in as {role}"):
        login_page.click_login_lp()
        login_page.send_email(email)
        login_page.send_password(password)
        login_page.click_login()
        login_page.close_success_toast(driver)

    with allure.step("Verifying login success"):
        WebDriverWait(driver, 20).until(EC.url_contains("dashboard"))
        assert "dashboard" in driver.current_url, f"Login failed for role: {role}"
        allure.attach(driver.get_screenshot_as_png(), name=f"{role}_login_success", attachment_type=AttachmentType.PNG)

    return driver, login_page, role


# -------- Allure Environment Hook --------
@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    config = ConfigManager()
    base_url = config.get_base_url()
    write_allure_environment(base_url)


# -------- Screenshot on Failure Hook --------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("setup")
        if driver:
            allure.attach(driver.get_screenshot_as_png(), name="screenshot_on_failure",
                          attachment_type=AttachmentType.PNG)


import os

config_path = os.path.join(os.path.dirname(__file__), 'data', 'config.ini')
print("Config path:", config_path)
