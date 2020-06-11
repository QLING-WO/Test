import unittest
from unittest import mock

from sample import OrderPayService,UserService


class TestOrderPay(unittest.TestCase):

    def test01(self):
        UserService.get_user_amount = mock.Mock(return_value=8000)
        order_pay_server = OrderPayService()
        result = order_pay_server.order_pay()
        print("支付结果为:",result)
        self.assertEqual(6000,result.get("account_remain"))

    def test02(self):
        UserService.get_user_amount = mock.Mock(return_value=2000)
        order_pay_server = OrderPayService()
        result = order_pay_server.order_pay()
        print("支付结果为:",result)
        self.assertEqual(0,result.get("account_remain"))

    def test03(self):
        UserService.get_user_amount = mock.Mock(return_value=1999)
        order_pay_server = OrderPayService()
        result = order_pay_server.order_pay()
        print("支付结果为:",result)
        self.assertEqual(1999,result.get("account_remain"))

    def test04(self):
        UserService.get_user_amount = mock.Mock(side_effect = ConnectionAbortedError)
        self.assertRaises(ConnectionAbortedError, UserService.get_user_amount)