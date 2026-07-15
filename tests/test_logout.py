from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


def test_logout(driver):

    login = LoginPage(driver)

    login.login("venu","venu123")

    driver.find_element(By.LINK_TEXT,"Logout").click()

    assert driver.current_url.endswith("/")

    print("Logout Test Passed")