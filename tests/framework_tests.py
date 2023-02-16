import os


def test_html_report_generated():
    assert os.path.exists("/html/pytest_report.html")
