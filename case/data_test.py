# coding=utf-8
import ddt
import unittest


@ddt.ddt
class DataTest(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    @ddt.data([1, 2], [3, 4], [5, 6])
    @ddt.data(
        ["123", "userwed", "111111", "code", "email_error", "请输入有效的电子邮件地址"],
        ["sl11@165.com", "11", "111111", "code", "username_error", "字符长度必须大于等于4，一个中文字算2个字符"],
        ["sl12@167.com", "userdsd43", "11", "code", "password_error", "最少需要输入 5 个字符"],
        ["sl1321@160.com", "uservf356", "111111", "code", "code_error", "验证码错误"]
    )
    @ddt.unpack
    def test_add(self, a, b):
        print(a+b)


if __name__ == "__main__":
    unittest.main()
