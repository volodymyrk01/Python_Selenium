import os
import subprocess


def test_html_report_generated():
    assert os.path.exists("/html/pytest_report.html")


def test_number_of_tests():
    test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    num_tests = count_tests_in_directory(test_dir)
    assert num_tests == 3


def count_tests_in_directory(test_dir):
    command = ["pytest", "--collect-only", test_dir]
    output = subprocess.check_output(command, stderr=subprocess.STDOUT).decode()
    lines = output.split("\n")
    num_tests = 0
    for line in lines:
        if "collected " in line:
            num_tests += int(line.split("collected ")[1].split(" ")[0])
            return num_tests