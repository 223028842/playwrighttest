import json
import os
import time

import pytest
from playwright.sync_api import expect
import utilities.secret_config

class test_grid_login:
    def __init__(self,page):
        self.page = page
        self.usernametxt = page.get_by_label('Username *')
        self.passwordtxt = page.get_by_label('Credentials *')
        self.domain=page.get_by_label('Domain')
        self.domainoption=page.get_by_role('option', name= utilities.secret_config.DOMAIN)
        self.nextbtn=page.get_by_role('button', name= 'Next')
        self.loginbtn=page.get_by_role('button', name='Login')

    def test_login(self):
        self.page.goto(utilities.secret_config.APPURL)
        #self.page.set_default_timeout(3000)
        self.usernametxt.fill(utilities.secret_config.USER)
        self.domain.locator('div').nth(2).click()
        self.domainoption.click()
        self.nextbtn.click()
        self.passwordtxt.fill(utilities.secret_config.PASS)
        self.loginbtn.click()
        expect(self.page).to_have_title('GridOS ADMS')
        self.page.wait_for_load_state(timeout=3000)
        time.sleep(2)
        # Save the authentication state (cookies, local storage, etc.)
        self.page.context.storage_state(path='auth_state.json')
        #storage_state =  self.page.context.storage_state()

        # Save the state to a file at the project path
        # with open("auth_state.json", "w") as f:
        #     json.dump(storage_state, f)

        #self.page.context().storageState(path= 'authentication.json')
