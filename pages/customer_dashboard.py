from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.helper import SeleniumHelper

class CustomerDashboard:
    
    CUSTOMER_NAME = (
        By.XPATH,
        "//strong/span"
    )
    
    ACCOUNT_DROPDOWN = (
        By.ID,
        "accountSelect"
    )

    ACCOUNT_DETAILS = (
        By.XPATH,
        "//div[contains(@class,'center')]/strong"
    )

    TRANSACTIONS_TAB = (
        By.XPATH,
        "//button[contains(text(), 'Transactions')]"
    )   

    DEPOSIT_TAB = (
        By.XPATH,
        "//button[contains(text(),'Deposit')]"
    )

    DEPOSIT_SUBMIT_BUTTON = (
        By.XPATH,
        "//button[@type='submit' and contains(text(),'Deposit')]"
    )

    AMOUNT_INPUT = (
        By.XPATH,
        "//input[@placeholder='amount']"
    )
    
    DEPOSIT_SUCCESSFUL_MESSAGE = (
        By.XPATH,
        "//*[contains(text(), 'Deposit Successful')]"
    )

    TRANSACTION_SUCCESSFUL_MESSAGE = (
        By.XPATH,
        "//*[contains(text(), 'Transaction Successful')]"
    )

    WITHDRAW_TAB = (
        By.XPATH,
        "//button[contains(text(),'Withdrawl')]"
    )

    WITHDRAW_SUBMIT_BUTTON = (
        By.XPATH,
        "//button[@type='submit' and contains(text(),'Withdraw')]"
    )
    

    def __init__(self, driver):
        self.driver = driver
        self.helper = SeleniumHelper(driver)

    def select_account(self, account_number):

        try:
            dropdown = Select(
                self.helper.find_element(
                    self.ACCOUNT_DROPDOWN
                )
            )

            dropdown.select_by_visible_text(
                account_number
            )

        except Exception as e:
            raise Exception(
                f"Unable to select Account Number '{account_number}'. Error: {str(e)}"
            )

    def customer_name_locator(self):

        return (
            By.XPATH,
            f"//strong/span"
        )

    def verify_customer_displayed(self, expected_name):
        
        element = self.helper.find_element(
            self.CUSTOMER_NAME
        )

        actual_name = element.text


        if actual_name != expected_name:

            raise AssertionError(
                f"Customer validation failed. "
                f"Expected '{expected_name}', "
                f"but found '{actual_name}'"
            )
    
    def get_account_details(self):

        elements = self.helper.find_elements(
            self.ACCOUNT_DETAILS
        )

        return {
            "account_number": elements[0].text.strip(),
            "balance": elements[1].text.strip(),
            "currency": elements[2].text.strip()
        }

    def click_transaction_history(self):

        try:
            self.helper.click_element(
                self.TRANSACTIONS_TAB
            )

        except Exception as e:
            raise Exception(
                f"Unable to click Transaction History button. Error: {str(e)}"
            )

    def perform_deposit(self, amount):

        try:
            self.helper.click_element(
                self.DEPOSIT_TAB
            )

            self.helper.enter_text(
                self.AMOUNT_INPUT,
                amount
            )

            self.helper.click_element(
                self.DEPOSIT_SUBMIT_BUTTON
            )

        except Exception as e:
            raise Exception(
                f"Unable to perform Deposit. Error: {str(e)}"
            )
        
    def verify_successful_deposit(self, original_balance, amount):

        try:
            self.helper.element_exists(
                self.DEPOSIT_SUCCESSFUL_MESSAGE
            )

            details = self.get_account_details()
            new_balance = details["balance"]
            expected_balance = int(original_balance) + int(amount)

            if new_balance != str(expected_balance):
                raise AssertionError(
                f"Customer validation failed. "
                f"Expected '{expected_balance}', "
                f"but found '{new_balance}'"
            )

        except Exception as e:
            raise Exception(
                f"Unable to verify whether deposit is successful. Error: {str(e)}"
            )
        
    def perform_withdrawal(self, amount):

        try:
            self.helper.click_element(
                self.WITHDRAW_TAB
            )

            self.helper.enter_text(
                self.AMOUNT_INPUT,
                amount
            )

            self.helper.click_element(
                self.WITHDRAW_SUBMIT_BUTTON
            )

        except Exception as e:
            raise Exception(
                f"Unable to perform Withdawal. Error: {str(e)}"
            )
        
    def verify_successful_withdrawal(self, original_balance, amount):

        try:
            self.helper.element_exists(
                self.TRANSACTION_SUCCESSFUL_MESSAGE
            )

            details = self.get_account_details()
            new_balance = details["balance"]
            expected_balance = int(original_balance) - int(amount)

            if new_balance != str(expected_balance):
                raise AssertionError(
                f"Customer validation failed. "
                f"Expected '{expected_balance}', "
                f"but found '{new_balance}'"
            )

        except Exception as e:
            raise Exception(
                f"Unable to verify whether withdrawal is successful. Error: {str(e)}"
            )
        
    def verify_balance_empty(self):

        try:
            self.helper.element_exists(
                self.TRANSACTION_SUCCESSFUL_MESSAGE
            )

            details = self.get_account_details()
            new_balance = details["balance"]

            if new_balance != "0":
                raise AssertionError(
                f"Customer validation failed. "
                f"Expected '0', "
                f"but found '{new_balance}'"
            )

        except Exception as e:
            raise Exception(
                f"Unable to verify whether withdrawal is successful. Error: {str(e)}"
            )