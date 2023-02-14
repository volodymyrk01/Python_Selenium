import time

from selenium.webdriver import Keys

from pages.home_page import HomePage


def test_search(init_driver):
    url = "https://www.google.com/"
    homepage = HomePage(init_driver)
    homepage.load_page(url)
    # time.sleep(120)
    homepage.search("Abracadabra" + Keys.ENTER)
    homepage.clear_search()
    time.sleep(20)


def test_search2(init_driver):
    url = "https://www.google.com/"
    homepage = HomePage(init_driver)
    homepage.load_page(url)
    # time.sleep(120)
    homepage.search("Abracadabra" + Keys.ENTER)
    homepage.clear_search()
    time.sleep(20)
