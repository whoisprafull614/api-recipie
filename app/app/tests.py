"""Test to check calc"""
from django.test import SimpleTestCase
from app import calc
class CalcTest(SimpleTestCase):
    
    "Test to check calc Module"
    def test_calc(self):
        "Testing Adding two Numbers"
        res = calc.AddTwo(5,6);
        self.assert_equal(res,11)