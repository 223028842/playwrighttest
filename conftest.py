import pytest
from playwright.sync_api import Playwright
from utilities.test_common_utilities import common_utilities

@pytest.fixture
def setup(page):
    # browser = playwright.chromium.launch(headless=False,slow_mo=500)#slow_mo is to slow down the execution and show it demo people
    # context = browser.new_context()
    # page=context.new_page()
    commonutilities =common_utilities(page)
    commonutilities.test_navigate_to_page("https://rahulshettyacademy.com/seleniumPractise/#/")

    yield page