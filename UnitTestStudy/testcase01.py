import unittest


class Cases(unittest.TestCase):
    # 前置条件
    def setUp(self) -> None:
        print('setup')

    # 后置条件
    def tearDown(self) -> None:
        print('teardown')
    def test_01(self):
        print("第一个测试用例")
        self.demo_01()

    def demo_01(self):
        print("假的测试用例")

    def test_02(self):
        print('第二条测试用例')

if __name__ == '__main__':
    unittest.main()