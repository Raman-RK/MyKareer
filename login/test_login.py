from helpers.conf_test import *


class TestLogIn:

    # Universal login-logout test for all roles
    @pytest.mark.parametrize("setup_login", [
        "admin", "superadmin"
    ], indirect=True)
    # "member_professional_association",
    #         "candidate_employer", "student", "academic_planner",
    #         "higher_institution_hr", "staff", "mentor", "advisor"
    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, setup_login):  # Removed `request`
        driver, login_page, role = setup_login  # Unpack role from the fixture

        with allure.step(f"{role} logout after login"):
            login_page.click_profile_pic()
            login_page.click_logout()
            allure.attach(driver.get_screenshot_as_png(), name=f"{role}_logout_screenshot",
                          attachment_type=allure.attachment_type.PNG)
