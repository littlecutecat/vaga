import unittest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from TestData.login_data import *
from TestData.common_data import *
from ddt import ddt, data
import pytest


@pytest.mark.usefixtures("assess_web")
@pytest.mark.usefixtures("refresh_page")
class LoginTest:
    # 函数名称用来接收它的返回值
    def test_login_03_normal(self, assess_web):
        # 调用登录类并进行数据的赋值
        assess_web[1].login(noraml_login['phone'], noraml_login['pwd'])
        # 断言
        assert IndexPage(self.assess_web[0]).iseExist_logout_ele()


# @ddt
# class LoginTest(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Chrome()
#         cls.driver.get(login_url)
#         cls.lg = LoginPage(cls.driver)
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
#
#     def tearDown(self):
#         self.driver.refresh()
#         # self.driver.quit()
#
#     # 正常登录
#     def test_login_03_normal(self):
#         # 调用登录类并进行数据的赋值
#         self.lg.login(noraml_login['phone'], noraml_login['pwd'])
#         # 断言
#         self.assertTrue(IndexPage(self.driver).iseExist_logout_ele())
#
#     # 输入格式不正确的手机号、不输入手机号、不输入密码,使用ddt来分解数据
#     @data(*wrong_login)
#     def test_login_01_wrongformat(self, data):
#         # 调用登录类并进行数据的赋值
#         self.lg.login(data['phone'], data['pwd'])
#         # 页面中获取的实际结果与期望结果进行比对
#         self.assertEqual(self.lg.get_errorMsg_login(), data['expected'])

    # @data(*wrong_pwd_user)
    # def test_login_02_wrongpwd(self, data):
    #     self.lg.login(data['phone'], data['pwd'])
    #     self.assertEqual(self.lg.get_middle_errorMsg_login(), data['expected'])
