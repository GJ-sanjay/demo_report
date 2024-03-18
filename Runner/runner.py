
from behave import __main__ as behave_main

FEATURE_FILE_PATH = (
    "C://Users//sjayakumar//myworld//UltimateQA//Feature//features.feature"
)

if __name__ == "__main__":
    # Use '--no-capture' to stop suppress stderr and stdout
    behave_main.main(["--no-capture", FEATURE_FILE_PATH])

#To Generate a allure report
#Use this code below
    
"""
import subprocess

FEATURE_FILE_PATH = (
    "C://Users//sjayakumar//myworld//UltimateQA//Feature//features.feature"
)

if __name__ == "__main__":
    # Execute the Behave tests and capture output
    behave_command = ["behave", "--no-capture", FEATURE_FILE_PATH]
    subprocess.run(behave_command, check=True)

    # Generate Allure reports using the Allure command-line tool
    allure_command = ["allure", "generate", "allure-results", "-o", "allure-report", "--clean"]
    subprocess.run(allure_command, check=True)
"""