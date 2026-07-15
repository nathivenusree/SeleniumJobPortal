from utils.logger import logger
from pages.login_page import LoginPage

def test_login(driver):
    logger.info("Starting Login Test")

    driver.get("http://127.0.0.1:7777/login/")

    login = LoginPage(driver)
    login.login("venu", "venu123")

    logger.info("Login Successful")

    # Verify login succeeded
    assert "/login/" not in driver.current_url
    

    logger.info("Test Completed Successfully")