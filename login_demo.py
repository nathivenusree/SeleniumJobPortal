from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("http://127.0.0.1:7777/login/")

wait = WebDriverWait(driver, 10)

username = wait.until(
    EC.visibility_of_element_located((By.NAME, "username"))
)

username.send_keys("admin")

driver.find_element(By.NAME, "password").send_keys("admin123")

login_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)

print("Clicking login button...")

login_button.click()

time.sleep(5)

print("Current URL:", driver.current_url)
print("Page Title:", driver.title)

input("Press Enter to close...")

driver.quit()

