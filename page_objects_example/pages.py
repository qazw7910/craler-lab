# pages.py
from locators import MainPageLocators, SearchResultsPageLocators
from elements import BasePageElement

class BasePage:
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    """Main page action methods come here"""
    def __init__(self, driver):
        super().__init__(driver)
        self.search_box = BasePageElement(driver, MainPageLocators.SEARCH_BOX)
        self.search_button = BasePageElement(driver, MainPageLocators.SEARCH_BUTTON)

    def perform_search(self, text):
        self.search_box.input_text(text)
        self.search_button.click()

class SearchResultsPage(BasePage):
    """Search results page action methods come here"""
    # Add methods for interacting with search results
    pass
