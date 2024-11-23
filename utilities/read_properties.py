import os
import configparser


class ReadConfig:
    """Base class for handling the configuration file"""

    def __init__(self):
        # Initialize config parser and load the config file
        self.config = configparser.ConfigParser()
        self.config_file_path = os.path.join(os.path.dirname(__file__), '../data/config.ini')
        self.config.read(self.config_file_path, encoding='utf-8')


class Urls(ReadConfig):
    """URLs (live and dev)"""

    # Live URLs
    def get_live_main_url(self):
        return self.config.get('live urls', 'baseURL')

    def higher_institute_live_url(self):
        return self.config.get('live urls', 'higherInstitution')

    def employer_live_url(self):
        return self.config.get('live urls', 'employer')

    def recruiter_live_url(self):
        return self.config.get('live urls', 'recruiter')

    def p_association_live_url(self):
        return self.config.get('live urls', 'pAssociation')

    # Dev URLs
    def get_dev_main_url(self):
        return self.config.get('dev urls', 'baseURL')

    def higher_institute_dev_url(self):
        return self.config.get('dev urls', 'higherInstitution')

    def employer_dev_url(self):
        return self.config.get('dev urls', 'employer')

    def recruiter_dev_url(self):
        return self.config.get('dev urls', 'recruiter')

    def p_association_dev_url(self):
        return self.config.get('dev urls', 'pAssociation')


# import os
# import configparser
#
#
# class ReadConfig:
#     config = configparser.ConfigParser()
#     config_file_path = os.path.join(os.path.dirname(__file__), '../data/config.ini')
#
#     def __init__(self):
#         self.config.read(self.config_file_path, encoding='utf-8')
#
#     # live urls
#
#     def get_live_main_url(self):
#         main_live_url = self.config.get('live urls', 'baseURL')
#         print(main_live_url)
#         return main_live_url
#
#     def higher_institute_live_url(self):
#         url = self.config.get('live urls', 'higherInstitution')
#         return url
#
#     def employer_live_url(self):
#         url = self.config.get('live urls', 'employer')
#         return url
#
#     def recruiter_live_url(self):
#         url = self.config.get('live urls', 'recruiter')
#         return url
#
#     def p_association_live_url(self):
#         url = self.config.get('live urls', 'pAssociation')
#         return url
#
#     # dev urls
#
#     def higher_institute_dev_url(self):
#         url = self.config.get('dev urls', 'higherInstitution')
#         return url
#
#     def employer_dev_url(self):
#         url = self.config.get('dev urls', 'employer')
#         return url
#
#     def recruiter_dev_url(self):
#         url = self.config.get('dev urls', 'recruiter')
#         return url
#
#     def p_association_dev_url(self):
#         url = self.config.get('dev urls', 'pAssociation')
#         return url
#
#     def get_dev_main_url(self):
#         main_dev_url = self.config.get('dev urls', 'baseURL')
#         print(main_dev_url)
#         return main_dev_url
#
#     # passwords
#
#     def get_c_password(self):
#         c_password = self.config.get('credentials live', 'commonPassword')
#         return c_password
#
#     def get_sa_password(self):
#         s_password = self.config.get('credentials live', 'spassword')
#         return s_password
#
#     # credentials live
#     def s_admin_email(self):
#         email = self.config.get('credentials live', 'superAdminEmail')
#         return email  # superadmin
#
#     def admin_email(self):
#         email = self.config.get('credentials live', 'adminEmail')
#         return email  # all adminsc
#
#     def member_pa_email(self):
#         email = self.config.get('credentials live', 'memberPaEmail')
#         return email  # professional association member
#
#     def l_advisor_email(self):
#         email = self.config.get('credentials live', 'lAdvisorEmail')
#         return email  # lead advisor
#
#     def advisor_email(self):
#         email = self.config.get('credentials live', 'advisorEmail')
#         return email  # advisor
#
#     def mentor_email(self):
#         email = self.config.get('credentials live', 'mentorEmail')
#         return email














