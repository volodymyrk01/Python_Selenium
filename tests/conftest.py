import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='Chrome',
        help='Choose browser: Chrome, Firefox, Edge'
    )


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
