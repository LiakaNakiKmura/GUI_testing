# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 01:05:39 2020

@author: thesh
"""

# Standard module
import unittest

# 3rd party's module
import numpy as np
from numpy.testing import assert_array_almost_equal

# Original module  
from context import src # path setting
from testing_utility.unittest_util import cls_startstop_msg as add_msg

from src.interface.up_down import (Abs_XY_Calc)
from src.calc.xy_calc import XY_Calc


@add_msg
class TestXYCalc(unittest.TestCase):
    def setUp(self):
        self.xycalc = XY_Calc()
        self.x_step = 1
        self.y_step = 1
        self._max_length = 10
    
    def test_inherited(self):
        self.assertTrue(isinstance(self.xycalc, Abs_XY_Calc))
    
    def test_list(self):
        
        # initial value
        x = np.array([0])
        y = np.array([0])     
        assert_array_almost_equal(self.xycalc.get_xy_list(), (x,y))
        x, y = self._increment_xy(x,y)
        x, y = self._increment_xy(x,y)
        x, y = self._increment_xy(x,y, False)
        x, y = self._increment_xy(x,y)
        x, y = self._increment_xy(x,y)
        x, y = self._increment_xy(x,y, False)
        x, y = self._increment_xy(x,y)
        x, y = self._increment_xy(x,y, False)
        x, y = self._increment_xy(x,y, False)
        x, y = self._increment_xy(x,y, False)
        x, y = self._increment_xy(x,y, False)
        x, y = self._increment_xy(x,y, False)
        x, y = self._increment_xy(x,y)
        x, y = self._increment_xy(x,y)
        x, y = self._increment_xy(x,y, False)
        x, y = self._increment_xy(x,y)
        x, y = self._increment_xy(x,y, False)
        x, y = self._increment_xy(x,y, False)
 
    
    def _increment_xy(self, x, y, sign = True):
        if sign is True:
            s = 1
            self.xycalc.up()
        else:
            s = -1
            self.xycalc.down()
            
        x = self.add_step(x, self.x_step)[-self._max_length:]
        y = self.add_step(y, self.y_step*s)[-self._max_length:]
        assert_array_almost_equal(self.xycalc.get_xy_list(), (x,y))   
        return x, y 

 
    def add_step(self, d_list, step):
        return np.append(d_list, d_list[-1] + step)
    
    
if __name__=='__main__':
    unittest.main()