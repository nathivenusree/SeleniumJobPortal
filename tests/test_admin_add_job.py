from pages.admin_page import AdminPage
from selenium.webdriver.support.ui import WebDriverWait


def test_admin_add(driver):

    admin = AdminPage(driver)

    admin.login("venu", "venu123")

    WebDriverWait(driver, 10).until(
        lambda d: d.current_url == "http://127.0.0.1:7777/"
    )

    # Open Add Job page
    admin.click_add_job()
    

    # Debug information
    print("Current URL:", driver.current_url)
    print("Title:", driver.title)
    
    with open("page.html", "w", encoding="utf-8") as f:
         f.write(driver.page_source)

    driver.save_screenshot("add_job_page.png")

    input("Press Enter after checking the Add Job page...")


    admin.enter_job(
        "Python Automation Engineer",
        "Looking for an Automation Testing Engineer",
        "Singapore",
        "7000"
    )

    driver.save_screenshot("after_typing.png")

    admin.save_job()

    print("After Save URL:", driver.current_url)