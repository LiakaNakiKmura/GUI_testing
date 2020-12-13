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
                         (Mediator, 'add_callee_caller_pairs'),
                         (Callee, 'on_change')
                         )
    _class_instanceattr_pairs = ((Caller, 'mediator'), 
                         )

class MockCallee(Callee):
    def on_change(self, *args, **kargs):
        print('Callee Called')
        self.args = args
        self.kargs = kargs


class MockCaller(Caller):
    def on_change(self, *args, **kargs):
        print('Caller Called')
        super().on_change(*args, **kargs)
        
# Test that if Caller call on change, colleage obj is called. 

@add_msg
class TestMediator(unittest.TestCase):
    def setUp(self):
        self.mediator = Mediator()
        self.caller = MockCaller()
        self.callee = MockCallee()
    
    def test_validate_mediator_setup(self):
        bad_data = [0, 'a', [], {1:2}, None, lambda x: 0 ]
        for d in bad_data:
            with self.assertRaises(TypeError):
                self.caller.mediator=d
        self.caller.mediator = self.mediator
    
    def test_mediator_set_pairs(self):
        '''
        Test validation on add_callee_caller_pairs
        '''
        
        class Foo: pass
        f = Foo()
        bad_pairs = ((f,self.caller), (self.callee, f))
        for d in bad_pairs:
            with self.assertRaises(TypeError):
                self.mediator.add_callee_caller_pairs(*d)
        self.mediator.add_callee_caller_pairs(self.callee, self.caller)
        
        # TODO: add test to same caller is not allowed:
        
    def test_mediator_relation(self):
        '''
        Test mediator relations.
        Set up is just pass caller, callee pairs.
        If Caller is on_change with args, kargs, Callee is on_change with args,
        kargs.        
        '''
        self.mediator.add_callee_caller_pairs(self.callee, self.caller)
        input_data = tuple(range(20))
        self.caller.on_change(*input_data)
        self.assertEqual(self.callee.args, input_data)
        
        input_data2 = {chr(65+i):i for i in range(20)}
        self.caller.on_change(**input_data2)
        self.assertEqual(self.callee.kargs, input_data2)
        
    
if __name__=='__main__':
    unittest.main()