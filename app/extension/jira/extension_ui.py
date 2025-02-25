import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login
from extension.jira.extension_pages import ProjectList, ProjectComplianceSettings, AuditProject
from util.conf import JIRA_SETTINGS

def admin_login(webdriver, username='admin', password='admin'):
    login_page = Login(webdriver)
    login_page.delete_all_cookies()
    login_page.go_to()
    login_page.set_credentials(username=username, password=password)
    
    # Handling first login setup steps if necessary
    if login_page.is_first_login():
        login_page.first_login_setup()
    if login_page.is_first_login_second_page():
        login_page.first_login_second_page_setup()
    
    # Wait until the page has loaded after login
    login_page.wait_for_page_loaded()

def ctc_view_projects(webdriver, datasets):    
    page = BasePage(webdriver)

    admin_login(webdriver)
    project_list_page = ProjectList(webdriver)
    
    @print_timing("selenium_ctc_view_projects_action")
    def measure():
        project_list_page.go_to()
        project_list_page.wait_for_page_loaded()

    measure()

def ctc_view_project_compliance_settings(webdriver, datasets):
    page = BasePage(webdriver)

    admin_login(webdriver)
    project_compliance_settings = ProjectComplianceSettings(webdriver, project_key=datasets['current_session']['project_key'])

    @print_timing("ctc_view_project_compliance_settings")
    def measure():
        project_compliance_settings.go_to()
        project_compliance_settings.wait_for_compliance_settings_loaded()

    measure()    

def ctc_view_project_audit_history(webdriver, datasets):
    page = BasePage(webdriver)

    admin_login(webdriver)
    project_audit_page = AuditProject(webdriver, project_key=datasets['current_session']['project_key'])

    @print_timing("ctc_view_project_audit_history")
    def measure():
        project_audit_page.go_to()
        project_audit_page.wait_for_audit_list()

    measure()  

def ctc_view_project_audit_history_details(webdriver, datasets):
    page = BasePage(webdriver)

    admin_login(webdriver)
    project_audit_page = AuditProject(webdriver, project_key=datasets['current_session']['project_key'])

    @print_timing("ctc_view_project_audit_history_details")
    def measure():
        project_audit_page.go_to()
        project_audit_page.wait_for_audit_list()
        project_audit_page.view_audit_history()

    measure()       

def ctc_configure_compliance_settings_and_complete_audit(webdriver, datasets):
    page = BasePage(webdriver)

    admin_login(webdriver)
    project_key = datasets['current_session']['project_key']
    project_compliance_settings = ProjectComplianceSettings(webdriver, project_key=project_key)
    project_audit_page = AuditProject(webdriver, project_key=project_key)

    @print_timing("ctc_configure_compliance_settings_and_complete_audit")
    def measure():

        project_compliance_settings.go_to()
        project_compliance_settings.wait_for_compliance_settings_loaded()

        project_compliance_settings.set_compliance_owner()
        project_compliance_settings.set_compliance_type()
        project_compliance_settings.set_audit_frequency()
        project_compliance_settings.set_audit_configuration()        
        project_compliance_settings.save_audit_configuration()

        project_audit_page.go_to()
        project_audit_page.wait_for_audit_list()      
          
        project_audit_page.complete_new_audit()

    measure()        