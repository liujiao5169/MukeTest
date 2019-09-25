# coding=utf-8
import sys
import ddt
from util.excel_init import ExcelInit
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import HTMLTestRunner


ex = ExcelInit()
data = ex.get_data()

# 读取Excel数据进行参数化
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
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
                image_path = sys.path[0]+"/image/"+case_name+".png"
                self.driver.save_screenshot(image_path)
        self.driver.close()

    # 邮箱 用户名 密码 验证码 定位元素 错误提示
    '''
    @ddt.data(
        ["123", "userwed", "111111", "code", "user_email_error", "请输入有效的电子邮件地址"],
        ["@wh.com", "userwed", "111111", "code", "user_email_error", "请输入有效的电子邮件地址"],
        ["123@182.com", "userwed", "111111", "code", "user_email_error", "请输入有效的电子邮件地址"]
              )
    @ddt.unpack
    '''
    # excel文件数据
    @ddt.data(*data)
    def test_register_case(self, data):
        email, username, password, code, assertcode, assertext = data
        register_error = self.register_b.register_function(email, username, password, code, assertcode, assertext)
        # email_error返回True或者False，返回True时，说明email错误提示没有显示，断言结果为F；email错误提示显示显示时，断言结果为OK
        self.assertFalse(register_error, '测试失败')


if __name__ == "__main__":
    file_path = sys.path[1] + "/report/" + "first_case1.html"
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='The first report1', description=u'第一份测试报告', verbosity=2)
    runner.run(suite)
