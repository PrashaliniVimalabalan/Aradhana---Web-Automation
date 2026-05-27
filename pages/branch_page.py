# branch_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


class BranchPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ================= LOCATORS =================

    branch_menu = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[1]/div/div[2]/a[3]'
    )

    search_box = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[1]/div/input'
    )

    add_branch_button = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[1]/div[2]/button'
    )

    country_dropdown = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[3]/div/form/div[1]/div[1]/select'
    )

    branch_name_input = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[3]/div/form/div[1]/div[2]/input'
    )

    # ADD BRANCH BUTTON
    submit_branch_button = (
        By.XPATH,
        "//button[contains(text(),'Add Branch')]"
    )

    edit_button = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[2]/table/tbody/tr[1]/td[4]/button[1]'
    )

    # UPDATE BUTTON
    update_button = (
        By.XPATH,
        "//button[contains(text(),'Update')]"
    )

    delete_icon = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[2]/table/tbody/tr[1]/td[4]/button[2]'
    )

    delete_confirm_button = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[3]/div/div/button[2]'
    )

    # ================= METHODS =================

    def open_branch_page(self):

        branch = self.wait.until(
            EC.element_to_be_clickable(self.branch_menu)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            branch
        )

    def search_branch(self, keyword):

        search = self.wait.until(
            EC.presence_of_element_located(self.search_box)
        )

        search.clear()

        search.send_keys(keyword)

    def click_add_branch(self):

        add_branch = self.wait.until(
            EC.element_to_be_clickable(self.add_branch_button)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add_branch
        )

    def add_new_branch(self, country, branch_name):

        # Select Country
        dropdown = Select(
            self.wait.until(
                EC.presence_of_element_located(self.country_dropdown)
            )
        )

        dropdown.select_by_visible_text(country)

        # Enter Branch Name
        branch = self.wait.until(
            EC.presence_of_element_located(self.branch_name_input)
        )

        branch.clear()

        branch.send_keys(branch_name)

        # Click Add Branch
        submit = self.wait.until(
            EC.element_to_be_clickable(self.submit_branch_button)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            submit
        )

    def click_edit(self):

        time.sleep(5)

        edit = self.wait.until(
            EC.element_to_be_clickable(self.edit_button)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            edit
        )

    def update_branch(self):

        update = self.wait.until(
            EC.element_to_be_clickable(self.update_button)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            update
        )

    def delete_branch(self):

        time.sleep(3)

        delete = self.wait.until(
            EC.element_to_be_clickable(self.delete_icon)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            delete
        )

        confirm = self.wait.until(
            EC.element_to_be_clickable(self.delete_confirm_button)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            confirm
        )