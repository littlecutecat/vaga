import logging
import datetime
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common.project_path import *


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 等待元素出现
    def wait_eleVisible(self, locator, times=30, poll_frequency=0.5, doc=""):
        logging.info("{0}等待元素{1}可见".format(doc, locator))
        try:
            # 开始等待时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver, times, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束等待时间
            end = datetime.datetime.now()
            # 等待时间
            waittime = (end-start).seconds
            logging.info("{0}的元素{1}等待的时间为{2}".format(doc, locator, waittime))
        except:
            logging.exception("{0}等待元素{1}可见失败".format(doc, locator))
            # 截图操作
            self.save_sreentshot(doc)
            raise

    # 等待元素存在
    def wait_elePresence(self, locator, times=30, poll_frequency=0.5, doc=""):
        logging.info("{0}等待元素{1}存在".format(doc, locator))
        try:
            # 开始等待时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver, times, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束等待时间
            end = datetime.datetime.now()
            # 等待时间
            waittime = (end - start).seconds
            logging.info("{0}的元素{1}等待的时间为{2}".format(doc, locator, waittime))
        except:
            logging.exception("{0}等待元素{1}可见失败".format(doc, locator))
            # 截图操作
            self.save_sreentshot(doc)
            raise

    # 查找/获取元素
    def get_element(self, locator, doc=""):
        logging.info("{0}查找元素{1}".format(doc, locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception("{0}查找元素{1}失败".format(doc, locator))
            self.save_sreentshot(doc)
            raise

    # 元素的点击
    def click_element(self, locator, doc=""):
        ele = self.get_element(locator, doc)
        logging.info("{0}点击元素{1}".format(doc, locator))
        try:
            ele.click()
        except:
            logging.exception("{0}点击元素{1}失败".format(doc, locator))
            self.save_sreentshot(doc)

    # 输入值
    def input_text(self, locator, text, doc=""):
        ele = self.get_element(locator, doc)
        logging.info("{0}输入文本{1}".format(doc, locator))
        try:
            ele.send_keys(text)
        except:
            logging.exception("{0}输入元素{1}失败".format(doc, locator))
            self.save_sreentshot(doc)

    # 获取元素的文本
    def get_text(self, locator, doc=""):
        ele = self.get_element(locator, doc)
        logging.info("{0}获取属性{1}".format(doc, locator))
        try:
            return ele.text
        except:
            logging.exception("{0}输入获取文本失败".format(doc))
            self.save_sreentshot(doc)

    # 获取元素的属性
    def get_ele_attribute(self, locator, attr, doc=""):
        ele = self.get_element(locator, doc)
        logging.info("{0}元素属性{1}".format(doc, locator))
        try:
            return ele.get_attribute(attr)
        except:
            logging.exception("{0}输入获取属性失败".format(doc))
            self.save_sreentshot(doc)

    # alert处理
    def alert_action(self, action='accept'):
        pass

    # iframe切换
    def switch_iframe(self):
        pass

    # 上传操作
    def upload_file(self):
        pass

    # 截图操作
    def save_sreentshot(self, doc):
        # 图片名称：模块名称_页面名称_操作名称_时间(年月日时分秒).png
        file_path = screenshot_path + "/{0}_{1}.png".format(doc, time.strftime("%Y-%M-%D-%H-%M-%S", time.localtime(time.time())))
        try:
            self.driver.save_screeshot(file_path)
            logging.info("截取网页成功，存在路径为:{0}".format(file_path))
        except:
            logging.exception("截图失败")


    # 窗口切换
    # 滚动条处理
