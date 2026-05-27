# test_user.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from pages.login_page import LoginPage
from pages.user_page import UserPage


def test_user_module():

    # Launch Browser
    driver = webdriver.Chrome()

    # Maximize Browser
    driver.maximize_window()

    # Open Website
    driver.get("https://aradanaqa.pineappleai.cloud/login")

    # Login
    login = LoginPage(driver)

    login.login("admin", "admin123")

    # Wait Object
    wait = WebDriverWait(driver, 10)

    # Verify Dashboard
    dashboard = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//h1[contains(text(),'Dashboard')]")
        )
    )

    assert dashboard.is_displayed()

    print("LOGIN SUCCESSFUL")

    # Create User Page Object
    user = UserPage(driver)

    # Open User Page
    user.open_user_page()

    print("USER PAGE OPENED")

    time.sleep(3)

    # Search User
    user.search_user("Admin")

    print("USER SEARCH SUCCESSFUL")

    time.sleep(3)

    # Select Role Filter
    user.select_role("Teacher")

    print("ROLE FILTER APPLIED")

    time.sleep(3)

    # Select Course Filter
    user.select_course("Keyboard")

    print("COURSE FILTER APPLIED")

    time.sleep(5)

    # Close Browser
    driver.quit()