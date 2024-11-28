import time
import playwright
import pytest
from playwright.sync_api import Playwright
from pytest_playwright.pytest_playwright import browser
import utilities.secret_config
from utilities.test_common_utilities import common_utilities

@pytest.fixture(scope="session")
#def setup(browser):
def context_creation(playwright):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(ignore_https_errors=True,no_viewport=True)
    page=context.new_page()

    commonutilities =common_utilities(page)
    commonutilities.test_navigate_to_page()

    yield context
    time.sleep(5)

@pytest.fixture()
def login_set_up(context_creation,playwright):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(storage_state='auth_state.json',ignore_https_errors=True,no_viewport=True)
    page= context.new_page()

    yield page
    time.sleep(5)
    browser.close()

