# test_branch.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from pages.login_page import LoginPage
from pages.branch_page import BranchPage


def test_branch_module():

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

    # Create Branch Object
    branch = BranchPage(driver)

    # Open Branch Page
    branch.open_branch_page()

    print("BRANCH PAGE OPENED")

    time.sleep(3)

    # Search Branch
    branch.search_branch("Chennai")

    print("BRANCH SEARCH SUCCESSFUL")

    time.sleep(3)

    # Add Branch
    branch.click_add_branch()

    print("ADD BRANCH POPUP OPENED")

    time.sleep(2)

    branch.add_new_branch(
        "India",
        "Automation Branch"
    )

    print("NEW BRANCH ADDED")

    time.sleep(5)

    # Edit Branch
    branch.click_edit()

    print("EDIT BUTTON CLICKED")

    time.sleep(3)

    # Update Branch
    branch.update_branch()

    print("BRANCH UPDATED")

    time.sleep(5)

    # Delete Branch
    branch.delete_branch()

    print("BRANCH DELETED")

    time.sleep(5)

    # Close Browser
    driver.quit()
