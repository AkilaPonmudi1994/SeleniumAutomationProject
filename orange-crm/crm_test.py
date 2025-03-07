import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class OrangeHRMTest:
    # Constants
    BASE_URL = "https://opensource-demo.orangehrmlive.com/"
    DEFAULT_USERNAME = "Admin"
    DEFAULT_PASSWORD = "admin123"

    def __init__(self):
        self.driver = self._setup_driver()
        self.wait = WebDriverWait(self.driver, 10)

    def _setup_driver(self):
        """Initialize and configure the Chrome driver"""
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get(self.BASE_URL)
        driver.maximize_window()
        driver.implicitly_wait(3)
        return driver

    def login(self, username, password):
        """Login to the application"""
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

    def search_by_employee_name(self, employee_name):
        """Search for an employee by name"""
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

    def search_by_username(self, username):
        """Search for a user by username"""
        search_input = self.driver.find_element(
            By.XPATH,
            "//label[text()='Username']/following::input[@class='oxd-input oxd-input--active']",
        )
        search_input.send_keys(username)
        self.driver.implicitly_wait(3)

        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        print("Search completed for username")
        time.sleep(5)

    def read_table_data(self):
        """Read data from the admin table"""
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

    def run_employee_search_tests(self):
        """Run employee search tests"""
        initial_data = self.read_table_data()
        print(initial_data)

        for employee in initial_data:
            employee_name = employee.get("employee_name")
            self.search_by_employee_name(employee_name)

            search_results = self.read_table_data()
            result_name = search_results[0].get("employee_name")

            if self.compare_search_results(employee_name, result_name):
                print(f"{employee_name} search test passed")

    def run_username_search_tests(self):
        """Run username search tests"""
        initial_data = self.read_table_data()
        print(initial_data)

        for user in initial_data:
            username = user.get("username")
            self.search_by_username(username)

            search_results = self.read_table_data()
            result_username = search_results[0].get("username")

            if self.compare_search_results(username, result_username):
                print(f"{username} search test passed")

    def cleanup(self):
        """Clean up resources"""
        self.driver.quit()


def main():
    test = OrangeHRMTest()
    try:
        test.login(test.DEFAULT_USERNAME, test.DEFAULT_PASSWORD)
        test.run_employee_search_tests()
        time.sleep(5)
        test.run_username_search_tests()
    finally:
        test.cleanup()


if __name__ == "__main__":
    main()
