from selenium.webdriver.common.by import By


def test_admin_edit(driver):

    driver.find_element(By.LINK_TEXT,"Admin Dashboard").click()

    driver.find_element(By.LINK_TEXT,"Edit").click()

    title = driver.find_element(By.NAME,"title")

    title.clear()

    title.send_keys("Senior Python Developer")

    driver.find_element(By.TAG_NAME,"button").click()

    assert "Senior Python Developer" in driver.page_source

    print("Edit Job Passed")