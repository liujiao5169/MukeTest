#coding=utf-8
from selenium import webdriver
import random
import time
from PIL import Image
from ShowapiRequest import ShowapiRequest

driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
#生成随机邮箱
#for i in range(6):
em = random.sample("123456789abcdefg",6)
email = ''.join(em)+"@163.com"
#print(email)

time.sleep(2)
#识别验证码
#（1）截屏并保持图片
#（2）根据验证码ID获取验证码位置location#{'x': 1000, 'y': 523}，size#{'height': 40, 'width': 129}
#得到(left,upper,right,lower)
#（3）打开截屏图片，根据四个值裁剪验证码图片，保存验证码图片
#（4）打开验证码图片，将图片转化成str
driver.save_screenshot("E:/imooc.png")
img_id = driver.find_element_by_id("getcode_num")
img_xy = img_id.location#{'x': 1000, 'y': 523}
left = img_xy["x"]
upper = img_xy["y"]
img_size = img_id.size#{'height': 40, 'width': 129}
right = img_size["width"]+left
lower = img_size["height"]+upper
img_ele1 = Image.open("E:/imooc.png")
img_ele2 = img_ele1.crop((left,upper,right,lower))
img_ele2.save("E:/imooc1.png")

#img = Image.open("E:/imooc1.png")
#text = pytesseract.image_to_string(img)
#print(text)

#利用第三方包
r = ShowapiRequest("http://route.showapi.com/184-4","103021","9c4dd4bb313b4eb6a7d978987d042dad" )
r.addFilePara("image", "E:/imooc1.png")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res = r.post()
text = res.json()["showapi_res_body"]["Result"]
#print(text) # 返回信息

driver.find_element_by_id("register_email").send_keys(email)
driver.find_element_by_id("register_nickname").send_keys(em)
driver.find_element_by_id("register_password").send_keys("111111")
driver.find_element_by_id("captcha_code").send_keys(text)
driver.find_element_by_id("register-btn").click()
time.sleep(5)
driver.quit()