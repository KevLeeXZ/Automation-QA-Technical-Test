from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.helper import SeleniumHelper

class BankManagerDashboard:
    
    HOME_BUTTON = (
        By.XPATH,
        "//button[@ng-click='home()']"
    )

    ADD_CUSTOMER_TAB = (
        By.XPATH,
        "//button[@ng-click='addCust()']"
    )

    OPEN_ACCOUNT_TAB = (
        By.XPATH,
        "//button[@ng-click='openAccount()']"
    )

    CUSTOMERS_TAB = (
        By.XPATH,
        "//button[@ng-click='showCust()']"
    )  

    ADD_CUSTOMER_FIRST_NAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='First Name']"
    )

    ADD_CUSTOMER_LAST_NAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='Last Name']"
    )

    ADD_CUSTOMER_POST_CODE_INPUT = (
        By.XPATH,
        "//input[@placeholder='Post Code']"
    )
    
    ADD_CUSTOMER_SUBMIT_BUTTON = (
        By.XPATH,
        "//button[@type='submit' and contains(text(),'Add Customer')]"
    )

    CUSTOMER_DROPDOWN = (
        By.ID,
        "userSelect"
    )

    CURRENCY_DROPDOWN = (
        By.ID,
        "currency"
    )

    PROCESS_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Process')]"
    )
    
    SEARCH_CUSTOMER_INPUT = (
        By.XPATH,
        "//input[@placeholder='Search Customer']"
    )

    TABLE_HEADERS = (
        By.XPATH,
        "//table/thead/tr[1]/td"
    )

    CUSTOMER_ROWS = (
        By.XPATH,
        "//table/tbody/tr"
    )

    def __init__(self, driver):
        self.driver = driver
        self.helper = SeleniumHelper(driver)

    def click_add_customer_tab(self):

        try:
            self.helper.click_element(
                self.ADD_CUSTOMER_TAB
            )

        except Exception as e:
            raise Exception(
                f"Unable to click Add Customer tab. Error: {str(e)}"
            )

    def click_open_account_tab(self):

        try:
            self.helper.click_element(
                self.OPEN_ACCOUNT_TAB
            )

        except Exception as e:
            raise Exception(
                f"Unable to click Open Account tab. Error: {str(e)}"
            )

    def click_customers_tab(self):

        try:
            self.helper.click_element(
                self.CUSTOMERS_TAB
            )

        except Exception as e:
            raise Exception(
                f"Unable to click Customers tab. Error: {str(e)}"
            )

    def click_home_button(self):

        try:
            self.helper.click_element(
                self.HOME_BUTTON
            )

        except Exception as e:
            raise Exception(
                f"Unable to click Home button. Error: {str(e)}"
            )

    def fill_customer_information(self, first_name, last_name, post_code):
        
        try:
            self.helper.enter_text(
                self.ADD_CUSTOMER_FIRST_NAME_INPUT, first_name
            )

            self.helper.enter_text(
                self.ADD_CUSTOMER_LAST_NAME_INPUT, last_name
            )

            self.helper.enter_text(
                self.ADD_CUSTOMER_POST_CODE_INPUT, post_code
            )
        except Exception as e:
            raise Exception(
                f"Unable to click Customers tab. Error: {str(e)}"
            )
    
    def click_add_customer_submit_button(self):

        try:
            self.helper.click_element(
                self.ADD_CUSTOMER_SUBMIT_BUTTON
            )

        except Exception as e:
            raise Exception(
                f"Unable to click Add Customer submit button. Error: {str(e)}"
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

    def select_currency(self, currency):
        try:
            dropdown = Select(
                self.helper.find_element(
                    self.CURRENCY_DROPDOWN
                )
            )

            dropdown.select_by_visible_text(
                currency
            )

        except Exception as e:
            raise Exception(
                f"Unable to select currency '{currency}'. Error: {str(e)}"
            )

    def click_process_button(self):

        try:
            self.helper.click_element(
                self.PROCESS_BUTTON
            )

        except Exception as e:
            raise Exception(
                f"Unable to click Process button. Error: {str(e)}"
            )

    def table_row_locator(self, row, column_index):

        return (
            By.XPATH, 
            f"//table/tbody/tr[{row}]/td[{column_index}]"
        )

    def get_row_value(self, row, column_name):        
        column_index = self.helper.get_column_index(self.TABLE_HEADERS, column_name) + 1
        row_locator = self.table_row_locator(row, column_index)

        return self.helper.get_text(row_locator)

    def get_first_name(self, row):
        return self.get_row_value(row, "First Name")

    def get_last_name(self, row):
        return self.get_row_value(row, "Last Name")
    
    def get_post_code(self, row):
        return self.get_row_value(row, "Post Code")
    
    def get_account_number(self, row):
        return self.get_row_value(row, "Account Number")

    def verify_add_customer(self, first_name, last_name, post_code):

        try:
            alert_message = (
                self.helper.get_alert_text()
            )

            assert "Customer added successfully" in alert_message, (
                f"Expected alert to contain 'Customer added successfully', "
                f"but found '{alert_message}'"
            )

            self.helper.accept_alert()

            self.click_open_account_tab()
            customer_name = first_name + " " + last_name
            self.select_customer(customer_name)

            self.click_customers_tab()
            self.helper.enter_text(
                self.SEARCH_CUSTOMER_INPUT, first_name
            )
            row_count = self.helper.get_element_count(
                self.CUSTOMER_ROWS
                )
            assert row_count == 1, (
                f"Expected transaction history to be 1, "
                f"but found {row_count} records"
            )
            new_first_name = self.get_first_name(1)
            if new_first_name != first_name:
                raise AssertionError(
                    f"Transaction amount validation falied. "
                    f"Expected '{first_name}', "
                    f"but found '{new_first_name}'"
                )

            new_last_name = self.get_last_name(1)
            if new_last_name != last_name:
                raise AssertionError(
                    f"Transaction amount validation falied. "
                    f"Expected '{last_name}', "
                    f"but found '{new_last_name}'"
                )
            
            new_post_code = self.get_post_code(1)
            if new_post_code != post_code:
                raise AssertionError(
                    f"Transaction amount validation falied. "
                    f"Expected '{post_code}', "
                    f"but found '{new_post_code}'"
                )
            
        except Exception as e:
            raise Exception(
                f"Unable to verify whether customer is added. Error: {str(e)}"
            )
        
    def verify_open_account(self, customer_name):

        try:
            
            alert_message = (
                self.helper.get_alert_text()
            )

            assert "Account created successfully with account Number" in alert_message, (
                f"Expected alert to contain 'Customer added successfully', "
                f"but found '{alert_message}'"
            )
            
            self.helper.accept_alert()
            
            account_number = alert_message.split("Number :")[1].strip()

            self.click_customers_tab()
            first_name = customer_name.split()[0]
            self.helper.enter_text(
                self.SEARCH_CUSTOMER_INPUT, first_name
            )
            row_count = self.helper.get_element_count(
                self.CUSTOMER_ROWS
                )
            assert row_count == 1, (
                f"Expected transaction history to be 1, "
                f"but found {row_count} records"
            )
            
            new_account_number = self.get_account_number(1)
            assert account_number in new_account_number, (
                f"Expected account number to contain '{account_number}', "
                f"but found '{new_account_number}'"
            )
            
            return account_number
            
        except Exception as e:
            raise Exception(
                f"Unable to verify whether account is opened. Error: {str(e)}"
            )