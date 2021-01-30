# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 23:44:44 2021

@author: LiNaK
"""

# Standard module
import unittest

# 3rd party's module
from context import src # path setting
from testing_utility.unittest_util import cls_startstop_msg as add_msg
from PyQt5.QtWidgets import (QPushButton, )



# Original module  
from test_interface import TestForMethodExist
from src.GUI.pyqt.utility.qt_interface import (WidgetCreater,)
from src.GUI.pyqt.pyqt_up_down import (ButtonCreater,)


@add_msg
class TestCommandBounderInterfaces(TestForMethodExist, unittest.TestCase):
    def class_attr_pairs_initialize(self):
        self._class_method_pairs=((WidgetCreater, 'get_widget'),
                                  )
        
class Mock_Qt():
    pass

@add_msg
class TestWidgetCreater(unittest.TestCase):
    pass


@add_msg
class TestButtonCreater(unittest.TestCase):
    def setUp(self):
        self.button_creater = ButtonCreater()
        #self.app = QApplication(sys.argv)
    
    def test_button_chk(self):
        button =  self.button_creater.get_widget()
        self.assertTrue(isinstance(button, QPushButton))
    
    def test_inhertance(self):
        self.assertTrue(isinstance(self.button_creater, WidgetCreater))
    
    def test_callee(self):
        pass

if __name__=='__main__':
    unittest.main()

