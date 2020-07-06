from selenium.webdriver.common.by import By


class BidPageLocator:
    invest_input = (By.XPATH, '//input[contains(@class,"form-control")]')
    bit_balance = 'data-amount'
    bit_button = (By.XPATH, '//button[text()="投标"]')
    errorMsg_from_investButton = (By.XPATH, '//button[@class="btn btn-special height_style"]')
    errorMsg_from_pageCenter = (By.XPATH, '//div[@class="text-center"]')
    errorMsg_close_pagecenter = (By.XPATH, '//a[@class="layui-layer-btn0"]')
    bit_success = (By.XPATH, '//div[@class="layui-layer-content"]/div[@class="capital_ts"]/div[contains(@class,"capital_font1 ")]')
