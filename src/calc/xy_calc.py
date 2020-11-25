# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 01:09:42 2020

@author: thesh
"""

import numpy as np

from context import src # path setting
from src.interface.up_down import (Abs_XY_Calc)


class XY_Calc(Abs_XY_Calc):
    _xstep = 1
    _ystep = 1
    _max_l = 10
     
    def __init__(self):
        self._x = np.array([0])
        self._y = np.array([0])
    
    def up(self):
        self._increment_xy(True)
    
    def down(self):
        self._increment_xy(False)
    
    def get_xy_list(self):
        return self._x, self._y
    
    def _increment_xy(self, sign = True):
        if sign is True:
            s = 1
        else:
            s= -1
            
        self._x = np.append(self._x, self._x[-1] + self._xstep)[-self._max_l:]
        self._y = np.append(self._y, self._y[-1] + s*self._ystep)[-self._max_l:]
    