# coding =utf-8

from selenium import webdriver
import random
import time
from PIL import Image
from ShowapiRequest import ShowapiRequest
from base.find_element import FindElement


class RegisterFunction(object):

    def __init__(self, url, i):
        self.driver = self.driver_init(url, i)

    # 浏览器初始化
    def driver_init(self, url, i):
        if i == 1:
            driver = webdriver.Chrome()
        elif i == 2:
            driver = webdriver.firefox()
        else:
            driver = webdriver.edge()
        driver.get(url)
        driver.maximize_window()
        return driver

    # 输入用户信息
    def send_user_info(self, key, data):
        self.get_user_element(key).send_keys(data)

    # 定位用户信息
    def get_user_element(self, key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    # 生成随机用户名
    def user_info(self):
        user_info = ''.join(random.sample("123456789abcdefgh", 6))
        return user_info

    # 截取验证码图片
    def get_code_image(self, file_name):
        self.driver.save_screenshot(file_name)
        img_id = self.get_user_element("code_image")
        img_xy = img_id.location  # {'x': 1000, 'y': 523}
        left = img_xy["x"]
        upper = img_xy["y"]
        img_size = img_id.size  # {'height': 40, 'width': 129}
        right = img_size["width"] + left
        lower = img_size["height"] + upper
        img_ele1 = Image.open(file_name)
        img_ele2 = img_ele1.crop((left, upper, right, lower))
        img_ele2.save(file_name)

    # 解析图片获取验证码
    def code_online(self, file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4", "103021", "9c4dd4bb313b4eb6a7d978987d042dad")
        r.addFilePara("image", file_name)
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "0")
        res = r.post()
        text = res.json()["showapi_res_body"]["Result"]
        return text

    def main(self):
        user_name_info = self.user_info()
        user_mail = user_name_info + "@163.com"
        file_name = "E:/imooc1.png"
        code_text = self.code_online(file_name)
        self.send_user_info("user_mail", user_mail)
        self.send_user_info("user_name", user_name_info)
        self.send_user_info("password", "111111")
        self.send_user_info("code_text", code_text)
        self.get_user_element("register_button").click()
        code_error = self.get_user_element("code_text_error")
        if code_error == None:
            print("注册成功")
        else:
            self.driver.save_screenshot("E:/image-error.png")
        time.sleep(5)
        self.driver.close()


if __name__ == '__main__':
    for i in range(3):
        register_function = RegisterFunction("http://www.5itest.cn/register",1)
        register_function.main()

