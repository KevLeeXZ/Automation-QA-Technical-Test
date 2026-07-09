import pytest
from pages.login import LoginPage
from pages.customer_dashboard import CustomerDashboard
from utils.excel_reader import read_test_data


TEST_DATA = read_test_data(
    "TestCase.xlsx"
)

@pytest.mark.tc_id("LGN007")
@pytest.mark.tc_desc("Login as Customer")
def test_customer_login(driver):

    try:

        driver.get(
            "https://www.globalsqa.com/angularJs-protractor/BankingProject/"
        )

        customer1 = TEST_DATA["Customer1"]
        customer2 = TEST_DATA["Customer2"]

        login_page = LoginPage(driver)

        login_page.click_customer_login()

        login_page.select_customer(
            customer1
        )

        login_page.click_login()
    
        dashboard = CustomerDashboard(driver)

        dashboard.verify_customer_displayed(customer2)


    except Exception as e:

        raise AssertionError(
            f"Customer login test failed. Reason: {str(e)}"
        )