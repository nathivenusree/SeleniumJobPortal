import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.TAG_NAME, "button").click()

    def click_add_job(self):
        self.driver.get("http://127.0.0.1:7777/add-job/")

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "id_title"))
        )

        print("Current URL:", self.driver.current_url)

    

    def enter_job(self, title, description, location, salary):

        data = {
            "id_title": title,
            "id_description": description,
            "id_location": location,
            "id_salary": salary,
    }

        for field_id, value in data.items():

           element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, field_id))
        )

        print("\n==========")
        print("Field:", field_id)
        print("Before:", element.get_attribute("value"))

        element.click()
        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(value)

        print("After send_keys:", element.get_attribute("value"))

        if field_id == "id_description":
            print("Textarea text:", element.text)
            

            
            
    def save_job(self):

        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[type='submit']")
            )
        )

        print("Before click:", self.driver.current_url)

        button.click()

        time.sleep(2)

        print("After click:", self.driver.current_url)