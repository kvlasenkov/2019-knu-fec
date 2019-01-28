import unittest
from gf_operations import add, mult, div

class TestAdd(unittest.TestCase) :
    def test_add(self) :
        self.assertEqual(3, add(1, 2))

class TestMult(unittest.TestCase) :
    def test_mult(self) :
        self.assertEqual(8, mult(2, 4))
    def mult_zero(self) :
        self.assertEqual(0, mult(25, 0))
    def mult_overfield(self) :
        self.assertEqual(248, mult(141, 255))

class TestDiv(unittest.TestCase) :
    def test_div(self) :
        self.assertEqual(4, div(8, 2))
    def div_zero(self) :
        self.assertEqual(0, div(0, 48))
    def div_error(self) :
        self.assertRaises(ZeroDivisionError)
    def div_neg(self) :
        self.assertEqual(13, div(240, 244))

if __name__ == '__main__' :
    unittest.main()
