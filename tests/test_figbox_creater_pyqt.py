# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 13:58:44 2020

@author: thesh
"""

# Standard module
import unittest

# 3rd party's module

# Original module  
from context import src # path setting
from testing_utility.unittest_util import cls_startstop_msg as add_msg

from test_figbox_cmd_bounder import TestFigBoxCreater

from src.GUI.pyqt.pyqt_up_down import (Pyqt_Fig_Box_Creater)
from src.utility.mediator import (Caller, Callee)

@add_msg
class TestCreaterInterfaces(TestFigBoxCreater, unittest.TestCase):
    _FigBoxCreater_class = Pyqt_Fig_Box_Creater

if __name__=='__main__':
    unittest.main()