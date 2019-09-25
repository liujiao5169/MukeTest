# coding=utf-8
import sys
sys.path.append("C:\\Users\\TSDLJ\\PycharmProjects\\UITest_muke")
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import HTMLTestRunner
import os
from log.user_log import UserLog


class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logger = UserLog()
        cls.log = cls.logger.get_log()

    @classmethod
    def tearDownClass(cls):
        cls.logger.close_log()

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.log.info("This is chrome")
        self.driver.maximize_window()
        self.register_b = RegisterBusiness(self.driver)
        self.file_name = "C:/Users/TSDLJ/PycharmProjects/UITest_muke/screenshot.png"

    def tearDown(self):
        print('这是case的后置条件')
        # sys.exc_info()
        # 报错时截图
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                image_path = os.getcwd()+"/image/"+case_name+".png"
                self.driver.save_screenshot(image_path)
        self.driver.close()

    def test_email_error(self):
        email_error = self.register_b.email_login("123", "user12345", "111111", self.file_name)
        # email_error返回True或者False，返回True时，说明email错误提示没有显示，断言结果为F；email错误提示显示显示时，断言结果为OK
        self.assertFalse(email_error, '邮箱验证case执行')

    def test_username_error(self):
        username_error = self.register_b.username_login("sl11@163.com", "11", "111111", self.file_name)
        self.assertFalse(username_error, '用户名验证case执行')

    def test_password_error(self):
        password_error = self.register_b.password_login("sl12@163.com", "user12343", "11", self.file_name)
        self.assertFalse(password_error, '密码验证case执行')

    def test_code_error(self):
        code_error = self.register_b.code_login("sl1321@163.com", "user12356", "111111", self.file_name)
        self.assertFalse(code_error, '验证码验证case执行')

    def test_login_success(self):
        success = self.register_b.register_succes("sl1511@163.com", "user23211", "111111", self.file_name)
        self.assertTrue(success, '登录验证case执行')


if __name__ == "__main__":
    # unittest.main()
    file_path = os.getcwd()+"/report/"+"first_case.html"
    # print(os.path.dirname(os.getcwd()))
    f = open(file_path, 'wb')
    suite = unittest.TestSuite()
    # suite.addTest(FirstCase('test_email_error'))
    # suite.addTest(FirstCase('test_username_error'))
    # suite.addTest(FirstCase('test_password_error'))
    # suite.addTest(FirstCase('test_code_error'))
    suite.addTest(FirstCase('test_login_success'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='The first report', description=u'第一份测试报告', verbosity=2)
    runner.run(suite)

