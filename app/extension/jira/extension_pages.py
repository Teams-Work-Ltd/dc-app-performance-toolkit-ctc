from selenium.webdriver.common.keys import Keys
from selenium_ui.conftest import retry

from selenium_ui.base_page import BasePage

from extension.jira.extension_selectors import UrlManager, ProjectComplianceSettingsPageLocators, ProjectListPageLocators, AuditProjectLocators

class ProjectList(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        url_manager = UrlManager()
        self.page_url = url_manager.project_list_url()

    def wait_for_page_loaded(self):
        self.wait_until_any_ec_presented(
            selectors=[ProjectListPageLocators.project_table, ProjectListPageLocators.project_table_loaded])

class ProjectComplianceSettings(BasePage):
    page_loaded_selector = None

    def __init__(self, driver, project_key):
        BasePage.__init__(self, driver)
        self.locators = ProjectComplianceSettingsPageLocators(project_key)
        self.page_url = self.locators.project_compliance_url
        ProjectComplianceSettings.page_loaded_selector = self.locators.compliance_page_settings_ready

    def wait_for_compliance_settings_loaded(self):
        self.wait_until_visible(self.locators.compliance_page_settings_ready)

    def set_compliance_owner(self):
        self.wait_until_clickable(self.locators.compliance_owner_select)
        self.get_element(self.locators.compliance_owner_select).send_keys(Keys.CONTROL + "a")
        self.get_element(self.locators.compliance_owner_select).send_keys(Keys.BACKSPACE)
        self.get_element(self.locators.compliance_owner_select).send_keys("admin")
        self.wait_until_clickable(self.locators.compliance_owner_select_admin).click()

    def set_compliance_type(self):
        self.wait_until_clickable(self.locators.compliance_type_select)
        self.get_element(self.locators.compliance_type_select).click()
        self.wait_until_clickable(self.locators.compliance_type_select_confidential).click()

    def set_compliance_categories(self):
        self.wait_until_clickable(self.locators.compliance_categories_select)
        self.get_element(self.locators.compliance_categories_select).click()

        remove_button = self.get_element(self.locators.compiance_category_financial_reporting_remove)
        if remove_button.is_displayed():
            remove_button.click()

        self.get_element(self.locators.compliance_category_financial_reporting).click()

    def set_audit_frequency(self):
        self.wait_until_clickable(self.locators.audit_frequency_select)  
        self.get_element(self.locators.audit_frequency_select).click()      
        self.wait_until_clickable(self.locators.audit_frequency_ad_hoc).click()

    def set_audit_configuration(self):
        checkbox = self.get_element(self.locators.compliance_configuration_gdpr)
        if not checkbox.is_selected():
            checkbox.click()

    def save_audit_configuration(self):
        self.get_element(self.locators.save_project_compliance_button).click()
        self.wait_until_visible(self.locators.save_success_message)


class AuditProject(BasePage):

    def __init__(self, driver, project_key):
        BasePage.__init__(self, driver)
        self.locators = AuditProjectLocators(project_key)
        self.page_url = self.locators.audit_project_url

    def wait_for_audit_list(self):
        self.wait_until_visible(self.locators.audit_list_page_ready)

    def view_audit_history(self):
        self.get_element(self.locators.audit_history_button).click()
        self.wait_until_visible(self.locators.audit_history_table)

    def complete_new_audit(self):
        text_summary = f"This is the latest audit - {self.generate_random_string(50)}"
        self.get_element(self.locators.new_audit_button).click()
        self.wait_until_visible(self.locators.new_audit_form_ready)
        
        # Complete the audit form.
        self.get_element(self.locators.dpo_radio_option).click()
        self.get_element(self.locators.dpo_evidence_field).send_keys("Evidence dpo")
        self.get_element(self.locators.written_data_protection_policy_radio_option).click()
        self.get_element(self.locators.written_data_protection_policy_evidence_field).send_keys("Evidence written data protection policy")
        self.get_element(self.locators.senior_manager_gdpr_radio_option).click()
        self.get_element(self.locators.senior_manager_gdpr_evidence_field).send_keys("Evidence senior manager gdpr")

        self.get_element(self.locators.gdpr_compliance_document_radio_option).click()
        self.get_element(self.locators.gdpr_compliance_document_evidence_field).send_keys("Evidence for gdpr_compliance_document")

        self.get_element(self.locators.gdpr_compliance_review_radio_option).click()
        self.get_element(self.locators.gdpr_compliance_review_evidence_field).send_keys("Evidence for gdpr_compliance_review")

        self.get_element(self.locators.gdpr_compliance_log_radio_option).click()
        self.get_element(self.locators.gdpr_compliance_log_evidence_field).send_keys("Evidence for gdpr_compliance_log")

        self.get_element(self.locators.data_protection_roles_radio_option).click()
        self.get_element(self.locators.data_protection_roles_evidence_field).send_keys("Evidence for data_protection_roles")

        self.get_element(self.locators.data_protection_impact_assessments_radio_option).click()
        self.get_element(self.locators.data_protection_impact_assessments_evidence_field).send_keys("Evidence for data_protection_impact_assessments")

        self.get_element(self.locators.other_controllers_radio_option).click()
        self.get_element(self.locators.other_controllers_evidence_field).send_keys("Evidence for other_controllers")

        self.get_element(self.locators.personal_data_identified_radio_option).click()
        self.get_element(self.locators.personal_data_identified_evidence_field).send_keys("Evidence for personal_data_identified")

        self.get_element(self.locators.record_of_processing_activities_radio_option).click()
        self.get_element(self.locators.record_of_processing_activities_evidence_field).send_keys("Evidence for record_of_processing_activities")

        self.get_element(self.locators.data_movement_diagram_radio_option).click()
        self.get_element(self.locators.data_movement_diagram_evidence_field).send_keys("Evidence for data_movement_diagram")

        self.get_element(self.locators.data_inventory_radio_option).click()
        self.get_element(self.locators.data_inventory_evidence_field).send_keys("Evidence for data_inventory")

        self.get_element(self.locators.third_party_data_flows).click()
        self.get_element(self.locators.third_party_data_flows_evidence_field).send_keys("Evidence for third_party_data_flows")

        self.get_element(self.locators.data_inventory_audits_radio_option).click()
        self.get_element(self.locators.data_inventory_audits_evidence_field).send_keys("Evidence for data_inventory_audits")

        self.get_element(self.locators.uk_specific_exemptions_radio_option).click()
        self.get_element(self.locators.uk_specific_exemptions_evidence_field).send_keys("Evidence for uk_specific_exemptions")

        self.get_element(self.locators.legal_reason_radio_option).click()
        self.get_element(self.locators.legal_reason_evidence_field).send_keys("Evidence for legal_reason")

        self.get_element(self.locators.consent_collected_radio_option).click()
        self.get_element(self.locators.consent_collected_evidence_field).send_keys("Evidence for consent_collected")

        self.get_element(self.locators.individual_rights_radio_option).click()
        self.get_element(self.locators.individual_rights_evidence_field).send_keys("Evidence for individual_rights")

        self.get_element(self.locators.individual_consents_radio_option).click()
        self.get_element(self.locators.individual_consents_evidence_field).send_keys("Evidence for individual_consents")

        self.get_element(self.locators.legitimate_interests_radio_option).click()
        self.get_element(self.locators.legitimate_interests_evidence_field).send_keys("Evidence for legitimate_interests")

        self.get_element(self.locators.explicit_consent_radio_option).click()
        self.get_element(self.locators.explicit_consent_evidence_field).send_keys("Evidence for explicit_consent")

        self.get_element(self.locators.privacy_notices_radio_option).click()
        self.get_element(self.locators.privacy_notices_evidence_field).send_keys("Evidence for privacy_notices")

        self.get_element(self.locators.minimum_data_processing_radio_option).click()
        self.get_element(self.locators.minimum_data_processing_evidence_field).send_keys("Evidence for minimum_data_processing")

        self.get_element(self.locators.personal_data_checked_radio_option).click()
        self.get_element(self.locators.personal_data_checked_evidence_field).send_keys("Evidence for personal_data_checked")

        self.get_element(self.locators.corrective_systems_radio_option).click()
        self.get_element(self.locators.corrective_systems_evidence_field).send_keys("Evidence for corrective_systems")

        self.get_element(self.locators.redundant_data_processes_radio_option).click()
        self.get_element(self.locators.redundant_data_processes_evidence_field).send_keys("Evidence for redundant_data_processes")

        self.get_element(self.locators.encryption_and_firewalls_radio_option).click()
        self.get_element(self.locators.encryption_and_firewalls_evidence_field).send_keys("Evidence for encryption_and_firewalls")

        self.get_element(self.locators.access_controls_radio_option).click()
        self.get_element(self.locators.access_controls_evidence_field).send_keys("Evidence for access_controls")

        self.get_element(self.locators.regular_security_audits_radio_option).click()
        self.get_element(self.locators.regular_security_audits_evidence_field).send_keys("Evidence for regular_security_audits")

        self.get_element(self.locators.software_up_to_date_radio_option).click()
        self.get_element(self.locators.software_up_to_date_evidence_field).send_keys("Evidence for software_up_to_date")

        self.get_element(self.locators.penetration_testing_radio_option).click()
        self.get_element(self.locators.penetration_testing_evidence_field).send_keys("Evidence for penetration_testing")

        self.get_element(self.locators.third_party_reviews_radio_option).click()
        self.get_element(self.locators.third_party_reviews_evidence_field).send_keys("Evidence for third_party_reviews")

        self.get_element(self.locators.anonymised_personal_data_radio_option).click()
        self.get_element(self.locators.anonymised_personal_data_evidence_field).send_keys("Evidence for anonymised_personal_data")

        self.get_element(self.locators.data_change_requests_radio_option).click()
        self.get_element(self.locators.data_change_requests_evidence_field).send_keys("Evidence for data_change_requests")

        self.get_element(self.locators.portable_data_radio_option).click()
        self.get_element(self.locators.portable_data_evidence_field).send_keys("Evidence for portable_data")

        self.get_element(self.locators.identity_checks_radio_option).click()
        self.get_element(self.locators.identity_checks_evidence_field).send_keys("Evidence for identity_checks")

        self.get_element(self.locators.response_times_radio_option).click()
        self.get_element(self.locators.response_times_evidence_field).send_keys("Evidence for response_times")

        self.get_element(self.locators.objection_handling_radio_option).click()
        self.get_element(self.locators.objection_handling_evidence_field).send_keys("Evidence for objection_handling")

        self.get_element(self.locators.retention_policy_radio_option).click()
        self.get_element(self.locators.retention_policy_evidence_field).send_keys("Evidence for retention_policy")

        self.get_element(self.locators.personal_data_deleted_radio_option).click()
        self.get_element(self.locators.personal_data_deleted_evidence_field).send_keys("Evidence for personal_data_deleted")

        self.get_element(self.locators.automated_retention_rules_radio_option).click()
        self.get_element(self.locators.automated_retention_rules_evidence_field).send_keys("Evidence for automated_retention_rules")

        self.get_element(self.locators.third_party_dpa_radio_option).click()
        self.get_element(self.locators.third_party_dpa_evidence_field).send_keys("Evidence for third_party_dpa")

        self.get_element(self.locators.gdpr_data_transfer_rules_radio_option).click()
        self.get_element(self.locators.gdpr_data_transfer_rules_evidence_field).send_keys("Evidence for gdpr_data_transfer_rules")

        self.get_element(self.locators.third_party_processor_review_radio_option).click()
        self.get_element(self.locators.third_party_processor_review_evidence_field).send_keys("Evidence for third_party_processor_review")

        self.get_element(self.locators.third_party_written_agreements_radio_option).click()
        self.get_element(self.locators.third_party_written_agreements_evidence_field).send_keys("Evidence for third_party_written_agreements")

        self.get_element(self.locators.data_breach_management_radio_option).click()
        self.get_element(self.locators.data_breach_management_evidence_field).send_keys("Evidence for data_breach_management")

        self.get_element(self.locators.data_breach_reporting_radio_option).click()
        self.get_element(self.locators.data_breach_reporting_evidence_field).send_keys("Evidence for data_breach_reporting")

        self.get_element(self.locators.data_breach_training_radio_option).click()
        self.get_element(self.locators.data_breach_training_evidence_field).send_keys("Evidence for data_breach_training")

        self.get_element(self.locators.data_breach_communication_radio_option).click()
        self.get_element(self.locators.data_breach_communication_evidence_field).send_keys("Evidence for data_breach_communication")

        self.get_element(self.locators.gdpr_training_radio_option).click()
        self.get_element(self.locators.gdpr_training_evidence_field).send_keys("Evidence for gdpr_training")

        self.get_element(self.locators.internal_processes_radio_option).click()
        self.get_element(self.locators.internal_processes_evidence_field).send_keys("Evidence for internal_processes")

        self.get_element(self.locators.gdpr_training_updated_radio_option).click()
        self.get_element(self.locators.gdpr_training_updated_evidence_field).send_keys("Evidence for gdpr_training_updated")

        self.get_element(self.locators.gdpr_training_staff_radio_option).click()
        self.get_element(self.locators.gdpr_training_staff_evidence_field).send_keys("Evidence for gdpr_training_staff")

        self.get_element(self.locators.new_audit_next_button).click()

        # Complete the audit notes.
        self.wait_until_visible(self.locators.new_audit_note_label)
        self.get_element(self.locators.new_audit_note_field).send_keys(text_summary)
        self.get_element(self.locators.new_audit_signature_field).send_keys("John Doe")
        self.get_element(self.locators.new_audit_next_button).click()

        # Complete the audit.
        self.get_element(self.locators.new_audit_complete_button).click()
        self.wait_until_visible(self.locators.audit_complete_message)
        
