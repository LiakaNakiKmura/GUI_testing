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

from src.interface.up_down import (Abs_Fig_Box_Creater,
                                   Abs_Cmd_Processer)
from src.utility.mediator import (Caller, Callee)


@add_msg
class TestCommandBounderInterfaces(TestForMethodExist, unittest.TestCase):
    _class_method_pairs=((Abs_Fig_Box_Creater, 'get_fig_updater'),
                         (Abs_Fig_Box_Creater, 'get_up_caller'),
                         (Abs_Fig_Box_Creater, 'get_down_caller'),
                         )


class TestFigBoxCreater(object):
    '''
    Test FigboxCreater class. This class will be inherited to test the concrete
    class of FigboxCreater.
    '''
    _FigBoxCreater_class = None
    
    def test_inheritance(self):
        # Target class is Abs_Fig_Box_Creater.
        self.assertTrue(issubclass(self._FigBoxCreater_class, Abs_Fig_Box_Creater))
    
    def test_inheritance_of_getter(self):
        # figbox ccreater returns Callee and Caller.
        figbox = self._FigBoxCreater_class()
        self.assertTrue(isinstance(figbox.get_fig_updater(), Callee))
        self.assertTrue(isinstance(figbox.get_up_caller(), Caller))
        self.assertTrue(isinstance(figbox.get_down_caller(), Caller))

class TestCMD_PRCR(object):
    '''
    Test FigboxCreater class. This class will be inherited to test the concrete
    class of FigboxCreater.
    '''
    _CMD_PRCR_class = None
    
    def test_inheritance(self):
        # Target class is Abs_Fig_Box_Creater.
        self.assertTrue(issubclass(self._CMD_PRCR_class, Abs_Cmd_Processer))
    
    def test_inheritance_of_getter(self):
        # Command processer returns Callee and Caller.
        cmd_pro = self._CMD_PRCR_class()
        self.assertTrue(isinstance(cmd_pro.get_graph_update(), Caller))
        self.assertTrue(isinstance(cmd_pro.get_up_cmd(), Callee))
        self.assertTrue(isinstance(cmd_pro.get_down_cmd(), Callee))

if __name__=='__main__':
    unittest.main()