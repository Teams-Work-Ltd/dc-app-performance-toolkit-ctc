from selenium.webdriver.common.by import By
from util.conf import JIRA_SETTINGS

class UrlManager:
    def __init__(self, project_key=None, projects_list_page=None, goals_list_page=None):
        self.host = JIRA_SETTINGS.server_url
        self.project_list = 'secure/CatAuditProjects.jspa'
        self.project_compliance_settings = 'selectedItem=com.teamswork.compliance.cat-the-compliant-plugin:cat-compliance-project-settings-ca19'
        self.audit_project = 'selectedItem=com.teamswork.compliance.cat-the-compliant-plugin:cat-the-compliant-project-audit-88c9'

    def audit_project_url(self, project_key):
        return f"{self.host}/projects/{project_key}?{self.audit_project}"

    def project_list_url(self):
        return f"{self.host}{self.project_list}"

    def project_compliance_settings_url(self, project_key):
      return f"{self.host}/projects/{project_key}?{self.project_compliance_settings}"

class ProjectComplianceSettingsPageLocators:
    def __init__(self, project_key):
        url_manager = UrlManager()
        self.project_compliance_url = url_manager.project_compliance_settings_url(project_key)
        self.compliance_page_settings_ready = (By.ID, '')
        self.compliance_owner_select = (By.ID, 'complianceOwner')
        self.compliance_type_select = (By.ID, 'complianceType')
        self.compliance_type_select_confidential = (By.ID, 'react-select-2-option-6')
        self.compliance_categories_select = (By.ID, "complianceCategories")
        self.compliance_category_financial_reporting = (By.ID, 'react-select-3-option-1')
        self.audit_frequency_select = (By.ID, "auditFrequency")
        self.audit_frequency_ad_hoc = (By.ID, 'react-select-4-option-7')
        self.compliance_configuration_gdpr = (By.ID, "GDPR-uid1")
        self.compliance_configuration_iso_27001 = (By.ID, "ISO_27001-uid2")
        self.compliance_coinfiguration_iso_20000 = (By.ID, "ISO_20000-uid3")
        self.save_project_compliance_button = (By.ID, "TODO")
        self.save_success_message = (By.XPATH, "//div[@role='alert']//span[text()='Compliance settings updated successfully']")

