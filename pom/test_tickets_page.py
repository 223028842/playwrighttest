class test_tickets_page:
    def __init__(self,page):
        self.page = page
        self.pagesplit = page.locator("//mat-icon[text()='vertical_split']");
        self.discardChanges = page.get_by_text('Discard changes', exact=True);
        self.update = page.get_by_text('Update',exact=True);
        self.crewTab = page.get_by_text('Crew', exact=True);
        self.overviewTab = page.get_by_text('Overview', exact=True);
        self.customersTab = page.get_by_text('Customers', exact=True);
        self.meteranalysisTab = page.get_by_text('Meter analysis', exact=True);
        self.restorationTab = page.get_by_text('Restoration', exact=True);
        self.chronologyTab = page.get_by_text('Chronology', exact=True);
        self.assignCrew = page.get_by_text(' Assign Crew ', exact=True);





