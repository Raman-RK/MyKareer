import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # This will help manage chromedriver automatically


@pytest.fixture(scope="session")
def setup(request):
    """
    Fixture to set up a WebDriver instance for browser automation testing.
    """
    # Set Chrome options if needed
    options = webdriver.ChromeOptions()
    # Optionally, you can add more options here, e.g., options.add_argument("--headless")

    # Use webdriver_manager to automatically download and install chromedriver
    chromedriver_path = ChromeDriverManager().install()

    # Set up the Service object with the chromedriver path
    service = Service(chromedriver_path)

    # Initialize the Chrome WebDriver with the service and options
    driver = webdriver.Chrome(service=service, options=options)

    # Set up WebDriver to use throughout the test session
    request.addfinalizer(driver.quit)  # Ensure driver quits after the test session

    return driver
