# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 01:09:14 2020

@author: thesh
"""
# Standard module
import unittest

# 3rd party's module

# Original module  
from context import src # path setting
from testing_utility.unittest_util import cls_startstop_msg as add_msg

from test_interface import TestForMethodExist

from src.interface.up_down import (Abs_UI_Creater,
                                   Abs_Fig_Box_Creater,
                                   Abs_Cmd_Processer)



if __name__=='__main__':
    unittest.main()