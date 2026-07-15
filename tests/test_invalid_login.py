from selenium.webdriver.common.by import By


def test_invalid_login(driver):
    driver.get("http://127.0.0.1:7777/login/")

    driver.find_element(By.NAME, "username").send_keys("wronguser")
    driver.find_element(By.NAME, "password").send_keys("wrongpassword")

    driver.find_element(By.TAG_NAME, "button").click()

    print(driver.page_source)
 
    assert "Invalid username or password" in driver.page_source