# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 01:17:22 2020

@author: thesh
"""

# Standard module
import unittest
from unittest.mock import patch

# 3rd party's module
import numpy as np
from numpy.testing import assert_array_almost_equal

# Original module  
from context import src # path setting
from testing_utility.unittest_util import cls_startstop_msg as add_msg

from test_interface import TestForMethodExist
from src.utility.mediator import (Caller, Mediator, Callee)

@add_msg
class TestMediatorInterfaces(TestForMethodExist, unittest.TestCase):
    _class_method_pairs=((Caller,'on_change'),
                         (Mediator, 'on_change'),
                         (Callee, 'on_change')
                         )
    _class_instanceattr_pairs = ((Caller, 'mediator'), 
                         )

class MockCallee(Callee):
    def on_change(self, *args, **kwargs):
        self.ca(*args,**kwargs)


# Test that if Caller call on change, colleage obj is called. 

@add_msg
class TestMediator(unittest.TestCase):
    def setUp(self):
        self.mediator = Mediator()
        self.caller = Caller()
    
    def test_validate_mediator_setup(self):
        bad_data = [0, 'a', [], {1:2}, None, lambda x: 0 ]
        for d in bad_data:
            with self.assertRaises(TypeError):
                self.caller.mediator=d
        self.caller.mediator = self.mediator
    
if __name__=='__main__':
    unittest.main()