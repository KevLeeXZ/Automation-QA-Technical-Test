from selenium.webdriver.common.by import By
from utils.helper import SeleniumHelper
from utils.datehelper import DateHelper

class TransactionHistory:

    TABLE_HEADERS = (
        By.XPATH,
        "//table/thead/tr[1]/td"
    )

    TRANSACTION_ROWS = (
        By.XPATH,
        "//table/tbody/tr"
    )

    DATE_TIME_HEADER = (
        By.XPATH,
        "//table/thead/tr[1]/td/*[contains(text(), 'Date-Time')]"
    )

    RESET_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Reset')]"
    )

    BACK_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Back')]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.helper = SeleniumHelper(driver)
        self.date_helper = DateHelper()

    def table_row_locator(self, row, column_index):

        return (
            By.XPATH, 
            f"//table/tbody/tr[{row}]/td[{column_index}]"
        )

    def get_row_value(self, row, column_name):        
        column_index = self.helper.get_column_index(self.TABLE_HEADERS, column_name) + 1
        row_locator = self.table_row_locator(row, column_index)

        return self.helper.get_text(row_locator)

    def get_datetime(self, row):
        return self.get_row_value(row, "Date-Time")

    def get_amount(self, row):
        return self.get_row_value(row, "Amount")
    
    def get_transaction_type(self, row):
        return self.get_row_value(row, "Transaction Type")

    def sort_date_time(self):
        try:
            self.helper.click_element(
                self.DATE_TIME_HEADER
            )

        except Exception as e:
            raise Exception(
                f"Unable to click Date-Time header to sort. Error: {str(e)}"
            )

    def click_reset_button(self):
        try:
            self.helper.click_element(
                self.RESET_BUTTON
            )

        except Exception as e:
            raise Exception(
                f"Unable to click Reset button. Error: {str(e)}"
            )
    
    def click_back_button(self):
        try:
            self.helper.click_element(
                self.BACK_BUTTON
            )

        except Exception as e:
            raise Exception(
                f"Unable to click Back button. Error: {str(e)}"
            )

    def verify_latest_record_date(self, expected_date):
        transaction_datetime = self.get_datetime(1)
        transaction_date = self.date_helper.extract_date(transaction_datetime)

        if transaction_date != expected_date:

            raise AssertionError(
                f"Transaction date validation falied. "
                f"Expected '{expected_date}', "
                f"but found '{transaction_date}'"
            )
        
    def verify_latest_record_amount(self, expected_amount):
        transaction_amount = self.get_amount(1)

        if transaction_amount != expected_amount:

            raise AssertionError(
                f"Transaction amount validation falied. "
                f"Expected '{expected_amount}', "
                f"but found '{transaction_amount}'"
            )
        
    def verify_latest_record_transaction_type(self, expected_type):
        transaction_type = self.get_transaction_type(1)

        if transaction_type != expected_type:

            raise AssertionError(
                f"Transaction type validation falied. "
                f"Expected '{expected_type}', "
                f"but found '{transaction_type}'"
            )
        
    def verify_transaction_history_empty(self):
        row_count = self.helper.get_element_count(
            self.TRANSACTION_ROWS
        )

        assert row_count == 0, (
            f"Expected transaction history to be empty, "
            f"but found {row_count} records"
        )