# test_cathaybk_search.py
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages import MainPage

class CathayBankSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        chrome_path = '../chromedriver.exe'
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-application-cache')
        options.add_argument('--disable-extensions')
        service = Service(executable_path=chrome_path)
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.get('https://www.cathaybk.com.tw/cathaybk/')

    def test_search_in_cathaybk(self):
        """Tests cathaybk search feature."""
        main_page = MainPage(self.driver)
        main_page.perform_search('信用卡')
        # Add more assertions here to verify search results

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
