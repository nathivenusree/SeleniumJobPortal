from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def test_register(driver):

    driver.get("http://127.0.0.1:7777/register/")

    username = "user" + str(int(time.time()))

    driver.find_element(By.NAME, "username").send_keys(username)

    driver.find_element(By.NAME, "email").send_keys(
        "test@example.com"
    )

    Select(
        driver.find_element(By.NAME, "user_type")
    ).select_by_visible_text("Job Seeker")

    driver.find_element(By.NAME, "password1").send_keys(
        "Test@12345"
    )

    driver.find_element(By.NAME, "password2").send_keys(
        "Test@12345"
    )

    driver.find_element(By.TAG_NAME, "button").click()

    #assert "Login" in driver.page_source
    print("Current URL:",driver.current_url)
    print(driver.page_source)