import os
from datetime import datetime

import pytest
import pytest_html

from utils.driver_factory import create_driver


@pytest.fixture
def driver():

    browser = create_driver()

    yield browser

    browser.quit()


def pytest_html_report_title(report):
    report.title = "XYZ Bank Automation Report"

def pytest_html_results_table_header(cells):
    cells.insert(1, "<th>Test Case ID</th>")
    cells.insert(2, "<th>Description</th>")

def pytest_html_results_table_row(report, cells):

    tc_id = getattr(report, "tc_id", "")
    tc_desc = getattr(report, "tc_desc", "")

    cells.insert(1, f"<td>{tc_id}</td>")
    cells.insert(2, f"<td>{tc_desc}</td>")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extras", [])

    marker = item.get_closest_marker("tc_id")
    if marker:
        report.tc_id = marker.args[0]

    marker = item.get_closest_marker("tc_desc")
    if marker:
        report.tc_desc = marker.args[0]

    # Only capture screenshot if test execution failed
    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            screenshot = driver.get_screenshot_as_base64()

            extra.append(
                pytest_html.extras.png(screenshot)
            )

    report.extras = extra