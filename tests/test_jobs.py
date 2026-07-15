from selenium.webdriver.support.ui import WebDriverWait

from utils.logger import logger
from pages.login_page import LoginPage
from pages.jobs_page import JobsPage


def test_jobs(driver):

    logger.info("Starting Jobs Test")

    login = LoginPage(driver)
    login.login("venu", "venu123")

    # Wait until login completes
    WebDriverWait(driver, 10).until(
        lambda d: "/login/" not in d.current_url
    )

    jobs = JobsPage(driver)
    jobs.open_jobs()

    logger.info("Opening Jobs page...")

    assert "/jobs/" in driver.current_url

    logger.info("Jobs Test Passed")