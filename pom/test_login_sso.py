class Login_sso:
    def __init__(self,page):
        self.page = page
        self.usname=page.get_by_label("Enter SSO ID")
        self.nxtBtn=  page.get_by_role("button", name="Next")
        self.pswd= page.get_by_label("Enter password")
        self.logInBtn= page.get_by_role("button", name="Log In & Remember Me")

    def test_login(self,username,password):
        if self.usname.is_visible():
            self.usname.click()
            self.usname.fill(username)
            self.nxtBtn.click()
            self.pswd.click()
            self.pswd.fill(password)
            self.logInBtn.click()

