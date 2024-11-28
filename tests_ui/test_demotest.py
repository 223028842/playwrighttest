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
@pytest.mark.skip
def test_greenkart_app(setup,fruit,country) -> None:
    page= setup
    page.wait_for_url("https://rahulshettyacademy.com/seleniumPractise/#/")
    homepage=HomePage(page)
    homepage.test_select_product(fruit)

    orderpage=order_page_elements(page)
    orderpage.test_proceedCheckout(country)

#@pytest.mark.skip(reason="not ready")
#@pytest.mark.xfail(reason="url is not ready")
@pytest.mark.sanity
@pytest.mark.skip
def test_greenkart_app_1(setup) -> None:

    page= setup
    page.wait_for_url("https://rahulshettyacademy.com/seleniumPractise/#/")
    homepage=HomePage(page)
    homepage.test_select_product("banana")







