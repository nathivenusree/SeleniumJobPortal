import os
import pytest
from utils.driver_factory import get_driver


@pytest.fixture
def driver():
    driver = get_driver()
    driver.get("http://127.0.0.1:7777/login/")

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs["driver"]

        # Create screenshots folder if it doesn't exist
        os.makedirs("screenshots", exist_ok=True)

        driver.save_screenshot(
            f"screenshots/{item.name}.png"
        )