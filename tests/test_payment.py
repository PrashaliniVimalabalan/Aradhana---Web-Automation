# test_payment.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from pages.login_page import LoginPage
from pages.payment_page import PaymentPage


def test_payment_module():

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

    # Create Payment Object
    payment = PaymentPage(driver)

    # Open Payment Page
    payment.open_payment_page()

    print("PAYMENT PAGE OPENED")

    time.sleep(3)

    # Add Payment
    payment.click_add_payment()

    print("ADD PAYMENT POPUP OPENED")

    time.sleep(3)

    # Search Student
    payment.search_student_name("Muzzamil")

    print("STUDENT SEARCH SUCCESSFUL")

    time.sleep(2)

    # Select Student
    payment.select_student()

    print("STUDENT SELECTED")

    time.sleep(2)

    # Next Step 1
    payment.click_next_step_1()

    print("NEXT STEP 1 COMPLETED")

    time.sleep(3)

    # Scroll Down Inside Popup
    driver.execute_script("window.scrollBy(0,500)")

    time.sleep(2)

    # Select March Month
    payment.select_payment_month()

    print("MONTH SELECTED")

    time.sleep(5)

    # Next Step 2
    payment.click_next_step_2()

    print("NEXT STEP 2 COMPLETED")

    time.sleep(3)

    # Submit Payment
    payment.submit_payment()

    print("PAYMENT SUBMITTED")

    time.sleep(5)

    # Generate Receipt
    payment.generate_receipt()

    print("RECEIPT GENERATED")

    time.sleep(5)

    # Close Browser
    driver.quit()