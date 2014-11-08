# -*- coding:utf-8 -*-  
#author: luoding
#blog:www.nwber.com
#E-mail: luoding@nwber.com

import unittest
from infix2postfix import Infix2Postfix 
    
class TestInfix2Postfix(unittest.TestCase):
    """ 
    测试infix2postfix.py中Infix2Postfix的中缀表达式转后缀表达式的功能
    """
    def setUp(self):
        self.Infix2Postfix = Infix2Postfix()
    
    def tearDown(self):
        self.infix2postfix = None
    
    def test_infix2postfix1(self):
        self.assertEqual(self.Infix2Postfix.infix2postfix("A * B + C * D"), "A B * C D * +", "test infix2postfix fail")
    
    def test_infix2postfix2(self):
        self.assertEqual(self.Infix2Postfix.infix2postfix(" ( A + B ) * C - ( D - E ) * ( F + G ) "), "A B + C * D E - F G + * -", "test infix2postfix fail")

                    
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestInfix2Postfix("test_infix2postfix1"))
    suite.addTest(TestInfix2Postfix("test_infix2postfix2"))
    runner = unittest.TextTestRunner()
    runner.run(suite)