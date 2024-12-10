
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login.page import Login
from utilities.read_properties import ConfigManager
from helpers.conf_test import *
from utilities.read_credentials import CredentialManager


class TestLogIn:
    # Reading configuration values for login
    config = ConfigManager()
    baseURL = config.get_base_url()
    print(f"URL is: {baseURL}")
    orgURL = config.get_org_url("Higher Institutions", "1")
    credentials_manager = CredentialManager()

    @pytest.fixture
    def setup_login(self, setup, request):
        role = request.param  # Access the role passed in parameterized tests
        s_email = self.credentials_manager.get_email(role)
        s_password = self.credentials_manager.get_password(role)
        print(f"Credentials for {role}: {s_email}, {s_password}")


        if not s_email or not s_password:
            print(f"Checking credentials for {role}: {s_email}, {s_password}")
            pytest.fail(f"Missing credentials for role: {role}")


        driver = setup
        lp = Login(driver)
        print(f"URL is: {self.baseURL}")
        driver.get(self.baseURL)
        driver.maximize_window()

        # Log in steps
        lp.click_login_lp()
        lp.send_email(s_email)
        lp.send_password(s_password)
        lp.click_login()
        lp.close_success_toast(driver)

        # Verify successful login
        WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))

        # Assert that "dashboard" is in the current URL
        assert "dashboard" in driver.current_url, f"Login failed for role: {role}"

        # Add a screenshot to Allure on successful login
        allure.attach(driver.get_screenshot_as_png(), name=f"{role}_login_screenshot",
                      attachment_type=allure.attachment_type.PNG)

        return driver, lp

    @pytest.mark.parametrize("setup_login", ["admin"], indirect=True)
    @allure.story("Admin Login Test")
    @allure.title("Test Admin Login")
    def test_admin_login(self, setup_login):
        driver, lp = setup_login
        print("Admin login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()
        print("Admin logout test executed successfully")

    @pytest.mark.parametrize("setup_login", ["superadmin"], indirect=True)
    @allure.story("Superadmin Login Test")
    @allure.title("Test Superadmin Login")
    def test_superadmin_login(self, setup_login):
        driver, lp = setup_login
        print("Superadmin login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()

    @pytest.mark.parametrize("setup_login", ["member_professional_association"], indirect=True)
    @allure.story("Member Login Test")
    @allure.title("Test Member Login")
    def test_member_login(self, setup_login):
        driver, lp = setup_login
        print("Member Professional Association login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()

    @pytest.mark.parametrize("setup_login", ["hr_employer"], indirect=True)
    @allure.story("HR Employer Login Test")
    @allure.title("Test HR Employer Login")
    def test_hr_employer_login(self, setup_login):
        driver, lp = setup_login
        print("HR Employer login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()

    @pytest.mark.parametrize("setup_login", ["candidate_employer"], indirect=True)
    @allure.story("Candidate Employer Login Test")
    @allure.title("Test Candidate Employer Login")
    def test_employer_login(self, setup_login):
        driver, lp = setup_login
        print("Candidate Employer login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()

    @pytest.mark.parametrize("setup_login", ["hr_recruiter"], indirect=True)
    @allure.story("HR Recruiter Login Test")
    @allure.title("Test HR Recruiter Login")
    def test_hr_recruiter_login(self, setup_login):
        driver, lp = setup_login
        print("HR Recruiter login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()

    @pytest.mark.parametrize("setup_login", ["student"], indirect=True)
    @allure.story("Student Login Test")
    @allure.title("Test Student Login")
    def test_student_login(self, setup_login):
        driver, lp = setup_login
        print("Student login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()

    @pytest.mark.parametrize("setup_login", ["academic_planner"], indirect=True)
    @allure.story("Academic Planner Login Test")
    @allure.title("Test Academic Planner Login")
    def test_academic_planner_login(self, setup_login):
        driver, lp = setup_login
        print("Academic Planner login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()

    @pytest.mark.parametrize("setup_login", ["higher_institution_hr"], indirect=True)
    @allure.story("Higher Institution HR Login Test")
    @allure.title("Test Higher Institution HR Login")
    def test_hi_hr_login(self, setup_login):
        driver, lp = setup_login
        print("Higher Institution HR login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()

    @pytest.mark.parametrize("setup_login", ["staff"], indirect=True)
    @allure.story("Staff Login Test")
    @allure.title("Test Staff Login")
    def test_staff_login(self, setup_login):
        driver, lp = setup_login
        print("Staff login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()

    @pytest.mark.parametrize("setup_login", ["mentor"], indirect=True)
    @allure.story("Mentor Login Test")
    @allure.title("Test Mentor Login")
    def test_mentor_login(self, setup_login):
        driver, lp = setup_login
        print("Mentor login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()

    @pytest.mark.parametrize("setup_login", ["advisor"], indirect=True)
    @allure.story("Advisor Login Test")
    @allure.title("Test Advisor Login")
    def test_advisor_login(self, setup_login):
        driver, lp = setup_login
        print("Advisor login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()

    @pytest.mark.parametrize("setup_login", ["lead_advisor"], indirect=True)
    @allure.story("Lead Advisor Login Test")
    @allure.title("Test Lead Advisor Login")
    def test_lead_advisor_login(self, setup_login):
        driver, lp = setup_login
        print("Lead Advisor login test executed successfully")
        lp.click_profile_pic()
        lp.click_logout()

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from login.page import Login
# from utilities.read_properties import *
# from helpers.conf_test import *
# from utilities.read_credentials import CredentialManager
#
#
# class TestLogIn:
#     # Reading configuration values for login
#     config = ConfigManager()
#     baseURL = config.get_base_url()
#     orgURL = config.get_org_url("Higher Institutions", "1")
#     credentials_manager = CredentialManager()
#
#     @pytest.fixture
#     def setup_login(self, setup, request):
#         role = request.param  # Access the role passed in parameterized tests
#         s_email = self.credentials_manager.get_email(role)
#         s_password = self.credentials_manager.get_password(role)
#         if not s_email or not s_password:
#             pytest.fail(f"Missing credentials for role: {role}")
#
#         driver = setup
#         lp = Login(driver)
#         driver.get(self.baseURL)
#         driver.maximize_window()
#         lp.click_login_lp()
#         lp.send_email(s_email)
#         lp.send_password(s_password)
#         lp.click_login()
#         lp.close_success_toast(driver)
#         print(driver.current_url)
#         # Verify successful login
#         WebDriverWait(driver, 10).until(
#             EC.url_contains("dashboard")
#         )
#
#         # Assert that "dashboard" is in the current URL
#         assert "dashboard" in driver.current_url, f"Login failed for role: {role}"
#
#         # to get screenshot of DOM
#         # try:
#         #     WebDriverWait(driver, 10).until(
#         #         EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'success')]"))
#         #     )
#         #     dom_content = driver.page_source
#         #     with open("dom_snapshot.html", "w", encoding="utf-8") as file:
#         #         file.write(dom_content)
#         #     print("DOM snapshot saved.")
#         # except Exception as e:
#         #     print(f"Failed to capture DOM: {e}")
#         return driver, lp
#
#     @pytest.mark.parametrize("setup_login", ["admin"], indirect=True)
#     def test_admin_login(self, setup_login):
#         driver, lp = setup_login
#         # admin
#         print("Admin login test executed successfully")
#         lp.click_profile_pic()
#         lp.click_logout()
#
#     @pytest.mark.parametrize("setup_login", ["superadmin"], indirect=True)
#     def test_superadmin_login(self, setup_login):
#         driver, lp = setup_login
#         # superadmin
#         print("Superadmin login test executed successfully")
#         lp.click_profile_pic()
#         lp.click_logout()
#
#     @pytest.mark.parametrize("setup_login", ["member_professional_association"], indirect=True)
#     def test_member_login(self, setup_login):
#         driver, lp = setup_login
#         print("member_professional_association login test executed successfully")
#         lp.click_profile_pic()
#         lp.click_logout()
#
#     @pytest.mark.parametrize("setup_login", ["hr_employer"], indirect=True)
#     def test_hr_employer_login(self, setup_login):
#         driver, lp = setup_login
#         print("hr_employer login test executed successfully")
#         lp.click_profile_pic()
#         lp.click_logout()
#
#     @pytest.mark.parametrize("setup_login", ["candidate_employer"], indirect=True)
#     def test_employer_login(self, setup_login):
#         driver, lp = setup_login
#         print(" candidate_employer login test executed successfully")
#         driver, lp = setup_login
#
#     @pytest.mark.parametrize("setup_login", ["hr_recruiter"], indirect=True)
#     def test_hr_recruiter_login(self, setup_login):
#         driver, lp = setup_login
#         print("hr_recruiter login test executed successfully")
#         lp.click_profile_pic()
#         lp.click_logout()
#
#     @pytest.mark.parametrize("setup_login", ["student"], indirect=True)
#     def test_student_login(self, setup_login):
#         driver, lp = setup_login
#         print("student login test executed successfully")
#         lp.click_profile_pic()
#         lp.click_logout()
#
#     @pytest.mark.parametrize("setup_login", ["academic_planner"], indirect=True)
#     def test_academic_planner_login(self, setup_login):
#         driver, lp = setup_login
#         print("academic_planner login test executed successfully")
#         lp.click_profile_pic()
#         lp.click_logout()
#
#     @pytest.mark.parametrize("setup_login", ["higher_institution_hr"], indirect=True)
#     def test_hi_hr_login(self, setup_login):
#         driver, lp = setup_login
#         print("higher_institution_hr login test executed successfully")
#         lp.click_profile_pic()
#         lp.click_logout()
#
#     @pytest.mark.parametrize("setup_login", ["staff"], indirect=True)
#     def test_staff_login(self, setup_login):
#         driver, lp = setup_login
#         print("staff login test executed successfully")
#         lp.click_profile_pic()
#         lp.click_logout()
#
#     @pytest.mark.parametrize("setup_login", ["mentor"], indirect=True)
#     def test_mentor_login(self, setup_login):
#         driver, lp = setup_login
#         print("mentor login test executed successfully")
#         lp.click_profile_pic()
#         lp.click_logout()
#
#     @pytest.mark.parametrize("setup_login", ["advisor"], indirect=True)
#     def test_advisor_login(self, setup_login):
#         driver, lp = setup_login
#         print("advisor login test executed successfully")
#         lp.click_profile_pic()
#         lp.click_logout()
#
#     @pytest.mark.parametrize("setup_login", ["lead_advisor"], indirect=True)
#     def test_lead_advisor_login(self, setup_login):
#         driver, lp = setup_login
#         print("lead_advisor login test executed successfully")
#         lp.click_profile_pic()
#         lp.click_logout()
