import pytest

from config.config import TestData
from pages.LoginPage import LoginPage
from tests.test_base import BaseTest


class Test_Login(BaseTest):

    def test_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)


