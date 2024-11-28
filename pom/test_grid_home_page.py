from tkinter.font import names

from playwright.async_api import Page

class test_grid_home_page:
    def __init__(self,page):
        self.page = page


    def test_select_view(self,viewoption):
        self.page.get_by_role('combobox').wait_for()
        self.page.get_by_role('combobox').click()
        self.page.get_by_role('option',name=viewoption).click()


