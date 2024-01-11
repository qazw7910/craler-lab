import logging
import os
import time

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import config


# This is Common attributes for each page.
class Page(object):
    def __init__(self, driver):
        self.driver = driver

    # ======================= single element ====================== #
    def wait_element_invisible(self, locator, timeout=config.DEFAULT_TIMEOUT):
        element = WebDriverWait(self.driver, timeout, 1).until(EC.invisibility_of_element_located(locator), f'Can not wait element {locator} invisible after {timeout} sec')
        logging.debug(f'wait_element_invisible: {locator}')
        return element

    def wait_element_visible(self, locator, timeout=config.DEFAULT_TIMEOUT):
        element = WebDriverWait(self.driver, timeout, 1).until(EC.visibility_of_element_located(locator), f'Can not wait element {locator} visible after {timeout} sec')
        return element

    def is_find_element(self, locator, timeout=config.DEFAULT_TIMEOUT):
        try:
            self.wait_element_visible(locator, timeout)
            logging.debug(f'is_find_element: {locator}; True')
            return True
        except TimeoutException:
            logging.debug(f'is_find_element: {locator}; False')
            return False

    def find_element(self, locator):
        element = self.wait_element_visible(locator)
        logging.debug(f'find_element: {locator}')
        return element

    def click_element(self, locator, timeout=config.DEFAULT_TIMEOUT):
        element = WebDriverWait(self.driver, timeout, 1).until(EC.element_to_be_clickable(locator), f'Can not wait element {locator} clickable after {timeout} sec')
        try:
            element.click()
            logging.debug(f'click_element: {locator}')
        except (ElementClickInterceptedException, StaleElementReferenceException):
            element = self.wait_element_visible(locator, timeout)
            self.driver.execute_script("arguments[0].click();", element)
            logging.debug(f'click_element via js: {locator}')
        time.sleep(1)

    def get_attr_from_element(self, locator, attr):
        element = self.wait_element_visible(locator)
        value = element.get_attribute(attr)
        logging.debug(f'get_attr_from_element: {locator}; {attr}: {value}')
        return value

    def get_text_from_element(self, locator):
        element = self.wait_element_visible(locator)
        text = element.text
        logging.debug(f'get_text_from_element: {locator}; text: {text}')
        return text

    def send_text_to_element(self, locator, text):
        element = self.wait_element_visible(locator)
        element.clear()
        element.send_keys(text)
        logging.debug(f'send_text_to_element: {locator}; text: {text}')

    def scroll_to_element(self, locator):
        ActionChains(self.driver).move_to_element(self.wait_element_visible(locator)).perform()
        logging.debug(f'scroll_to_element: {locator}')

    def get_values_from_select_option(self, locator):
        element = self.wait_element_visible(locator)
        select = Select(element)
        options = select.options
        options_values = list()
        for option in options:
            options_values.append(option.get_attribute('value'))
        logging.debug(f'get_values_from_select_option: {locator}; options_values: {options_values}')
        return options_values

    def select_option_by_index(self, locator, index):
        element = self.wait_element_visible(locator)
        select = Select(element)
        select.select_by_index(index)
        logging.debug(f'select_option_by_index: {locator}; index: {index}')

    def select_option_by_text(self, locator, text):
        element = self.wait_element_visible(locator)
        select = Select(element)
        select.select_by_visible_text(text)
        logging.debug(f'select_option_by_text: {locator}; text: {text}')

    def select_option_by_value(self, locator, value):
        element = self.wait_element_visible(locator)
        select = Select(element)
        select.select_by_value(value)
        logging.debug(f'select_option_by_text: {locator}; value: {value}')

    def deselect_all_option(self, locator):
        element = self.wait_element_visible(locator)
        select = Select(element)
        select.deselect_all()
        logging.debug(f'deselect_all_option: {locator}')

    # ======================= multiple elements ====================== #
    def wait_elements_visible(self, locator, timeout=config.DEFAULT_TIMEOUT):
        elements = WebDriverWait(self.driver, timeout, 1).until(EC.visibility_of_all_elements_located(locator), f'Can not wait elements {locator} visible after {timeout} sec')
        return elements

    def find_elements(self, locator):
        elements = self.wait_elements_visible(locator)
        logging.debug(f'find_elements: {locator}')
        return elements

    def click_list_item(self, locator, pos, timeout=config.DEFAULT_TIMEOUT):
        element = self.wait_elements_visible(locator, timeout)[pos]
        try:
            element.click()
            logging.debug(f'click_list_item: {locator}; pos: {pos}')
        except (ElementClickInterceptedException, StaleElementReferenceException):
            element = self.wait_elements_visible(locator, timeout)[pos]
            self.driver.execute_script("arguments[0].click();", element)
            logging.debug(f'click_list_item via js: {locator}; pos: {pos}')

    def click_list_item_by_text(self, locator, text, timeout=config.DEFAULT_TIMEOUT):
        for element in self.wait_elements_visible(locator, timeout):
            if text == element.text:
                element.click()
                logging.debug(f'click_list_item_by_text: {locator}; text: {text}')

    def get_texts_from_elements(self, locator):
        elements = self.wait_elements_visible(locator)
        texts_at_elements = list()
        for element in elements:
            texts_at_elements.append(element.text)
        logging.debug(f'get_texts_from_elements: {locator}; texts_at_elements: {texts_at_elements}')
        return texts_at_elements

    # ======================= screenshots ====================== #
    def get_screenshot(self, method_name):
        try:
            screenshot_name = f'{time.strftime("%Y%m%d%H%M%S")}_{method_name}.png'
            screenshot_path = os.path.join(config.SCREENSHOTS_DIR_PATH, time.strftime("%Y%m%d"), screenshot_name)
            self.driver.get_screenshot_as_file(screenshot_path)
            logging.debug(f'get_screenshot: {screenshot_path}')
            return screenshot_name, screenshot_path
        except Exception as e:
            logging.error(e)
