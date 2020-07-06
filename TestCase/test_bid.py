import unittest
from selenium import webdriver
from TestData.login_data import *
from TestData.common_data import *
from PageObjects.login_page import LoginPage
from PageObjects.bid_page import BidPage
from PageObjects.index_page import IndexPage
from TestData.bit_data import *
from ddt import ddt, data


@ddt
class TestBid(unittest.TestCase):
    @classmethod
    # 所有用例之前先登录
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(login_url)
        cls.lg = LoginPage(cls.driver)
        cls.lg.login(noraml_login['phone'], noraml_login['pwd'])
        cls.indexpage = IndexPage(cls.driver)
        cls.indexpage.click_bid_random()
        cls.bit = BidPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.refresh()

    # 投资成功，正常输入100的倍数
    def test_invest_03_success(self):
        self.bit.invest(success_money)
        self.assertEqual(self.bit.click_activeButton_on_success(), '投标成功！')
    #
    # # 提示请输入10的倍数，即属于小于10，字母，负数
    @data(*failed_money10)
    def test_invest_01_failed10(self, data):
        self.bit.invest(data['money'])
        self.assertEqual(self.bit.get_errorMsg_from_investButton(), data['expected'])

    # 不输入金额，输入100的非整数倍的错误提示语
    @data(*failed_money100)
    def test_invest_02_failed100(self, data):
        self.bit.invest(data['money'])
        self.assertEqual(self.bit.get_errorMsg_from_pageCenter(), data['expected'])
