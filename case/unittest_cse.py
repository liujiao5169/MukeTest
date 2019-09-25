# coding=utf-8
import unittest


class UnittestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("整体前置条件")

    def setUp(self):
        print("前置条件")

    def tearDown(self):
        print("后置条件")

    def testcase001(self):
        print("这是第1条case")

    def testcase002(self):
        print("这是第2条case")

    @unittest.skip("不执行")
    def testcase003(self):
        print("这是第3条case")

    @classmethod
    def tearDownClass(cls):
        print("整体后置处理")


if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(UnittestCase("testcase001"))
    suite.addTest(UnittestCase("testcase002"))
    suite.addTest(UnittestCase("testcase003"))
    unittest.TextTestRunner().run(suite)
