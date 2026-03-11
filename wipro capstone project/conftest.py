import pytest
from selenium import webdriver
import os
from datetime import datetime


@pytest.fixture
def driver():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://phptravels.net/flights")

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver is not None:
            screenshots_dir = "screenshots1"
            os.makedirs(screenshots_dir, exist_ok=True)

            file_name = f"{item.nodeid.replace('::','_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            try:
                driver.save_screenshot(file_path)
                print(f"Screenshot saved at {file_path}")
            except Exception as e:
                print(f"Screenshot capture failed: {e}")