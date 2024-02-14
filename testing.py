import unittest
from testmutl import *

class Multiply(unittest.TestCase):
    def test_mult_1(self):
        self.assertEqual(multiply(4,5),20)
    def test_mult_2(self):
        self.assertEqual(multiply(4,5),110)
    def test_mult_3(self):
        self.assertEqual(multiply('4','5'),20)
    
unittest.main()