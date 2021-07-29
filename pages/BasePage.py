import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""Pages parent class"""
"""contains all common methods """


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_func(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).click()
        time.sleep(3)


    def send_keys(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)


    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.get_attribute('innerHTML')

    def is_enebled(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def key_press(self, locator , *args):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))





