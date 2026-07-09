import pytest
from pages.login import LoginPage
from pages.customer_dashboard import CustomerDashboard
from pages.transaction_history import TransactionHistory
from utils.excel_reader import read_test_data
from utils.datehelper import DateHelper
import time


TEST_DATA = read_test_data(
    "TestCase.xlsx"
)

@pytest.mark.tc_id("TRN001")
@pytest.mark.tc_desc("Deposit valid amount")
def test_valid_deposit(driver):

    try:

        driver.get(
            "https://www.globalsqa.com/angularJs-protractor/BankingProject/"
        )

        customer1 = TEST_DATA["Customer1"]
        amount1 = TEST_DATA["Amount1"]

        login_page = LoginPage(driver)

        login_page.click_customer_login()
        login_page.select_customer(customer1)
        login_page.click_login()
    
        dashboard = CustomerDashboard(driver)

        account_details = dashboard.get_account_details()
        account_balance = account_details["balance"]
        dashboard.perform_deposit(amount1)
        date_helper = DateHelper()
        today_date = date_helper.get_today_date()
        dashboard.verify_successful_deposit(account_balance, amount1)
        time.sleep(2)
        dashboard.click_transaction_history()

        history = TransactionHistory(driver)
        history.sort_date_time()
        time.sleep(1)
        history.verify_latest_record_date(today_date)
        history.verify_latest_record_amount(amount1)
        history.verify_latest_record_transaction_type("Credit")

    except Exception as e:

        raise AssertionError(
            f"Deposit valid amount failed. Reason: {str(e)}"
        )
    
@pytest.mark.tc_id("TRN010")
@pytest.mark.tc_desc("Withdraw valid amount")
def test_valid_withdrawal(driver):

    try:

        driver.get(
            "https://www.globalsqa.com/angularJs-protractor/BankingProject/"
        )

        customer1 = TEST_DATA["Customer1"]
        amount1 = TEST_DATA["Amount1"]

        login_page = LoginPage(driver)

        login_page.click_customer_login()
        login_page.select_customer(customer1)
        login_page.click_login()
    
        dashboard = CustomerDashboard(driver)

        account_details = dashboard.get_account_details()
        account_balance = account_details["balance"]
        dashboard.perform_withdrawal(amount1)
        date_helper = DateHelper()
        today_date = date_helper.get_today_date()
        dashboard.verify_successful_withdrawal(account_balance, amount1)
        time.sleep(2)
        dashboard.click_transaction_history()

        history = TransactionHistory(driver)
        history.sort_date_time()
        time.sleep(1)
        history.verify_latest_record_date(today_date)
        history.verify_latest_record_amount(amount1)
        history.verify_latest_record_transaction_type("Debit")

    except Exception as e:

        raise AssertionError(
            f"Withdraw valid amount failed. Reason: {str(e)}"
        )
    
@pytest.mark.tc_id("TRN026")
@pytest.mark.tc_desc("Reset Transaction History")
def test_reset_transaction_history(driver):

    try:

        driver.get(
            "https://www.globalsqa.com/angularJs-protractor/BankingProject/"
        )

        customer1 = TEST_DATA["Customer1"]
        amount1 = TEST_DATA["Amount1"]

        login_page = LoginPage(driver)

        login_page.click_customer_login()
        login_page.select_customer(customer1)
        login_page.click_login()
    
        dashboard = CustomerDashboard(driver)

        time.sleep(1)
        dashboard.click_transaction_history()

        history = TransactionHistory(driver)
        history.click_reset_button()
        history.verify_transaction_history_empty()
        history.click_back_button()

        dashboard.verify_balance_empty()

    except Exception as e:

        raise AssertionError(
            f"Reset Transaction History failed. Reason: {str(e)}"
        )