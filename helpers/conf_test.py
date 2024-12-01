import pytest
import allure
from selenium import webdriver
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # This will help manage chromedriver automatically


@pytest.fixture(scope="function")
def setup(request):
    options = webdriver.ChromeOptions()
    chromedriver_path = ChromeDriverManager().install()
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)
    request.addfinalizer(driver.quit)
    return driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('setup')
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=AttachmentType.PNG
            )
