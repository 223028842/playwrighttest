from playwright.sync_api import expect


class HomePage:
    def __init__(self, page):
        self.page = page
        self.vegsearch= page.get_by_placeholder("Search for Vegetables and")
        self.products = page.locator('.product').all()
        self.addtocartBtn = page.get_by_role("button", name="ADD TO CART")
        self.cartIcon =page.get_by_role("link", name="Cart")
        self.procedcheckoutBtn = page.get_by_role("button", name="PROCEED TO CHECKOUT")

    def test_select_product(self,productname):
        self.vegsearch.wait_for()
        for product in self.products:
            print(product.text_content())
            if product.text_content().lower().__contains__(productname):
                product.scroll_into_view_if_needed()
                product.get_by_role("button", name="ADD TO CART").click()
                break
        expect(self.cartIcon).to_be_visible()
        self.cartIcon.click()
        self.procedcheckoutBtn.click()