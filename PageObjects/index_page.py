from PageLocators.indexpage_locator import IndexpageLocator as loc
from common.basepage import BasePage
import random


class IndexPage(BasePage):

    # 判断是否存在退出按钮
    def iseExist_logout_ele(self):
        try:
            self.wait_eleVisible(loc.logout)
            return True
        except:
            return False

    # 找到可以抢投标的标  1、先找到所有可以抢标的标  2、再从中随机拿取第一个
    def click_bid_random(self):
        self.wait_eleVisible(loc.bit)
        # 找到所有可以抢的标
        bits = self.driver.find_elements(*loc.bit)
        # 随机取一个
        index = random.randint(0, len(bits)-1)
        bits[index].click()
