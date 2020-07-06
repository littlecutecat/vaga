from PageLocators.bidpage_locator import BidPageLocator as loc
from common.basepage import BasePage


class BidPage(BasePage):

    # 投资
    def invest(self, money):
        doc = "投资模块的投资功能"
        self.wait_eleVisible(loc.invest_input, doc=doc)
        self.input_text(loc.invest_input, money, doc=doc)
        self.click_element(loc.bit_button, doc=doc)

    # 获取用户余额
    def get_user_money(self):
        doc = "投资前或者后获取用户余额"
        self.wait_eleVisible(loc.invest_input, doc=doc)
        return self.get_text(loc.bit_balance, doc=doc)

    # 投资成功的提示框
    def click_activeButton_on_success(self):
        doc = "投资成功后的提示框"
        self.wait_eleVisible(loc.bit_success, doc=doc)
        self.click_element(loc.bit_success, doc=doc)

    # 投资失败的错误提示
    def get_errorMsg_from_pageCenter(self):
        doc = "投资失败的错误提示"
        self.wait_eleVisible(loc.errorMsg_close_pagecenter, doc=doc)
        msg = self.get_text(loc.errorMsg_close_pagecenter, doc=doc)
        self.click_element(loc.errorMsg_from_pageCenter, doc=doc)
        return msg

    # 获取错误提示-鼠标按钮上的
    def get_errorMsg_from_investButton(self):
        doc = "获取错误提示-鼠标按钮上的"
        return self.get_text(loc.errorMsg_from_investButton)
