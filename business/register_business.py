# coding=utf-8
import sys
sys.path.append("C:\\Users\\TSDLJ\\PycharmProjects\\UITest_muke")
from handle.register_handle import RegisterHandle


class RegisterBusiness(object):
    def __init__(self, driver):
        self.register_h = RegisterHandle(driver)

    def user_base(self, email, username, password, code):
        self.register_h.send_email(email)
        self.register_h.send_username(username)
        self.register_h.send_password(password)
        self.register_h.send_code(code)
        self.register_h.click_register_button()

    def register_succes(self, email, username, password, file_name):
        self.user_base(email, username, password, file_name)
        if self.register_h.get_register_text() == None:
            return True
        else:
            return False

    def email_login(self, email, username, password, file_name):
        self.user_base(email, username, password, file_name)
        if self.register_h.get_text("email_error", "请输入有效的电子邮件地址") == None:
            print("邮箱检验不成功")
            return True
        else:
            return False

    def register_function(self, email, username, password, code, assertcode, assertext):
        self.user_base(email, username, password, code)
        if self.register_h.get_text(assertcode, assertext) == None:
            # print("测试失败")
            return True
        else:
            return False

    def username_login(self, email, username, password, file_name):
        self.user_base(email, username, password, file_name)
        if self.register_h.get_text("username_error", "字符长度必须大于等于4，一个中文字算2个字符") == None:
            print("用户名检验不成功")
            return True
        else:
            return False

    def password_login(self, email, username, password, file_name):
        self.user_base(email, username, password, file_name)
        if self.register_h.get_text("password_error", "最少需要输入 5 个字符") == None:
            print("密码检验不成功")
            return True
        else:
            return False

    def code_login(self, email, username, password, file_name):
        self.user_base(email, username, password, file_name)
        if self.register_h.get_text("code_error", "验证码错误") == None:
            print("验证码检验不成功")
            return True
        else:
            return False
