from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time




driver = webdriver.Chrome(
    service = Service(ChromeDriverManager().install())
)

driver.maximize_window()

driver.get("http://127.0.0.1:7777/")

time.sleep(2)

driver.find_element(By.LINK_TEXT,"Jobs").click()

time.sleep(2)

driver.find_element(By.LINK_TEXT,"Apply").click()

time.sleep(5)

print("Current URL:",driver.current_url)

driver.quit()