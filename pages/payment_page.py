# pages/payment_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class PaymentPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        # Payment Menu
        self.payment_menu = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div[1]/div/div[2]/a[6]"
        )

        # Add Payment Button
        self.add_payment_button = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div[2]/main/div/div[1]/button"
        )

        # Search Student
        self.search_student = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div[2]/main/div/div[4]/div/div[3]/div/div[1]/input"
        )

        # Student Result
        self.student_result = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div[2]/main/div/div[4]/div/div[3]/div/div[2]/div/div/div[2]/div[2]"
        )

        # Next Button Step 1
        self.next_button_1 = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div[2]/main/div/div[4]/div/div[4]/button"
        )

        # March Month Button
        self.month_button = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div[2]/main/div/div[4]/div/div[3]/div/div[1]/div/div[2]/button[3]"
        )

        # Next Button Step 2
        self.next_button_2 = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div[2]/main/div/div[4]/div/div[4]/button[2]"
        )

        # Submit Payment
        self.submit_payment_button = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div[2]/main/div/div[4]/div/div[4]/button[2]"
        )

        # Generate Receipt
        self.generate_receipt_button = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div[2]/main/div/div[4]/div/button[1]"
        )

    # Open Payment Page
    def open_payment_page(self):

        payment = self.wait.until(
            EC.element_to_be_clickable(self.payment_menu)
        )

        payment.click()

        time.sleep(3)

    # Click Add Payment
    def click_add_payment(self):

        add_btn = self.wait.until(
            EC.element_to_be_clickable(self.add_payment_button)
        )

        add_btn.click()

        time.sleep(3)

    # Search Student
    def search_student_name(self, student):

        search = self.wait.until(
            EC.visibility_of_element_located(self.search_student)
        )

        search.clear()

        search.send_keys(student)

        time.sleep(3)

    # Select Student
    def select_student(self):

        student = self.wait.until(
            EC.element_to_be_clickable(self.student_result)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            student
        )

        time.sleep(2)

        student.click()

        time.sleep(3)

    # Next Step 1
    def click_next_step_1(self):

        next1 = self.wait.until(
            EC.element_to_be_clickable(self.next_button_1)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            next1
        )

        time.sleep(5)

    # Select Month
    def select_payment_month(self):

        time.sleep(5)

        month = self.wait.until(
            EC.element_to_be_clickable(self.month_button)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            month
        )

        time.sleep(2)

        month.click()

        print("MONTH SELECTED")

        time.sleep(5)

    # Next Step 2
    def click_next_step_2(self):

        time.sleep(5)

        next2 = self.wait.until(
            EC.presence_of_element_located(self.next_button_2)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            next2
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            next2
        )

        print("STEP 2 NEXT CLICKED")

        time.sleep(5)

    # Submit Payment
    def submit_payment(self):

        submit = self.wait.until(
            EC.element_to_be_clickable(
                self.submit_payment_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            submit
        )

        print("PAYMENT SUBMITTED")

        time.sleep(5)

    # Generate Receipt
    def generate_receipt(self):

        receipt = self.wait.until(
            EC.element_to_be_clickable(
                self.generate_receipt_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            receipt
        )

        print("RECEIPT GENERATED")

        time.sleep(5)