class AuditProjectLocators:
    audit_project_url = UrlManager().audit_project_url()
    audit_list_page_ready = (By.ID, '') # Should be the id/class of the audit table list
    
    audit_history_button = (By.ID, 'audit-history-link')
    audit_history_table = (By.ID, '')    

    dpo_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-0-0'][value='cyaml.y']")
    dpo_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-0-0')
    written_data_protection_policy_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-0-1'][value='cyaml.y']")
    written_data_protection_policy_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-0-1')
    senior_manager_gdpr_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-0-2'][value='cyaml.y']")
    senior_manager_gdpr_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-0-2')
    gdpr_compliance_document_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-0-3'][value='cyaml.y']")
    gdpr_compliance_document_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-0-3')
    gdpr_compliance_review_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-0-4'][value='cyaml.y']")
    gdpr_compliance_review_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-0-4')
    gdpr_compliance_log_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-0-5'][value='cyaml.y']")
    gdpr_compliance_log_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-0-5')
    data_protection_roles_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-0-6'][value='cyaml.y']")
    data_protection_roles_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-0-6')
    data_protection_impact_assessments_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-0-7'][value='cyaml.y']")
    data_protection_impact_assessments_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-0-7')
    other_controllers_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-0-8'][value='cyaml.y']")
    other_controllers_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-0-8')

    personal_data_identified_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-1-0'][value='cyaml.y']")
    personal_data_identified_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-1-0')
    record_of_processing_activities_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-1-1'][value='cyaml.y']")
    record_of_processing_activities_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-1-1')
    data_movement_diagram_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-1-2'][value='cyaml.y']")
    data_movement_diagram_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-1-2')
    data_inventory_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-1-3'][value='cyaml.y']")
    data_inventory_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-1-3')
    third_party_data_flows = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-1-4'][value='cyaml.y']")
    third_party_data_flows_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-1-4')
    data_inventory_audits_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-1-5'][value='cyaml.y']")
    data_inventory_audits_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-1-5')
    uk_specific_exemptions_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-1-6'][value='cyaml.y']")
    uk_specific_exemptions_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-1-6')

    legal_reason_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-2-0'][value='cyaml.y']")
    legal_reason_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-2-0')
    consent_collected_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-2-1'][value='cyaml.y']")
    consent_collected_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-2-1')
    individual_rights_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-2-2'][value='cyaml.y']")
    individual_rights_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-2-2')
    individual_consents_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-2-3'][value='cyaml.y']") 
    individual_consents_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-2-3')
    legitimate_interests_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-2-4'][value='cyaml.y']")
    legitimate_interests_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-2-4')
    explicit_consent_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-2-5'][value='cyaml.y']")
    explicit_consent_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-2-5')
    privacy_notices_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-2-6'][value='cyaml.y']") 
    privacy_notices_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-2-6')

    minimum_data_processing_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-3-0'][value='cyaml.y']")
    minimum_data_processing_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-3-0')
    personal_data_checked_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-3-1'][value='cyaml.y']")
    personal_data_checked_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-3-1')
    corrective_systems_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-3-2'][value='cyaml.y']")
    corrective_systems_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-3-2')
    redundant_data_processes_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-3-3'][value='cyaml.y']")
    redundant_data_processes_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-3-3')

    encryption_and_firewalls_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-4-0'][value='cyaml.y']")
    encryption_and_firewalls_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-4-0')
    access_controls_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-4-1'][value='cyaml.y']")
    access_controls_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-4-1')
    regular_security_audits_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-4-2'][value='cyaml.y']")
    regular_security_audits_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-4-2')
    software_up_to_date_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-4-3'][value='cyaml.y']")
    software_up_to_date_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-4-3')
    penetration_testing_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-4-4'][value='cyaml.y']")
    penetration_testing_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-4-4')
    third_party_reviews_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-4-5'][value='cyaml.y']")
    third_party_reviews_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-4-5')
    anonymised_personal_data_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-4-6'][value='cyaml.y']")
    anonymised_personal_data_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-4-6')

    data_change_requests_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-5-0'][value='cyaml.y']")
    data_change_requests_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-5-0')
    portable_data_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-5-1'][value='cyaml.y']")
    portable_data_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-5-1')
    identity_checks_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-5-2'][value='cyaml.y']")
    identity_checks_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-5-2')
    response_times_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-5-3'][value='cyaml.y']")
    response_times_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-5-3')
    objection_handling_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-5-4'][value='cyaml.y']")
    objection_handling_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-5-4')

    retention_policy_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-6-0'][value='cyaml.y']")
    retention_policy_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-6-0')
    personal_data_deleted_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-6-1'][value='cyaml.y']")
    personal_data_deleted_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-6-1')
    automated_retention_rules_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-6-2'][value='cyaml.y']")
    automated_retention_rules_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-6-2')
    
    third_party_dpa_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-7-0'][value='cyaml.y']")
    third_party_dpa_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-7-0')
    gdpr_data_transfer_rules_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-7-1'][value='cyaml.y']")
    gdpr_data_transfer_rules_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-7-1')
    third_party_processor_review_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-7-2'][value='cyaml.y']")
    third_party_processor_review_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-7-2')
    third_party_written_agreements_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-7-3'][value='cyaml.y']")
    third_party_written_agreements_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-7-3')

    data_breach_management_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-8-0'][value='cyaml.y']")
    data_breach_management_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-8-0')
    data_breach_reporting_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-8-1'][value='cyaml.y']")
    data_breach_reporting_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-8-1')
    data_breach_training_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-8-2'][value='cyaml.y']")
    data_breach_training_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-8-2')
    data_breach_communication_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-8-3'][value='cyaml.y']")
    data_breach_communication_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-8-3')

    gdpr_training_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-9-0'][value='cyaml.y']")
    gdpr_training_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-9-0')
    internal_processes_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-9-1'][value='cyaml.y']")
    internal_processes_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-9-1')
    gdpr_training_updated_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-9-2'][value='cyaml.y']")
    gdpr_training_updated_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-9-2')
    gdpr_training_staff_radio_option = (By.CSS_SELECTOR, "input[name='status-cyaml.gdpr.checklist.name-9-3'][value='cyaml.y']")
    gdpr_training_staff_evidence_field = (By.ID, 'evidence-cyaml.gdpr.checklist.name-9-3')

    new_audit_button = (By.ID, '')
    new_audit_form_ready = (By.ID, 'audit-container')
    new_audit_previous_button = (By.ID, 'audit-wizard-prev-button') 
    new_audit_next_button = (By.ID, 'audit-wizard-next-button')
    new_audit_note_label = (By.ID, 'note-uid6-label')
    new_audit_note_field = (By.ID, 'note-uid6')
    new_audit_signature_field = (By.ID, 'signature-uid7')
    new_audit_date_field = (By.ID, 'date-uid8')
    new_audit_complete_button = (By.ID, 'complete-audit')
    audit_complete_message = (By.XPATH, "//div[@role='alert']//span[text()='Audit updated successfully']")
    
class ProjectListPageLocators:
    project_list_url = UrlManager().project_list_url()
    search_project_name = (By.ID, "search-project-name")
    project_table = (By.CLASS_NAME, "projects-list")
    project_search_button = (By.ID, "search-projects-button")