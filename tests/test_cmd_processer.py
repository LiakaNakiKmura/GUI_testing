# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 20:52:08 2020

@author: thesh
"""

# Standard module
import unittest

# 3rd party's module

# Original module  
from context import src # path setting
from testing_utility.unittest_util import cls_startstop_msg as add_msg

from test_figbox_cmd_bounder import TestCMD_PRCR

from src.app.cmd import (Up_Down_CMD_PRCR)
from src.utility.mediator import (Caller, Callee)

@add_msg
class TestCMD_PRCR_interface(TestCMD_PRCR, unittest.TestCase):
    def overwrite_in_inherated_class(self):
        self._CMD_PRCR_class = Up_Down_CMD_PRCR
    
    
@add_msg
class TestCMD_PRCR(unittest.TestCase):
    def test_DataInpter(self):
        pass
    pass

if __name__=='__main__':
    unittest.main()