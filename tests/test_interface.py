# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 21:34:32 2019

@author: LiNaK
This is the test for interface classes which has specific abstract method.

"""

# Standard module
import unittest
from unittest.mock import patch

# 3rd party's module

# Original module  
from context import src # path setting
from testing_utility.unittest_util import cls_startstop_msg as add_msg

# targets.
from src.interface.up_down import (Abs_XY_Graph_Creater, 
                                   Abs_XY_Calc,
                                   Abs_UI_Creater,
                                   Abs_Fig_Box_Creater,
                                   Abs_Cmd_Processer)

class TestForMethodExist():
    '''
    Check that class has specified method for especially abstract class.    
    '''
    
    def class_attr_pairs_initialize(self):
        '''
        Over write this method in inherated class.
        
        These lists of pairs will be tested.
        If you don't needed to test these varialbe. you don't needed to set.
        _class_method_pairs is set as ((class1, mrthod1),(class2, method2)...)
        _class_attr_pairs is set as ((class1, attribute1),(class2, attribute2)...)
        _class_instanceattr_pairs is set as ((class1, attribute1),(class2, attribute2)...)

        '''
        self._class_method_pairs =(())
        # class and method pairs. If method is not existed in class, raise error.
        
        self._class_attr_pairs = (())
        # class and class attribute pairs. Attribute must be defined in class
        # not in instance.
        
        self._class_instanceattr_pairs = (())
        # class and instance's attribute pairs. Attribute must be defined in 
        # 'instance'. These attribute can be possible that is not exist in class.        
    
    def setUp(self):
        self.set_null_pairs()
        self.class_attr_pairs_initialize()
        
    def set_null_pairs(self):
        '''
        set null pairs to prevent to undefine the variable.
        '''
        self._class_method_pairs =(())
        self._class_attr_pairs = (())
        self._class_instanceattr_pairs = (())
    
    
    def test_class_method_pairs(self):
        for cl, mth in self._class_method_pairs:
            self.assertTrue(callable(getattr(cl, mth)))
    
    def test_class_attr_pairs(self):
        for cl, attr in self._class_attr_pairs:
            self.assertTrue(hasattr(cl, attr))

    def test_instance_attr_pairs(self):
        for cl, attr in self._class_instanceattr_pairs:
            self.assertTrue(hasattr(cl(), attr))



@add_msg
class TestCreaterInterfaces(TestForMethodExist, unittest.TestCase):
    def class_attr_pairs_initialize(self):
        self._class_method_pairs=((Abs_XY_Graph_Creater,'get_up_caller'),
                                  (Abs_XY_Graph_Creater,'get_down_caller'),
                                  (Abs_UI_Creater, 'up_mediated'),
                                  (Abs_UI_Creater, 'down_mediated'),
                                  (Abs_XY_Calc, 'up'),
                                  (Abs_XY_Calc, 'down'),
                                  (Abs_XY_Calc, 'get_xy_list')
                                  )
        self._class_attr_pairs = ((Abs_UI_Creater, 'canvas'), # Property object.
                                  (Abs_XY_Graph_Creater, 'canvas')
                                  )

    

    
    
if __name__=='__main__':
    unittest.main()