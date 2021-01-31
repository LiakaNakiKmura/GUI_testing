# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 23:44:44 2021

@author: LiNaK
"""

# Standard module
import unittest
import sys

# 3rd party's module
from context import src # path setting
from testing_utility.unittest_util import cls_startstop_msg as add_msg
from PyQt5.QtWidgets import (QPushButton, QMainWindow, QWidget, QApplication)
from PyQt5.QtCore import QObject


# Original module  
from test_interface import TestForMethodExist
from src.GUI.pyqt.utility.qt_interface import (WidgetCreater,)
from src.GUI.pyqt.pyqt_up_down import (ButtonCreater,)


class MockWidgetCreater(WidgetCreater):    
    def get_widget(self):
        pass


@add_msg
class TestCommandBounderInterfaces(TestForMethodExist, unittest.TestCase):
    def class_attr_pairs_initialize(self):
        self._class_method_pairs=((WidgetCreater, 'get_widget'),
                                  )
        self._class_instanceattr_pairs = ((MockWidgetCreater, 'parent'), 
                                          )
        
class Mock_MainWindow(QMainWindow):
    pass

@add_msg
class TestWidgetCreater(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.parent = Mock_MainWindow()
        self._target = MockWidgetCreater
    
    def test_set_parent(self):
        mock_widget_creater = self._target()
        mock_widget_creater.parent = self.parent
        self.assertTrue(mock_widget_creater.parent, self.parent)
        #parent is set by property.
        
        mock_widget_creater = self._target(self.parent)
        self.assertTrue(mock_widget_creater.parent, self.parent)
        #parent can be set at contraction.
        
        mock_widget_creater = self._target(self.parent)
        parent2 = Mock_MainWindow()
        mock_widget_creater.parent = parent2
        self.assertTrue(mock_widget_creater.parent, parent2)
        #parent will be overwritten at 2nd input.
        
        def wrong_set_Raise(wrong_value):
            def set_property(wrong_value):
                mock_widget_creater = self._target()
                mock_widget_creater.parent = wrong_value
            
            def set_init(wrong_value):
                mock_widget_creater = self._target(parent = wrong_value)
                
            self.assertRaises(TypeError, set_property, wrong_value)
            self.assertRaises(TypeError, set_init, wrong_value)
        
        wrong_set_Raise(1)
        wrong_set_Raise('abc')
        wrong_set_Raise(QObject)
        wrong_set_Raise(QObject())
    

@add_msg
class TestButtonCreater(unittest.TestCase):
    def setUp(self):
        self.button_creater = ButtonCreater()
    
    
    def _test_button_chk(self):
        button =  self.button_creater.get_widget()
        self.assertTrue(isinstance(button, QPushButton))
    
    def test_inhertance(self):
        self.assertTrue(isinstance(self.button_creater, WidgetCreater))
    
    def test_callee(self):
        pass

if __name__=='__main__':
    unittest.main()

