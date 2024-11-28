class test_overview_tab:
    def __init__(self,page):
        self.page = page
        self.pagesplit = page.locator("//mat-icon[text()='vertical_split']");
        self.discardChanges = page.get_by_text('Discard changes',exact=True);
        self.update = page.get_by_text('Update', exact=True);
        self.assignBtn = page.get_by_role('button', name=' Assign ', exact=True);
        self.selectcrew = page.get_by_text('Select crew', exact=True);
        self.confirmOpen = page.get_by_role('button', name= 'Confirm open', exact=True);



    def test_assign_crew(self,crewId):
        self.page.wait_for_timeout(timeout=6000)
        self.selectcrew.click()
        self.page.wait_for_timeout(timeout=10000)
        self.page.get_by_role('option', name= crewId, exact=False).click()
        self.assignBtn.scroll_into_view_if_needed()
        self.assignBtn.click()