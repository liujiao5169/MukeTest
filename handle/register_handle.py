# coding=utf-8
import sys
sys.path.append("C:\\Users\\TSDLJ\\PycharmProjects\\UITest_muke")
from page.register_page import RegisterPage
from util.get_code import GetCode


class RegisterHandle(object):
    def __init__(self, driver):
        self.driver = driver
        self.register_p = RegisterPage(self.driver)

    # 输入邮箱
    def send_email(self, email):
        self.register_p.get_email_element().send_keys(email)

    # 输入用户名
    def send_username(self, username):
        self.register_p.get_username_element().send_keys(username)

    # 输入密码
    def send_password(self, password):
        self.register_p.get_password_element().send_keys(password)

    # 输入验证码
    def send_code(self, code):
        # get_code = GetCode(self.driver)
        # code = get_code.code_online(file_name)
        self.register_p.get_code_element().send_keys(code)

    # 获取文字信息
    def get_text(self, info, user_info):
        try:
            if info == "user_email_error":
                text = self.register_p.get_register_email_error_element().text
            elif info == "user_name_error":
                text = self.register_p.get_username_error_element().text
            elif info == "password_error":
                text = self.register_p.get_password_error_element().text
            else:
                text = self.register_p.get_code_error_element().text
        except:
            text = None
        return text

    # 点击注册按钮
    def click_register_button(self):
        self.register_p.get_register_button_element().click()

    # 获取注册按钮文本
    def get_register_text(self):
        try:
            text = self.register_p.get_register_button_element().get_attribute("value")
        except:
            text = None
        return text


