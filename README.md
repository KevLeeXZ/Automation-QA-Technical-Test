# Automation-QA-Technical-Test
Public Repo for Automation QA Technical Test based on XYZ Bank Application
Using Selenium with Pytest framework

## Installation
Clone the repository

```bash
git clone <repo>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run all tests

```bash
pytest
```

Generate HTML report

```bash
pytest -v --html=reports/report.html --self-contained-html --css=reports/assets.css
```

## Framework Design
The framework follows the Page Object Model (POM).

- Tests contain only test logic.
- Page Objects contain UI interactions.
- Helper classes provide reusable Selenium functions.
- Excel stores reusable test data.

## Test Data
Test data is stored in `TestCase.xlsx`.

Instead of hardcoding values inside scripts, test cases reference keys.

Example:

| Key | Value |
|-----|-------|
| Customer1 | Hermione Granger |
| Currency1 | Dollar |

This allows test data to be updated without modifying automation scripts.
