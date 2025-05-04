import configparser
import os


class CredentialManager:
    def __init__(self, config_file=r'C:\Users\sarab\Downloads\MyKareer\data\config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        print(f"Loaded sections: {self.config.sections()}")

    def get_email(self, role):
        try:
            email_key = f"{role}_email"
            print(f"Fetching '{email_key}' from section 'credentials live'")
            return self.config.get('credentials live', email_key)
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            print(f"[ERROR] Email not found for role '{role}': {e}")
            return None

    def get_password(self, role):
        try:
            password_key = f"{role}_password"
            print(f"Fetching '{password_key}' from section 'credentials live'")
            return self.config.get('credentials live', password_key)
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            print(f"[ERROR] Password not found for role '{role}': {e}")
            return None

    def get_other_data(self, section, key):
        try:
            return self.config.get(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            print(f"[ERROR] Could not get key '{key}' from section '{section}': {e}")
            return None
