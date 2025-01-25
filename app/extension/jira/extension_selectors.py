from selenium.webdriver.common.by import By
from util.conf import JIRA_SETTINGS

class UrlManager:
    def __init__(self, project_key=None, projects_list_page=None, goals_list_page=None):
        self.host = JIRA_SETTINGS.server_url
        self.project_list = '/secure/CatAuditProjects.jspa'
        self.project_compliance_settings = 'selectedItem=com.teamswork.compliance.cat-the-compliant-plugin:cat-compliance-project-settings-ca19'
        self.audit_project = 'selectedItem=com.teamswork.compliance.cat-the-compliant-plugin:cat-the-compliant-project-audit-88c9'

    def audit_project_url(self, project_key):
        return f"{self.host}/projects/{project_key}?{self.audit_project}"

    def project_list_url(self):
        return f"{self.host}{self.project_list}"

    def project_compliance_settings_url(self, project_key):
      return f"{self.host}/projects/{project_key}?{self.project_compliance_settings}"

class ProjectListPageLocators:
    project_list_url = UrlManager().project_list_url()
    search_project_name = (By.ID, "search-project-name")
    project_table = (By.ID, "audit-project-compliance-content-table-a2f4")
    project_table_loaded = (By.CLASS_NAME, "loaded")
    project_search_button = (By.ID, "search-projects-button")

class ProjectComplianceSettingsPageLocators:
    def __init__(self, project_key):
        url_manager = UrlManager()
        self.project_compliance_url = url_manager.project_compliance_settings_url(project_key)
        self.compliance_page_settings_ready = (By.ID, 'complianceOwner-label')
        self.compliance_owner_select = (By.CLASS_NAME, "fabric-user-picker__input")
        self.compliance_owner_select_admin = (By.ID, "react-select-complianceOwner-picker-field-option-0")
        self.compliance_type_select = (By.ID, 'complianceType')
        self.compliance_type_select_confidential = (By.ID, 'react-select-complianceType-option-6')
        self.compliance_categories_select = (By.ID, "complianceCategories")
        self.compliance_category_financial_reporting = (By.ID, 'react-select-complianceCategories-option-1')
        self.compiance_category_financial_reporting_remove = (By.XPATH, "//div[@aria-label='Remove Financial Reporting']")
        self.audit_frequency_select = (By.ID, "auditFrequency")
        self.audit_frequency_ad_hoc = (By.ID, 'react-select-auditFrequency-option-7')
        self.compliance_configuration_gdpr = (By.CSS_SELECTOR, 'input#complianceChecklist-option-GDPR')
        self.compliance_configuration_iso_27001 = (By.ID, "complianceChecklist-option-ISO_27001")
        self.compliance_coinfiguration_iso_20000 = (By.ID, "complianceChecklist-option-ISO_20000")
        self.save_project_compliance_button = (By.ID, "save-compliance-settings")
        self.save_success_message = (By.XPATH, "//div[@role='alert']//span[text()='Compliance settings updated successfully']")

