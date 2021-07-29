import pytest
import self as self
from selenium.webdriver.common.keys import Keys

from config.config import TestData
from pages.GmailMainPage import GmailMainPage
from pages.LoginPage import LoginPage
from tests.test_base import BaseTest


class Test_Login(BaseTest):

    def test_emails_counter(self):
        self.login_page = LoginPage(self.driver)
        #self.email_page = GmailMainPage(self.driver)
        gmail_main_page = self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        gmail_main_page.do_search_filter(TestData.EMAIL_SUBJECT_FILTER)
        gmail_main_page.get_emails_counter()
        gmail_main_page.start_email_window()
        gmail_main_page.create_email()

