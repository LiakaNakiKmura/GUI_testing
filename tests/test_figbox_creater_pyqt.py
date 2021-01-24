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
from test_interface import TestForMethodExist

@add_msg
class TestCreaterInterfaces(TestFigBoxCreater, unittest.TestCase):
    
    def overwrite_in_inherated_class(self):
        self._FigBoxCreater_class = Pyqt_Fig_Box_Creater


@add_msg
class TestCommandBounderInterfaces(TestForMethodExist, unittest.TestCase):
    def class_attr_pairs_initialize(self):
        self._class_method_pairs=((Pyqt_Fig_Box_Creater, 'get_fig_updater'),
                                  )


if __name__=='__main__':
    unittest.main()