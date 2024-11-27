from playwright.sync_api import expect


class order_page_elements:

    def __init__(self, page):
        self.page = page
        self.applyBtn=page.get_by_role("button", name="Apply")
        self.placeorderBtn=page.get_by_role("button", name="Place Order")
        self.selectCountry=page.get_by_role("combobox")
        self.procedBtn=page.get_by_role("button", name="Proceed")
        self.termsconditions=page.get_by_role("checkbox")
        self.promocodetxtbox=page.get_by_placeholder("Enter promo code")
        self.promoinfo=page.locator(".promoInfo")

    def test_proceedCheckout(self,country):
        self.promocodetxtbox.wait_for()
        self.promocodetxtbox.click()
        self.promocodetxtbox.fill("kiran")
        self.applyBtn.click()
        self.promoinfo.wait_for()
        expect(self.promoinfo).to_have_text("Invalid code ..!")
        self.promocodetxtbox.clear()
        self.promocodetxtbox.click()
        self.promocodetxtbox.fill("rahulshettyacademy")
        self.applyBtn.click()
        self.promoinfo.wait_for()
        expect(self.promoinfo).to_have_text("Code applied ..!")
        self.placeorderBtn.click()
        self.selectCountry.wait_for()
        self.selectCountry.select_option(country)
        self.termsconditions.check()
        self.procedBtn.click()