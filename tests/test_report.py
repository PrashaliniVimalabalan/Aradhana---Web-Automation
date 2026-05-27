# test_report.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from pages.login_page import LoginPage
from pages.report_page import ReportPage


def test_report_module():

    # Launch Browser
    driver = webdriver.Chrome()

    driver.maximize_window()

    # Open Website
    driver.get("https://aradanaqa.pineappleai.cloud/login")

    # Login
    login = LoginPage(driver)

    login.login("admin", "admin123")

    # Wait
    wait = WebDriverWait(driver, 10)

    # Verify Dashboard
    dashboard = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//h1[contains(text(),'Dashboard')]")
        )
    )

    assert dashboard.is_displayed()

    print("LOGIN SUCCESSFUL")

    # Create Report Object
    report = ReportPage(driver)

    # Open Report Page
    report.open_report_page()

    print("REPORT PAGE OPENED")

    time.sleep(3)

    # Payment Report
    report.open_payment_report()

    print("PAYMENT REPORT OPENED")

    time.sleep(3)

    driver.back()

    time.sleep(2)

    # Exam Report
    report.open_exam_report()

    print("EXAM REPORT OPENED")

    time.sleep(3)

    driver.back()

    time.sleep(2)

    # Result Report
    report.open_result_report()

    print("RESULT REPORT OPENED")

    time.sleep(5)

    # Close Browser
    driver.quit()