from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class JobsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_jobs(self):
        self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Jobs"))
        )

        jobs_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Jobs"))
        )

        self.driver.execute_script("arguments[0].click();", jobs_link)

    def apply_first_job(self):
        apply_btn = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Apply"))
        )

        self.driver.execute_script("arguments[0].click();", apply_btn)