from utils.selenium_helper import SeleniunHelper


class BasePage(SeleniunHelper):
    def __init__(self, driver):
        super().__init__(driver)
