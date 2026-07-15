from selenium.webdriver.common.by import By


def test_admin_delete(driver):

    driver.find_element(By.LINK_TEXT,"Admin Dashboard").click()

    driver.find_element(By.LINK_TEXT,"Delete").click()

    assert "Python Automation Engineer" not in driver.page_source

    print("Delete Job Passed")