class AuditProjectLocators:
    def __init__(self, project_key):
        self.audit_project_url = UrlManager().audit_project_url(project_key)
        self.audit_list_page_ready = (By.ID, 'audit-history-link')
        
        self.audit_history_button = (By.ID, 'audit-history-link')
        self.audit_history_table = (By.ID, 'audit-project-history-content-table-c9af')    

        self.dpo_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-0-0'][value='cyaml.y']")
        self.dpo_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-0-0')
        self.written_data_protection_policy_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-0-1'][value='cyaml.y']")
        self.written_data_protection_policy_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-0-1')
        self.senior_manager_gdpr_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-0-2'][value='cyaml.y']")
        self.senior_manager_gdpr_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-0-2')
        self.gdpr_compliance_document_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-0-3'][value='cyaml.y']")
        self.gdpr_compliance_document_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-0-3')
        self.gdpr_compliance_review_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-0-4'][value='cyaml.y']")
        self.gdpr_compliance_review_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-0-4')
        self.gdpr_compliance_log_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-0-5'][value='cyaml.y']")
        self.gdpr_compliance_log_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-0-5')
        self.data_protection_roles_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-0-6'][value='cyaml.y']")
        self.data_protection_roles_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-0-6')
        self.data_protection_impact_assessments_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-0-7'][value='cyaml.y']")
        self.data_protection_impact_assessments_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-0-7')
        self.other_controllers_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-0-8'][value='cyaml.y']")
        self.other_controllers_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-0-8')

        self.personal_data_identified_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-1-0'][value='cyaml.y']")
        self.personal_data_identified_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-1-0')
        self.record_of_processing_activities_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-1-1'][value='cyaml.y']")
        self.record_of_processing_activities_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-1-1')
        self.data_movement_diagram_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-1-2'][value='cyaml.y']")
        self.data_movement_diagram_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-1-2')
        self.data_inventory_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-1-3'][value='cyaml.y']")
        self.data_inventory_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-1-3')
        self.third_party_data_flows = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-1-4'][value='cyaml.y']")
        self.third_party_data_flows_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-1-4')
        self.data_inventory_audits_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-1-5'][value='cyaml.y']")
        self.data_inventory_audits_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-1-5')
        self.uk_specific_exemptions_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-1-6'][value='cyaml.y']")
        self.uk_specific_exemptions_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-1-6')

        self.legal_reason_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-2-0'][value='cyaml.y']")
        self.legal_reason_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-2-0')
        self.consent_collected_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-2-1'][value='cyaml.y']")
        self.consent_collected_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-2-1')
        self.individual_rights_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-2-2'][value='cyaml.y']")
        self.individual_rights_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-2-2')
        self.individual_consents_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-2-3'][value='cyaml.y']") 
        self.individual_consents_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-2-3')
        self.legitimate_interests_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-2-4'][value='cyaml.y']")
        self.legitimate_interests_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-2-4')
        self.explicit_consent_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-2-5'][value='cyaml.y']")
        self.explicit_consent_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-2-5')
        self.privacy_notices_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-2-6'][value='cyaml.y']") 
        self.privacy_notices_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-2-6')

        self.minimum_data_processing_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-3-0'][value='cyaml.y']")
        self.minimum_data_processing_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-3-0')
        self.personal_data_checked_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-3-1'][value='cyaml.y']")
        self.personal_data_checked_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-3-1')
        self.corrective_systems_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-3-2'][value='cyaml.y']")
        self.corrective_systems_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-3-2')
        self.redundant_data_processes_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-3-3'][value='cyaml.y']")
        self.redundant_data_processes_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-3-3')

        self.encryption_and_firewalls_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-4-0'][value='cyaml.y']")
        self.encryption_and_firewalls_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-4-0')
        self.access_controls_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-4-1'][value='cyaml.y']")
        self.access_controls_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-4-1')
        self.regular_security_audits_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-4-2'][value='cyaml.y']")
        self.regular_security_audits_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-4-2')
        self.software_up_to_date_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-4-3'][value='cyaml.y']")
        self.software_up_to_date_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-4-3')
        self.penetration_testing_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-4-4'][value='cyaml.y']")
        self.penetration_testing_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-4-4')
        self.third_party_reviews_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-4-5'][value='cyaml.y']")
        self.third_party_reviews_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-4-5')
        self.anonymised_personal_data_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-4-6'][value='cyaml.y']")
        self.anonymised_personal_data_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-4-6')

        self.data_change_requests_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-5-0'][value='cyaml.y']")
        self.data_change_requests_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-5-0')
        self.portable_data_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-5-1'][value='cyaml.y']")
        self.portable_data_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-5-1')
        self.identity_checks_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-5-2'][value='cyaml.y']")
        self.identity_checks_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-5-2')
        self.response_times_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-5-3'][value='cyaml.y']")
        self.response_times_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-5-3')
        self.objection_handling_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-5-4'][value='cyaml.y']")
        self.objection_handling_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-5-4')

        self.retention_policy_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-6-0'][value='cyaml.y']")
        self.retention_policy_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-6-0')
        self.personal_data_deleted_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-6-1'][value='cyaml.y']")
        self.personal_data_deleted_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-6-1')
        self.automated_retention_rules_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-6-2'][value='cyaml.y']")
        self.automated_retention_rules_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-6-2')

        self.third_party_dpa_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-7-0'][value='cyaml.y']")
        self.third_party_dpa_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-7-0')
        self.gdpr_data_transfer_rules_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-7-1'][value='cyaml.y']")
        self.gdpr_data_transfer_rules_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-7-1')
        self.third_party_processor_review_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-7-2'][value='cyaml.y']")
        self.third_party_processor_review_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-7-2')
        self.third_party_written_agreements_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-7-3'][value='cyaml.y']")
        self.third_party_written_agreements_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-7-3')

        self.data_breach_management_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-8-0'][value='cyaml.y']")
        self.data_breach_management_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-8-0')
        self.data_breach_reporting_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-8-1'][value='cyaml.y']")
        self.data_breach_reporting_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-8-1')
        self.data_breach_training_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-8-2'][value='cyaml.y']")
        self.data_breach_training_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-8-2')
        self.data_breach_communication_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-8-3'][value='cyaml.y']")
        self.data_breach_communication_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-8-3')

        self.gdpr_training_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-9-0'][value='cyaml.y']")
        self.gdpr_training_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-9-0')
        self.internal_processes_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-9-1'][value='cyaml.y']")
        self.internal_processes_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-9-1')
        self.gdpr_training_updated_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-9-2'][value='cyaml.y']")
        self.gdpr_training_updated_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-9-2')
        self.gdpr_training_staff_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-9-3'][value='cyaml.y']")
        self.gdpr_training_staff_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-9-3')

        self.new_audit_button = (By.ID, 'audit-project-wizard-start-btn-11a1')
        self.new_audit_form_ready = (By.ID, 'audit-container')
        self.new_audit_previous_button = (By.ID, 'audit-project-wizard-prev-btn-68af') 
        self.new_audit_next_button = (By.ID, 'audit-project-wizard-next-btn-55c1')
        self.new_audit_note_label = (By.ID, 'audit-project-wizard-note-textarea-6a13-label')
        self.new_audit_note_field = (By.ID, 'audit-project-wizard-note-textarea-6a13')
        self.new_audit_signature_field = (By.ID, 'audit-project-wizard-signature-input-95d9')
        self.new_audit_date_field = (By.ID, 'audit-project-wizard-date-input-65e3')
        self.new_audit_complete_button = (By.ID, 'audit-project-wizard-complete-btn-acc3')
        self.audit_complete_message = (By.XPATH, "//div[@role='alert']//span[text()='Audit updated successfully']")