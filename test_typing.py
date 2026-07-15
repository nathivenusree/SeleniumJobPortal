from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://127.0.0.1:7777/login/")

driver.find_element(By.NAME, "username").send_keys("venu")
driver.find_element(By.NAME, "password").send_keys("venu123")
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(2)

driver.get("http://127.0.0.1:7777/add-job/")

time.sleep(2)

title = driver.find_element(By.ID, "id_title")

driver.execute_script("arguments[0].focus();", title)

print("Focused:", driver.execute_script("return document.activeElement.id"))

title.send_keys("Hello")

print("Value:", title.get_attribute("value"))

print("Current URL:", driver.current_url)
print("Page Title:", driver.title)

title = driver.find_element(By.ID, "id_title")

print("Outer HTML:")
print(title.get_attribute("outerHTML"))

print("Readonly:", title.get_attribute("readonly"))
print("Disabled:", title.get_attribute("disabled"))

title.click()
print("Focused element ID:", driver.execute_script("return document.activeElement.id"))
#title.send_keys("Hello")

driver.execute_script(
    "arguments[0].value = arguments[1];",
    title,
    "Hello"
)

print("Value after JS:", title.get_attribute("value"))

print("Value after send_keys:", title.get_attribute("value"))

driver.save_screenshot("typing_test.png")

input("Press Enter to close...")
driver.quit()