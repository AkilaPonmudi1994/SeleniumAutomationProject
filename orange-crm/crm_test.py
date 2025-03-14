import time
import pytest
import  unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestOrangeHRM:
    # Constants
    BASE_URL = "https://opensource-demo.orangehrmlive.com/"
    DEFAULT_USERNAME = "Admin"
    DEFAULT_PASSWORD = "admin123"


    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self, request):
        print('*********setting up******')
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        cls = request.cls
        driver.get(cls.BASE_URL)
        driver.maximize_window()
        driver.implicitly_wait(3)
        cls.driver = driver
        cls.wait = WebDriverWait(cls.driver, 10)
        yield
        # teardown
        print('*****teardown*****')
        cls.driver.quit()


    def test_login(self):
        """Login to the application
        """
        self.driver.find_element(By.NAME, "username").send_keys(self.DEFAULT_USERNAME)
        self.driver.find_element(By.NAME, "password").send_keys(self.DEFAULT_PASSWORD)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        assert self.driver.title=="OrangeHRM"

    def test_search_by_employee_name(self,):
        """Search for an employee by name"""

        table_data = self.read_table_data()
        employee_names = []
        for data in table_data:
            emp_name =data.get('employee_name')
            employee_names.append(emp_name)

        for employee_name in employee_names:

            search_input = self.driver.find_element(
                By.XPATH, "//input[@placeholder='Type for hints...']"
            )
            search_input.send_keys(employee_name)
            print(f"Searching for employee: {employee_name}")

            dropdown = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'oxd-autocomplete-option')]")
                )
            )
            dropdown.click()

            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            print(f"Search completed for employee: {employee_name}")
            time.sleep(5)
            results = self.driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']/div")
            assert len(results) > 0
            read_latest_table_data = self.read_table_data()
            new_emp_name = read_latest_table_data[0].get('employee_name')
            assert self.compare_search_results(
                employee_name, new_emp_name
            )

    def test_search_by_username(self, ):
        """Search for a user by username"""
        user_names = []
        table_data = self.read_table_data()
        for data in table_data:
            user_name = data.get('username')
            user_names.append(user_name)

        for user_name in user_names:
            search_input = self.driver.find_element(
                By.XPATH,
                "//label[text()='Username']/following::input[@class='oxd-input oxd-input--active']",
            )
            search_input.send_keys(user_name)
            self.driver.implicitly_wait(3)

            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            print("Search completed for username")
            time.sleep(5)
            results = self.driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']/div")
            assert len(results) > 0

    def read_table_data(self):
        """Helper function to read data from the admin table"""
        self.driver.find_element(By.LINK_TEXT, "Admin").click()
        table_data = []
        print('Read first two results')
        for row in range(2):
            try:
                data = {
                    "username": self.driver.find_element(
                        By.XPATH,
                        f"//div[@class='oxd-table-body']/div[{row}]//div//div[2]//div",
                    ).text,
                    "role": self.driver.find_element(
                        By.XPATH,
                        f"//div[@class='oxd-table-body']/div[{row}]//div//div[3]//div",
                    ).text,
                    "employee_name": self.driver.find_element(
                        By.XPATH,
                        f"//div[@class='oxd-table-body']/div[{row}]//div//div[4]//div",
                    ).text,
                    "status": self.driver.find_element(
                        By.XPATH,
                        f"//div[@class='oxd-table-body']/div[{row}]//div//div[5]//div",
                    ).text,
                }
                print(
                    f"{row} {data['username']}\t{data['role']}\t{data['employee_name']}\t{data['status']}"
                )
                table_data.append(data)
            except Exception:
                continue
        return table_data

    def compare_search_results(self, before_name, after_name):
        """Compare search results"""
        if before_name.strip() in after_name.strip():
            print("Search results matched")
            return True
        print(f"Search results mismatch: {before_name} vs {after_name}")
        return False


