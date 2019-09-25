# coding=utf-8
from selenium import webdriver
import time
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest


driver = webdriver.Chrome()


# 浏览器初始化
def driver_init():
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    time.sleep(3)


# 获取元素信息
def elements(id):
    element = driver.find_element_by_id(id)
    return element


# 生成随机用户名
def user_info():
    user_info = ''.join(random.sample("123456789abcdefgh",6))
    return user_info


# 截取验证码图片
def get_code_image(file_name):
    driver.save_screenshot(file_name)
    img_id = driver.find_element_by_id("getcode_num")
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
def code_online(file_name):
    r = ShowapiRequest("http://route.showapi.com/184-4", "103021", "9c4dd4bb313b4eb6a7d978987d042dad")
    r.addFilePara("image", file_name)
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    res = r.post()
    text = res.json()["showapi_res_body"]["Result"]
    return text


# 运行主程序
def run_main():
    user_name_info = user_info()
    user_mail = user_name_info+"@163.com"
    file_name = "E:/imooc1.png"
    driver_init()
    get_code_image(file_name)
    text = code_online(file_name)
    elements("register_email").send_keys(user_mail)
    elements("register_nickname").send_keys(user_name_info)
    elements("register_password").send_keys("111111")
    elements("captcha_code").send_keys(text)
    time.sleep(5)
    elements("register-btn").click()
    driver.close()


run_main()
