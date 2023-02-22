from datetime import datetime
import pytest
from selenium import webdriver
from pymongo import MongoClient


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='Chrome',
        help='Choose browser: Chrome, Firefox, Edge'
    )


@pytest.fixture(autouse=True, scope='session')
def mongodb_fixture(request):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['framework_test']
    passed_count = 0
    failed_count = 0
    yield
    session = request.node
    for item in session.items:
        if item.session.testsfailed:
            failed_count += 1
        elif item.session.testscollected:
            passed_count += 1
    failed_result = {
        'timestamp': datetime.utcnow(),
        'result': 'FAILED',
        'count': failed_count
    }
    passed_result = {
        'timestamp': datetime.utcnow(),
        'result': 'PASSED',
        'count': passed_count
    }
    db.framework.drop()
    db.framework.insert_one(failed_result)
    db.framework.insert_one(passed_result)


@pytest.fixture
def init_driver(request):
    chrome_options = webdriver.ChromeOptions()
    firefox_options = webdriver.FirefoxOptions()
    edge_options = webdriver.EdgeOptions()

    browser = request.config.getoption("--browser")

    if browser == "Chrome":
        driver = webdriver.Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            options=chrome_options
        )

    elif browser == "Firefox":
        driver = webdriver.Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            options=firefox_options
        )

    elif browser == "Edge":
        driver = webdriver.Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            options=edge_options
        )

    else:
        raise Exception(f"Browser - {browser} is not supported")

    driver.maximize_window()
    yield driver

    driver.quit()
