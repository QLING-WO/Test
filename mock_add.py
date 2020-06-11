# 编写一个没有完成加法函数
# def add(a, b):
#     return "这是一个没有完成的加法函数"
#
#
# result = add(1, 2)
# print(result)

# 按照常识需求，传入一个1和2，那么他应该返回3
# 如果传入一个2和3，那么应该返回5
# 使用unittest框架，结合mock模块对加法函数虚拟的测试
import unittest
from unittest import mock


class TestAdd(unittest.TestCase):

    def test01_test_add(self):
        # result = add(1, 2)
        # 由于加法函数没有完成，那么我们使用mock模块，模拟加法函数的行为
        add = mock.Mock(return_value=3)
        # 使用mock的函数，进行虚假的运算
        result = add(1, 2)
        # 断言
        self.assertEqual(3, result)
