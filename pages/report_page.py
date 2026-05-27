# report_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ReportPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ================= LOCATORS =================

    report_menu = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[1]/div/div[2]/a[9]'
    )

    payment_report = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div/div[1]/div'
    )

    exam_report = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div/div[2]'
    )

    result_report = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div/div[3]'
    )

    # ================= METHODS =================

    def open_report_page(self):

        report = self.wait.until(
            EC.element_to_be_clickable(self.report_menu)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            report
        )

    def open_payment_report(self):

        payment = self.wait.until(
            EC.element_to_be_clickable(self.payment_report)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            payment
        )

    def open_exam_report(self):

        exam = self.wait.until(
            EC.element_to_be_clickable(self.exam_report)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            exam
        )

    def open_result_report(self):

        result = self.wait.until(
            EC.element_to_be_clickable(self.result_report)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            result
        )