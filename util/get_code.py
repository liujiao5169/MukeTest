# coding=utf-8
from PIL import Image
from ShowapiRequest import ShowapiRequest
import time


class GetCode(object):
    def __init__(self,driver):
        self.driver = driver

    # 截取验证码图片
    def get_code_image(self, file_name):
        self.driver.save_screenshot(file_name)
        img_id = self.driver.find_element_by_id("getcode_num")
        img_xy = img_id.location  # {'x': 1000, 'y': 523}
        left = img_xy["x"]
        upper = img_xy["y"]
        img_size = img_id.size  # {'height': 40, 'width': 129}
        right = img_size["width"] + left
        lower = img_size["height"] + upper
        img_ele1 = Image.open(file_name)
        img_ele2 = img_ele1.crop((left, upper, right, lower))
        img_ele2.save(file_name)
        time.sleep(2)

    # 解析图片获取验证码
    def code_online(self, file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4", "105013", "ddd26a987e734fbebaf3bda44dad634b")
        r.addFilePara("image", file_name)
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "0")
        res = r.post()
        text = res.json()["showapi_res_body"]["Result"]
        time.sleep(2)
        return text
