# conding:utf-8
import unittest
from selenium import webdriver
from case.loginfun import login


class LoginCase2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login_2(self):
        login(self.driver)  # 登录功能


if __name__ == '__main__':
    unittest.main()