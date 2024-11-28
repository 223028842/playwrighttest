from pydoc import pager

import utilities.secret_config
from pom.test_login_sso import Login_sso
from pom.test_grid_login import test_grid_login

class common_utilities:
    def __init__(self,page):
        self.page   =page


    def test_navigate_to_page(self):
        grid_login=test_grid_login(self.page)
        grid_login.test_login()
