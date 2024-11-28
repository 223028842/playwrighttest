from _pyrepl import console
from playwright.sync_api import expect


class test_all_tickets_page:
    def __init__(self,page):
        self.page = page
        self.Tickets = page.get_by_text('Tickets',exact=True)
        self.All = page.get_by_text('All', exact=True)
        self.SearchIcon = page.locator("//*[text()='search']").last
        self.SearchText = page.locator("//input[@placeholder='Search']").last
        self.devicename = page.locator("//div[@col-id='originaldevicenameid']").last
        self.backarrow = page.locator(".nav-back-icon")


    def test_search_open_ticket(self,devicename):
        self.Tickets.click()
        self.All.click()
        self.page.wait_for_timeout(timeout=3000)
        self.backarrow.click()
        self.SearchIcon.click()
        self.SearchText.fill(devicename)
        self.page.keyboard.press('Enter');
        self.page.get_by_role('row').first
        originaldevicename = self.devicename.text_content(timeout=30000)
        print(originaldevicename)
        #expect(originaldevicename, devicename)
        self.page.locator("//div[@col-id='ordername']").last.dblclick()