from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.jobs_page import JobsPage
from utils.logger import logger


def test_apply(driver):

    logger.info("Starting Apply Test")

    login = LoginPage(driver)
    login.login("admin", "admin123")

    logger.info("Login Successful")

    jobs = JobsPage(driver)
    jobs.open_jobs()

    logger.info("Jobs Page Opened")

    jobs.apply_first_job()

    logger.info("Applied for First Job")

    wait = WebDriverWait(driver, 10)

    heading = wait.until(
        EC.visibility_of_element_located((By.TAG_NAME, "h2"))
    )

    logger.info("Application Submitted Successfully")

    assert heading.text == "My Applications"

    logger.info("Apply Test Passed")