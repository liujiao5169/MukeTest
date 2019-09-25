# coding=utf-8
from selenium import webdriver
from base.find_element import FindElement
import time


class ActionMethod(object):
    # 打开浏览器
    def open_browser(self, browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()

    # 输入url
    def get_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    # 获取元素
    def get_element(self, key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    # 输入数据
    def element_send_keys(self, key, value):
        self.get_element(key).send_keys(value)

    # 点击元素
    def click_element(self, key):
        self.get_element(key).click()

    # 等待3秒
    def sleep_time(self):
        time.sleep(3)

    # 关闭浏览器
    def close_browser(self):
        self.driver.close()

    # 获取title
    def get_title(self):
        return self.driver.title
