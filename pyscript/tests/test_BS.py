# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 21:23:35 2020

@author: franklin

"""

import unittest
from BS import euro_vanilla, call_put_parity

class TestBS(unittest.TestCase):

    def setUp(self):
        
        self.bs_param = (50, 100, 1, 0.05, 0.25)
    
    def test_call(self):
        self.assertEqual(euro_vanilla(*self.bs_param), float(0.027352509369436617))
        self.assertAlmostEqual(euro_vanilla(*self.bs_param), float(0.027352509369436617))
        
    def test_put(self):
        self.assertEqual(euro_vanilla(*self.bs_param, option = 'put'), float(45.15029495944084))
        self.assertAlmostEqual(euro_vanilla(*self.bs_param, option = 'put'), float(45.15029495944084))

    def test_parity(self):
        self.assertEqual(call_put_parity(*self.bs_param), float(0.0))
        self.assertAlmostEqual(call_put_parity(*self.bs_param), float(0.0))

if __name__ == '__main__':
    unittest.main()