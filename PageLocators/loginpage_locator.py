from selenium.webdriver.common.by import By


class LoginLocator:
    username = (By.XPATH, '//input[@name="phone"]')
    pwd = (By.XPATH, '//input[@name="password"]')
    login = (By.XPATH, '//button[contains(@class,"btn")]')
    errorMsg_login = (By.XPATH, '//div[@class="form-error-info"]')
    middle_errorMsg_login = (By.XPATH, '//div[@class="layui-layer-content"]')
