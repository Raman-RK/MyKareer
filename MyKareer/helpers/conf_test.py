import os

import pytest
from selenium import webdriver
import subprocess
import time


@pytest.fixture(scope="session")
def setup(request):
    """
    Fixture to set up a WebDriver instance for browser automation testing.

    Args:
        request (pytest.FixtureRequest): Provides access to configuration information.

    Returns:
        WebDriver: Instance of the WebDriver (in this case, Chrome).
    """
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    def teardown():
        driver.quit()

    request.addfinalizer(teardown)
    return driver


@pytest.fixture(scope="module", autouse=True)
def screen_recorder():
    output_dir = os.path.join(os.path.dirname(__file__), "recordings")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "C://Users//Kajal//Desktop//Fonu//output.MP4")
    # Define the ffmpeg command
    ffmpeg_cmd = [
        'ffmpeg',
        '-f', 'gdigrab',  # Screen grab (on Windows, use 'x11grab' on Linux)
        '-framerate', '30',  # Frames per second
        '-i', 'desktop',  # Input source (use ':0.0' on Linux)
        '-q:v', '10',  # Quality level (lower number is higher quality)
        'output.mp4',  # Output file
        output_file
    ]

    # Start the ffmpeg process
    ffmpeg_process = subprocess.Popen(ffmpeg_cmd)

    # Allow ffmpeg to start
    time.sleep(2)

    yield

    # Stop the ffmpeg process
    ffmpeg_process.terminate()
