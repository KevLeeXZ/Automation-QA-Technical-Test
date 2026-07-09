from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.helper import SeleniumHelper


class LoginPage:

    CUSTOMER_LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Customer Login')]"
    )
    
    BANK_MANAGER_LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Bank Manager Login')]"
    )

    CUSTOMER_DROPDOWN = (
        By.ID,
        "userSelect"
    )


    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Login')]"
    )


    def __init__(self, driver):
        self.driver = driver
        self.helper = SeleniumHelper(driver)


    def click_customer_login(self):

        try:
            self.helper.click_element(
                self.CUSTOMER_LOGIN_BUTTON
            )

        except Exception as e:
            raise Exception(
                f"Unable to click Customer Login button. Error: {str(e)}"
            )

    def click_bank_manager_login(self):

        try:
            self.helper.click_element(
                self.BANK_MANAGER_LOGIN_BUTTON
            )

        except Exception as e:
            raise Exception(
                f"Unable to click Bank Manager Login button. Error: {str(e)}"
            )

    def select_customer(self, customer_name):

        try:
            dropdown = Select(
                self.helper.find_element(
                    self.CUSTOMER_DROPDOWN
                )
            )

            dropdown.select_by_visible_text(
                customer_name
            )

        except Exception as e:
            raise Exception(
                f"Unable to select customer '{customer_name}'. Error: {str(e)}"
            )


    def click_login(self):

        try:
            self.helper.click_element(
                self.LOGIN_BUTTON
            )

        except Exception as e:
            raise Exception(
                f"Unable to click Login button. Error: {str(e)}"
            )