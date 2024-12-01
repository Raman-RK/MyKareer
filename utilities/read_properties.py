import os
from dotenv import load_dotenv


class ConfigManager:
    def __init__(self):
        load_dotenv()
        self.environment = os.getenv("ENVIRONMENT", "DEV").upper()

    def get_base_url(self):
        return os.getenv(f"{self.environment}_BASE_URL")

    def get_org_url(self, org, org_number):
        key = f"{self.environment}_{org.upper()}_URL{org_number}"
        return os.getenv(key)
