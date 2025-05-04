import os
import pytest
import subprocess


def test_run():
    test_login = os.path.join(os.path.dirname(__file__), 'login/test_login.py')
    allure_results_path = os.path.join(os.path.dirname(__file__), 'allure-results')

    # Run the tests with parallel execution and allure results
    pytest.main([
        test_login,
        '-n', 'auto',  # Parallel execution using all cores
        '-v',  # Verbose output
        '--alluredir', allure_results_path  # Allure results directory
    ])

    # Generate Allure HTML report
    # subprocess.run(['allure', 'generate', allure_results_path, '--clean', '-o', 'allure-report'])
    # subprocess.run(['allure', 'generate', allure_results_path, '--clean', '-o', 'allure-report'])
    # subprocess.run(['allure', 'open', 'allure-report'])


if __name__ == "__main__":
    test_run()
