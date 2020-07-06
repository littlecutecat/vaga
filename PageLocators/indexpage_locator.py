from selenium.webdriver.common.by import By


class IndexpageLocator:
    logout = (By.XPATH, '//a[@href="/Index/logout.html"]')
    bit = (By.XPATH, '//a[text()="抢投标"]')
