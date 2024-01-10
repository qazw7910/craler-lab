# element.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePageElement:
    """Base page class that is initialized on every page object class."""

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def input_text(self, text):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locator)
        ).send_keys(text)

    def click(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locator)
        ).click()
