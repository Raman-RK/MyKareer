import os


def write_allure_environment(base_url, browser="Chrome", env="Staging", version="1.0.0"):
    content = f"""Browser={browser}
Environment={env}
Version={version}
BaseURL={base_url}
"""
    os.makedirs("allure-results", exist_ok=True)
    with open("allure-results/environment.properties", "w") as f:
        f.write(content)
