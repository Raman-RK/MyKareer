import pytest
from login.page import Login
from utilities.read_properties import *
from helpers.conf_test import *
from utilities.read_credentials import CredentialManager


class TestLogIn:
    # Reading configuration values for login
    config_reader_url = Urls()
    baseURL = config_reader_url.get_dev_main_url()
    hi_url = config_reader_url.higher_institute_dev_url()
    credentials_manager = CredentialManager()

    @pytest.fixture
    def setup_login(self, setup, request):
        role = request.param  # Access the role passed in parameterized tests
        s_email = self.credentials_manager.get_email(role)
        s_password = self.credentials_manager.get_password(role)
        if not s_email or not s_password:
            pytest.fail(f"Missing credentials for role: {role}")

        driver = setup
        lp = Login(driver)
        driver.get(self.baseURL)
        lp.click_login_lp()
        lp.send_email(s_email)
        lp.send_password(s_password)
        lp.click_login()

        # Verify successful login
        assert "login" in driver.current_url, f"Login failed for role: {role}"

        return driver

    @pytest.mark.parametrize("setup_login", ["admin"], indirect=True)
    def test_admin_login(self, setup_login):
        # admin
        print("Admin login test executed successfully")

    @pytest.mark.parametrize("setup_login", ["superadmin"], indirect=True)
    def test_superadmin_login(self, setup_login):
        # superadmin
        print("Superadmin login test executed successfully")

    @pytest.mark.parametrize("setup_login", ["member_professional_association"], indirect=True)
    def test_member_login(self, setup_login):
        print("member_professional_association login test executed successfully")

    @pytest.mark.parametrize("setup_login", ["hr_employer"], indirect=True)
    def test_hr_employer_login(self, setup_login):
        print("hr_employer login test executed successfully")

    @pytest.mark.parametrize("setup_login", ["candidate_employer"], indirect=True)
    def test_employer_login(self, setup_login):
        print(" candidate_employer login test executed successfully")

    @pytest.mark.parametrize("setup_login", ["hr_recruiter"], indirect=True)
    def test_hr_recruiter_login(self, setup_login):
        print("hr_recruiter login test executed successfully")

    @pytest.mark.parametrize("setup_login", ["student"], indirect=True)
    def test_student_login(self, setup_login):
        print("student login test executed successfully")

    @pytest.mark.parametrize("setup_login", ["academic_planner"], indirect=True)
    def test_academic_planner_login(self, setup_login):
        print("academic_planner login test executed successfully")

    @pytest.mark.parametrize("setup_login", ["higher_institution_hr"], indirect=True)
    def test_hi_hr_login(self, setup_login):
        print("higher_institution_hr login test executed successfully")

    @pytest.mark.parametrize("setup_login", ["staff"], indirect=True)
    def test_staff_login(self, setup_login):
        print("staff login test executed successfully")

    @pytest.mark.parametrize("setup_login", ["mentor"], indirect=True)
    def test_mentor_login(self, setup_login):
        print("mentor login test executed successfully")

    @pytest.mark.parametrize("setup_login", ["advisor"], indirect=True)
    def test_advisor_login(self, setup_login):
        print("advisor login test executed successfully")

    @pytest.mark.parametrize("setup_login", ["lead_advisor"], indirect=True)
    def test_lead_advisor_login(self, setup_login):
        print("lead_advisor login test executed successfully")
