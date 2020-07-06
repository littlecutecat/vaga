import pytest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from TestData.common_data import *

driver = None


@pytest.fixture(scope="class")
def assess_web():
    # 前置条件
    global driver
    print("所有用例执行之前先执行")
    driver = webdriver.Chrome()
    driver.get(login_url)
    lg = LoginPage(driver)
    # yeild 用来作为分割线，和 作为返回值
    yield (driver, lg)
    # 后置条件
    print("所有用例执行之后")
    driver.quit()


@pytest.fixture
def refresh_page():
    global driver
    yield
    driver.refresh()
