import configparser


class CredentialManager:
    def __init__(self, config_file='config.ini'):
        # Initialize the config parser and load the config file
        self.config = configparser.ConfigParser()
        self.config.read(r'C:\Users\sarab\Downloads\MyKareer\data\config.ini')

    def get_email(self, role):
        """
        Get the email for a specific role.
        :param role: The role name (e.g., 'superadmin', 'admin')
        :return: The email as a string.
        """
        try:
            email_key = f"{role}_email"
            return self.config.get('credentials live', email_key)
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            print(f"Error: {e}")
            return None

    def get_password(self, role):
        """
        Get the password for a specific role.
        :param role: The role name (e.g., 'superadmin', 'admin')
        :return: The password as a string.
        """
        try:
            password_key = f"{role}_password"
            return self.config.get('credentials live', password_key)
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            print(f"Error: {e}")
            return None

    def get_url(self, environment, target):
        """
        Get the URL for a specific environment and target.
        :param environment: The environment section ('dev urls' or 'live urls')
        :param target: The target name (e.g., 'baseURL', 'higherInstitution')
        :return: The URL as a string.
        """
        try:
            return self.config.get(environment, target)
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            print(f"Error: {e}")
            return None

    def get_other_data(self, section, key):
        """
        Get data from any section and key in the config file.
        :param section: The section name in the config file.
        :param key: The key name in the section.
        :return: The value associated with the key.
        """
        try:
            return self.config.get(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            print(f"Error: {e}")
            return None
