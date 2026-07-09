import pytest
from pages.login import LoginPage
from pages.customer_dashboard import CustomerDashboard
from pages.bank_manager_dashboard import BankManagerDashboard
from utils.excel_reader import read_test_data
from utils.datehelper import DateHelper
import time


TEST_DATA = read_test_data(
    "TestCase.xlsx"
)

@pytest.mark.tc_id("ADC001")
@pytest.mark.tc_desc("Add valid customer")
def test_add_valid_customer(driver):

    try:

        driver.get(
            "https://www.globalsqa.com/angularJs-protractor/BankingProject/"
        )

        first_name = TEST_DATA["Text1"]
        last_name = TEST_DATA["Text2"]
        post_code = TEST_DATA["Text3"]

        login_page = LoginPage(driver)

        login_page.click_bank_manager_login()
    
        dashboard = BankManagerDashboard(driver)

        dashboard.click_add_customer_tab()
        dashboard.fill_customer_information(first_name, last_name, post_code)
        dashboard.click_add_customer_submit_button()
        dashboard.verify_add_customer(first_name, last_name, post_code)
        dashboard.click_home_button()
        
        login_page.click_customer_login()
        customer_name = first_name + " " + last_name
        login_page.select_customer(customer_name)

    except Exception as e:

        raise AssertionError(
            f"Add valid customer failed. Reason: {str(e)}"
        )
    
@pytest.mark.tc_id("OPA001")
@pytest.mark.tc_desc("Open valid account")
def test_open_valid_account(driver):

    try:

        driver.get(
            "https://www.globalsqa.com/angularJs-protractor/BankingProject/"
        )

        customer1 = TEST_DATA["Customer1"]
        currency1 = TEST_DATA["Currency1"]

        login_page = LoginPage(driver)

        login_page.click_bank_manager_login()
    
        dashboard = BankManagerDashboard(driver)

        dashboard.click_open_account_tab()
        dashboard.select_customer(customer1)
        dashboard.select_currency(currency1)
        dashboard.click_process_button()
        time.sleep(1)
        account_number = dashboard.verify_open_account(customer1)
        dashboard.click_home_button()
        
        login_page.click_customer_login()
        login_page.select_customer(customer1)
        login_page.click_login()

        custDashboard = CustomerDashboard(driver)
        custDashboard.select_account(account_number)

    except Exception as e:

        raise AssertionError(
            f"Open valid account failed. Reason: {str(e)}"
        )