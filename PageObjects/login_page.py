from PageLocators.loginpage_locator import LoginLocator as loc
from common.basepage import BasePage


class LoginPage(BasePage):

    # 登录
    def login(self, username, pwd):
        doc = "登录模块的登录测试"
        self.wait_eleVisible(loc.username, doc=doc)
        self.input_text(loc.username, username, doc=doc)
        self.input_text(loc.pwd, pwd, doc=doc)
        self.click_element(loc.login, doc=doc)

    # 验证文字的错误提示
    def get_errorMsg_login(self):
        doc = "登录页面的错误提示"
        self.wait_eleVisible(loc.errorMsg_login, doc=doc)
        return self.get_text(loc.errorMsg_login, doc=doc)

    # 验证后台返回的错误提示
    # def get_middle_errorMsg_login(self):
    #     WebDriverWait(self.driver, 0.5).until(EC.visibility_of_element_located(loc.middle_errorMsg_login))
    #     return self.driver.find_element(*loc.middle_errorMsg_login).text

    # 是否存在注册功能
    def resgister_enter(self):
        pass
