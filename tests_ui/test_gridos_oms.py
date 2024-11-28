import pytest
from pom.test_grid_home_page import test_grid_home_page
from pom.test_all_tickets_page import test_all_tickets_page
from pom.test_tickets_page import test_tickets_page
from pom.test_overview_tab import test_overview_tab
import utilities.secret_config

@pytest.mark.parametrize("devicename,crewId",[("6-7412-8173-0-1"," Carino (1207), Local Lineman ")])
def test_gridos_oms(login_set_up,devicename,crewId):

    page=login_set_up
    page.goto(utilities.secret_config.APPURL)

    homepage= test_grid_home_page(page)
    homepage.test_select_view(' Network viewer ')

    #develop code to automate an API

    homepage.test_select_view(' Workstation ')

    allticketspage = test_all_tickets_page(page)
    allticketspage.test_search_open_ticket(devicename)

    ticketpage=test_tickets_page(page)
    ticketpage.overviewTab.click()

    overviewtab = test_overview_tab(page)
    overviewtab.test_assign_crew(crewId)


@pytest.mark.parametrize("devicename,crewId",[("6-7412-7054-0-5"," Carino (1207), Local Lineman ")])
def test_demo_workflow(login_set_up,devicename,crewId):
    page=login_set_up
    page.goto(utilities.secret_config.APPURL)

    homepage = test_grid_home_page(page)
    homepage.test_select_view(' Workstation ')

    allticketspage = test_all_tickets_page(page)
    allticketspage.test_search_open_ticket(devicename)

    ticketpage = test_tickets_page(page)
    ticketpage.overviewTab.click()

    overviewtab = test_overview_tab(page)
    overviewtab.test_assign_crew(crewId)







