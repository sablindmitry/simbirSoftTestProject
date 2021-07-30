from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from config.config import TestData
from pages.BasePage import BasePage

'''Main gmail page for sending and counting emails'''

class GmailMainPage(BasePage):

    '''Locators of all needed elements'''
    SEARCH_FIELD = (By.XPATH, '//*[@id="gs_lc50"]/input[1]')
    SEARCH_FIELD_BUTTON = (By.XPATH, '//*[@id="aso_search_form_anchor"]/button[4]')
    EMAILS_COUNTER = (By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/span/div[1]/span/span[2]') #Tryed with full path for test and suddenly it worked for all test ( can try to do relative xpath)
    CREATE_EMAIL_LOCATOR = (By.CLASS_NAME, 'T-I-KE')
    EMAIL_RECEIVER_LOCATOR = (By.XPATH, "//*[@name='to']")
    EMAIL_SUBJECT_LOCATOR = (By.XPATH, '//input[@name="subjectbox"]')
    EMAIL_BODY_LOCATOR = (By.XPATH, '//div[@role="textbox"]')
    SEND_EMAIL_BUTTON_LOCATOR = (By.CSS_SELECTOR, '.T-I.J-J5-Ji.aoO.v7.T-I-atl.L3')
    #SEND_EMAIL_BUTTON_LOCATOR = (By.XPATH, '//*[text()="Отправить"]')

    def __init__(self, driver):
        super().__init__(driver)

    def do_search_filter(self, text):
        '''Filtring emails by required subject '''
        self.send_keys(self.SEARCH_FIELD, text)
        self.click_func(self.SEARCH_FIELD_BUTTON)

    def get_emails_counter(self):
        '''Use locator for getting number of required emails'''
        if self.is_enebled(self.EMAILS_COUNTER):
            return self.get_element_text(self.EMAILS_COUNTER)

    def start_email_window(self):
        self.click_func(self.CREATE_EMAIL_LOCATOR)

    def create_email(self):
        self.send_keys(self.EMAIL_RECEIVER_LOCATOR, TestData.EMAIL_TO_SEND)
        self.send_keys(self.EMAIL_SUBJECT_LOCATOR, f'{TestData.EMAIL_SUBJECT_FILTER}  -  {TestData.MY_SURNAME}')
        self.send_keys(self.EMAIL_BODY_LOCATOR, f'Писем с темой "Simbirsoft Тестовое задание" найдено - {self.get_emails_counter()}')
        self.click_func(self.SEND_EMAIL_BUTTON_LOCATOR)





