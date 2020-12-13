# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 22:32:55 2020

@author: thesh
"""

# Standard module
import unittest

# Original module  
from testing_utility.unittest_util import cls_startstop_msg as add_msg

# targets.
from src.interface.warning import (ValueWarning,
                                   )
@add_msg
class TestValueWarning(unittest.TestCase):
    
    def test_value_warning(self):
        self.assertTrue(issubclass(ValueWarning, UserWarning ))


if __name__=='__main__':
    unittest.main()