from selenium.webdriver.common.by import By

def test_search_job(driver):

    driver.get("http://127.0.0.1:7777/jobs/")

    #search_box = driver.find_element(By.NAME, "keyword")
    #search_box.send_keys("python")

    #driver.find_element(By.TAG_NAME, "button").click()

    #assert "python developer" in driver.page_source.lower()

    print("Current URL:",driver.current_url)
    print(driver.title)
    print(driver.page_source)