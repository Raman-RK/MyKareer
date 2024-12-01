import configparser


class CredentialManager:
    def __init__(self, config_file='config.ini'):
        # Initialize the config parser and load the config file
        self.config = configparser.ConfigParser()
        self.config.read(r'C:\Users\sarab\Downloads\MyKareer\data\config.ini')  # Pass config_file as a parameter

    def get_email(self, role):
        try:
            email_key = f"{role}_email"
            return self.config.get('credentials live', email_key)
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            print(f"Error: {e}")
            return None

    def get_password(self, role):
        try:
            password_key = f"{role}_password"
            return self.config.get('credentials live', password_key)
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            print(f"Error: {e}")
            return None

    def get_other_data(self, section, key):
        try:
            return self.config.get(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            print(f"Error: {e}")
            return None


