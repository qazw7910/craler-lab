# locators.py
from selenium.webdriver.common.by import By

class MainPageLocators:
    """A class for main page locators. All main page locators should come here"""
    SEARCH_BOX = (By.ID, 'searchBox')
    SEARCH_BUTTON = (By.XPATH, '/html/body/div[1]/main/section/div[3]/div[3]/div/div/div[1]/div/a[1]')

class SearchResultsPageLocators:
    """A class for search results locators. All search results locators should come here"""
    # Define locators for search results elements
    pass
