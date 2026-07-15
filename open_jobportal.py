from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time



driver = webdriver.Chrome(
    service = Service(ChromeDriverManager().install())
)

driver.maximize_window()

driver.get("http://127.0.0.1:7777/")

print(driver.title)

time.sleep(5)

driver.quit()