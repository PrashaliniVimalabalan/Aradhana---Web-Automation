# user_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


class UserPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ================= LOCATORS =================

    user_menu = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[1]/div/div[2]/a[4]/span'
    )

    search_box = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div[1]/div/input'
    )

    roles_filter = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div[2]/select[1]'
    )

    course_filter = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div[2]/select[3]'
    )

    # ================= METHODS =================

    def open_user_page(self):

        user = self.wait.until(
            EC.element_to_be_clickable(self.user_menu)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            user
        )

    def search_user(self, keyword):

        search = self.wait.until(
            EC.presence_of_element_located(self.search_box)
        )

        search.clear()

        search.send_keys(keyword)

    def select_role(self, role):

        role_dropdown = Select(
            self.wait.until(
                EC.presence_of_element_located(self.roles_filter)
            )
        )

        role_dropdown.select_by_visible_text(role)

    def select_course(self, course):

        course_dropdown = Select(
            self.wait.until(
                EC.presence_of_element_located(self.course_filter)
            )
        )

        course_dropdown.select_by_visible_text(course)