from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):

    gmail_button = (By.XPATH, "//a[text()='Gmail']")
    sign_in_button = (By.XPATH, "//a[text()='Sign in']")
    # search_field = (By.XPATH, "//*[contains(@title, 'Search')]")
    search_bar = (By.NAME, "q")
    search_button = ""

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def load_page(self, url):
        self.driver.get(url)

    def search(self, input):
        self.do_click(self.search_bar)
        self.do_send_keys(self.search_bar, input)

    def clear_search(self):
        self.clear(self.search_bar)
