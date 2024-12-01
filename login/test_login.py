from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login.page import Login
from utilities.read_properties import *
from helpers.conf_test import *
from utilities.read_credentials import CredentialManager


class TestLogIn:
    # Reading configuration values for login
    config = ConfigManager()
    baseURL = config.get_base_url()
    orgURL = config.get_org_url("Higher Institutions", "1")
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
        driver.maximize_window()
        lp.click_login_lp()
        lp.send_email(s_email)
        lp.send_password(s_password)
        lp.click_login()
        lp.close_success_toast(driver)
        print(driver.current_url)
        # Verify successful login
        WebDriverWait(driver, 10).until(
            EC.url_contains("dashboard")
        )

        # Assert that "dashboard" is in the current URL
        assert "dashboard" in driver.current_url, f"Login failed for role: {role}"

        # to get screenshot of DOM
        # try:
        #     WebDriverWait(driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'success')]"))
        #     )
        #     dom_content = driver.page_source
        #     with open("dom_snapshot.html", "w", encoding="utf-8") as file:
        #         file.write(dom_content)
        #     print("DOM snapshot saved.")
        # except Exception as e:
        #     print(f"Failed to capture DOM: {e}")
        return driver, lp

    @pytest.mark.parametrize("setup_login", ["admin"], indirect=True)
    def test_admin_login(self, setup_login):
        driver, lp = setup_login
        # admin
        print("Admin login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()

    @pytest.mark.parametrize("setup_login", ["superadmin"], indirect=True)
    def test_superadmin_login(self, setup_login):
        driver, lp = setup_login
        # superadmin
        print("Superadmin login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()

    @pytest.mark.parametrize("setup_login", ["member_professional_association"], indirect=True)
    def test_member_login(self, setup_login):
        driver, lp = setup_login
        print("member_professional_association login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()

    @pytest.mark.parametrize("setup_login", ["hr_employer"], indirect=True)
    def test_hr_employer_login(self, setup_login):
        driver, lp = setup_login
        print("hr_employer login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()

    @pytest.mark.parametrize("setup_login", ["candidate_employer"], indirect=True)
    def test_employer_login(self, setup_login):
        driver, lp = setup_login
        print(" candidate_employer login test executed successfully")
        driver, lp = setup_login

    @pytest.mark.parametrize("setup_login", ["hr_recruiter"], indirect=True)
    def test_hr_recruiter_login(self, setup_login):
        driver, lp = setup_login
        print("hr_recruiter login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()

    @pytest.mark.parametrize("setup_login", ["student"], indirect=True)
    def test_student_login(self, setup_login):
        driver, lp = setup_login
        print("student login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()

    @pytest.mark.parametrize("setup_login", ["academic_planner"], indirect=True)
    def test_academic_planner_login(self, setup_login):
        driver, lp = setup_login
        print("academic_planner login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()

    @pytest.mark.parametrize("setup_login", ["higher_institution_hr"], indirect=True)
    def test_hi_hr_login(self, setup_login):
        driver, lp = setup_login
        print("higher_institution_hr login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()

    @pytest.mark.parametrize("setup_login", ["staff"], indirect=True)
    def test_staff_login(self, setup_login):
        driver, lp = setup_login
        print("staff login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()

    @pytest.mark.parametrize("setup_login", ["mentor"], indirect=True)
    def test_mentor_login(self, setup_login):
        driver, lp = setup_login
        print("mentor login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()

    @pytest.mark.parametrize("setup_login", ["advisor"], indirect=True)
    def test_advisor_login(self, setup_login):
        driver, lp = setup_login
        print("advisor login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()

    @pytest.mark.parametrize("setup_login", ["lead_advisor"], indirect=True)
    def test_lead_advisor_login(self, setup_login):
        driver, lp = setup_login
        print("lead_advisor login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()
