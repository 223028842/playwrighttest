import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from pom.test_login_sso import Login_sso
from pom.test_home_page_elements import HomePage
from pom.test_order_page_elements import order_page_elements
from utilities.test_common_utilities import  common_utilities

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("fruit",["banana","pumpkin","orange"])
@pytest.mark.parametrize("country",["India","Angola","Morocco"])
def test_greenkart_app(setup,fruit,country) -> None:
    # browser = playwright.chromium.launch(headless=False,slow_mo=500)#slow_mo is to slow down the execution and show it demo people
    # context = browser.new_context()
    # page=context.new_page()
    # commonutilities =common_utilities(page)
    # commonutilities.test_navigate_to_page("https://rahulshettyacademy.com/seleniumPractise/#/")
    #for comment code shortcut-Ctrl+K Ctrl+C
    page= setup
    page.wait_for_url("https://rahulshettyacademy.com/seleniumPractise/#/")
    homepage=HomePage(page)
    homepage.test_select_product(fruit)

    orderpage=order_page_elements(page)
    orderpage.test_proceedCheckout(country)

    # # ---------------------
    # context.close()
    # browser.close()

#@pytest.mark.skip(reason="not ready")
#@pytest.mark.xfail(reason="url is not ready")
@pytest.mark.sanity
def test_greenkart_app_1(setup) -> None:
    # browser = playwright.chromium.launch(headless=False,slow_mo=500)#slow_mo is to slow down the execution and show it demo people
    # context = browser.new_context()
    # page=context.new_page()
    # commonutilities =common_utilities(page)
    # commonutilities.test_navigate_to_page("https://rahulshettyacademy.com/seleniumPractise/#/")
    #for comment code shortcut-Ctrl+K Ctrl+C
    page= setup
    page.wait_for_url("https://rahulshettyacademy.com/seleniumPractise/#/")
    homepage=HomePage(page)
    homepage.test_select_product("banana")

    # ---------------------
    # context.close()
    # browser.close()
# with sync_playwright() as playwright:
#     test_greenkart_app(playwright)






