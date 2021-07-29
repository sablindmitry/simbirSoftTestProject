from selenium.webdriver.common.by import By
from config.config import TestData
from pages.BasePage import BasePage
from pages.GmailMainPage import GmailMainPage


class LoginPage(BasePage):

    EMAIL_FIELD_LOCATOR = (By.XPATH, '//*[@id ="identifierId"]')
    LOGIN_BUTTON_LOCATOR = (By.XPATH, '//*[@id ="identifierNext"]')
    PASSWORD_FIELD_LOCATOR = (By.XPATH, '//*[@id ="password"]/div[1]/div / div[1]/input')
    PASSWORD_BUTTON_LOCATOR = (By.XPATH, '//*[@id ="passwordNext"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)


    def do_login(self, username, password):
        self.send_keys(self.EMAIL_FIELD_LOCATOR, username)
        self.click_func(self.LOGIN_BUTTON_LOCATOR)
        self.send_keys(self.PASSWORD_FIELD_LOCATOR, password)
        self.click_func(self.PASSWORD_BUTTON_LOCATOR)
        return GmailMainPage(self.driver)






