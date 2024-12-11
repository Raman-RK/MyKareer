import os
import pytest


def test_run():
    test_login = os.path.join(os.path.dirname(__file__), 'login/test_login.py')

    allure_results_path = os.path.join(os.path.dirname(__file__), 'allure-results')

    # Run the tests
    pytest.main(['-q', '--alluredir', allure_results_path, test_login])


if __name__ == "__main__":
    test_run()
