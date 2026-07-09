from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException


class SeleniumHelper:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(
            driver,
            timeout
        )


    def find_element(self, locator):

        try:
            return self.wait.until(
                EC.presence_of_element_located(locator)
            )

        except Exception as e:
            raise Exception(
                f"Unable to locate element {locator}. "
                f"Timeout after waiting. Error: {str(e)}"
            )

    def find_elements(self, locator):

        try:

            elements = self.wait.until(
                EC.presence_of_all_elements_located(locator)
            )
            return elements

        except TimeoutException:

            raise Exception(
                f"Unable to locate elements {locator}. "
                f"No matching elements found."
            )
        
    def click_element(self, locator):

        try:
            element = self.wait.until(
                EC.element_to_be_clickable(locator)
            )

            element.click()

        except Exception as e:
            raise Exception(
                f"Unable to click element {locator}. "
                f"Element may not be clickable. Error: {str(e)}"
            )


    def enter_text(self, locator, text):

        try:
            element = self.find_element(locator)

            element.clear()
            element.send_keys(text)

        except Exception as e:
            raise Exception(
                f"Unable to enter text '{text}' "
                f"into element {locator}. Error: {str(e)}"
            )


    def get_text(self, locator):

        try:
            element = self.find_element(locator)

            return element.text

        except Exception as e:
            raise Exception(
                f"Unable to retrieve text from {locator}. "
                f"Error: {str(e)}"
            )
        
    def element_exists(self, locator, timeout=5):

        try:

            WebDriverWait(
                self.driver,
                timeout
            ).until(
                EC.presence_of_element_located(locator)
            )

            return True

        except TimeoutException:

            return False
        
    def get_table_headers(self, locator):

        headers = self.find_elements(locator)

        return [
            header.text.strip()
            for header in headers
        ]
    
    def get_column_index(self, locator, column_name):

        headers = self.get_table_headers(locator)

        try:

            return headers.index(
                column_name
            )

        except ValueError:

            raise Exception(
                f"Column '{column_name}' "
                f"not found. Available columns: {headers}"
            )
        
    def get_element_count(self, locator):

        return len(
            self.driver.find_elements(
                *locator
            )
        )
    
    def get_alert_text(self, timeout=5):

        try:

            alert = WebDriverWait(
                self.driver,
                timeout
            ).until(
                lambda d: d.switch_to.alert
            )

            return alert.text


        except TimeoutException:

            raise Exception(
                "Timed out waiting for browser alert."
            )

    def accept_alert(self):

        try:

            alert = self.driver.switch_to.alert
            alert.accept()

        except NoAlertPresentException:

            raise Exception(
                "Unable to accept alert. "
                "No browser alert found."
            )