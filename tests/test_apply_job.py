from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_apply_job(driver):

    # Open login page
    driver.get("http://127.0.0.1:7777/login/")

    # Login with an existing job seeker account
    driver.find_element(By.NAME, "username").send_keys("venu")
    driver.find_element(By.NAME, "password").send_keys("venu123")

    driver.find_element(By.TAG_NAME, "button").click()

    # Open jobs page
    driver.get("http://127.0.0.1:7777/jobs/")

    # Wait until Apply links appear
    apply_links = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.LINK_TEXT, "Apply"))
    )

    # Click the first Apply link
    apply_links[0].click()

    # Verify redirect
    assert "My Applications" in driver.page_source
    #assert "Python Developer" in driver.page_source