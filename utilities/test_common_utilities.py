import utilities.secret_config
from pom.test_login_sso import Login_sso

class common_utilities:
    def __init__(self,page):
        self.page = page


    def test_navigate_to_page(self,url):
        self.page.goto(url)
        loginsso=Login_sso(self.page)
        loginsso.test_login(utilities.secret_config.USERNAME,utilities.secret_config.PASSWORD)