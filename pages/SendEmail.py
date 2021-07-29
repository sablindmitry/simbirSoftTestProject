from selenium.webdriver.common.by import By
from config.config import TestData
from pages.BasePage import BasePage



class SendEmailPage(BasePage):
    CREATE_EMAIL_LOCATOR = (By.XPATH, '//*[@id=":15z"]/div/div')

    def __init__(self, driver):
        super().__init__(driver)

    def create_email(self):
        self.click_func(self.CREATE_EMAIL_LOCATOR)
