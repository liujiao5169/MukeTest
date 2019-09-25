# coding=utf-8
import unittest


class UnittestCase2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("整体前置条件")

    def setUp(self):
        print("前置条件")

    def tearDown(self):
        print("后置条件")

    def testcase001(self):
        print("这是第001条case")

    def testcase002(self):
        print("这是第002条case")

    @unittest.skip("不执行")
    def testcase003(self):
        print("这是第003条case")

    @classmethod
    def tearDownClass(cls):
        print("整体后置处理")


if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(UnittestCase2("testcase001"))
    suite.addTest(UnittestCase2("testcase002"))
    suite.addTest(UnittestCase2("testcase003"))
    unittest.TextTestRunner().run(suite)
