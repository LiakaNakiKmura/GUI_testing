# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 01:17:22 2020

@author: thesh
"""

# Standard module
import unittest

# 3rd party's module

# Original module  
from context import src # path setting
from testing_utility.unittest_util import cls_startstop_msg as add_msg

from test_interface import TestForMethodExist
from src.utility.mediator import (Caller, Mediator, Callee)
from src.interface.warning import (ValueWarning)

@add_msg
class TestMediatorInterfaces(TestForMethodExist, unittest.TestCase):
    _class_method_pairs=((Caller,'on_change'),
                         (Mediator, 'on_change'),
                         (Mediator, 'add_caller_callee_pairs'),
                         (Callee, 'on_change')
                         )
    _class_instanceattr_pairs = ((Caller, 'mediator'), 
                         )

class MockCallee(Callee):
    def on_change(self, *args, **kargs):
        self.args = args
        self.kargs = kargs


class MockCaller(Caller):
    def on_change(self, *args, **kargs):
        super().on_change(*args, **kargs)
        
# Test that if Caller call on change, colleage obj is called. 

@add_msg
class TestMediator(unittest.TestCase):
    def setUp(self):
        self.mediator = Mediator()
        self.caller = MockCaller()
        self.callee = MockCallee()
    
    def test_validate_mediator_setup(self):
        '''
        caller.mediator must be instance of Mediator.
        '''
        
        bad_data = [0, 'a', [], {1:2}, None, lambda x: 0 ]
        for d in bad_data:
            with self.assertRaises(TypeError):
                self.caller.mediator=d
        self.caller.mediator = self.mediator
    
    def test_mediator_set_pairs(self):
        '''
        Test validation on add_caller_callee_pairs.
        caller must be instance of Caller
        callee must be instance of Callee
        '''
        
        class Foo: pass
        f = Foo()
        bad_pairs = ((f,self.callee), (self.caller, f))
        for d in bad_pairs:
            with self.assertRaises(TypeError):
                self.mediator.add_caller_callee_pairs(*d)
        self.mediator.add_caller_callee_pairs(self.caller, self.callee)
    
    def test_mediator_repeat_set_pairs(self):
        '''
        Overwrite pairs if same caller is set to mediator.
        Raise waring Overwrote pairs.
        '''
        self.mediator.add_caller_callee_pairs(self.caller, self.callee)
        input_data1 = ('1st call',)
        self.caller.on_change(*input_data1)
        self.assertEqual(self.callee.args, input_data1)
        
        new_callee = MockCallee()
        
        # Test overwrite.
        with self.assertWarns(ValueWarning):
            self.mediator.add_caller_callee_pairs(self.caller, new_callee)
        input_data2 = ('2nd call',)
        self.caller.on_change(*input_data2)
        self.assertEqual(new_callee.args, input_data2)
        
        
    def test_mediator_relation(self):
        '''
        Test mediator relations.
        Set up is just pass caller, callee pairs.
        If Caller is on_change with args, kargs, Callee is on_change with args,
        kargs.        
        '''
        self.mediator.add_caller_callee_pairs(self.caller, self.callee)
        input_data = tuple(range(20))
        self.caller.on_change(*input_data)
        self.assertEqual(self.callee.args, input_data)
        
        input_data2 = {chr(65+i):i for i in range(20)}
        self.caller.on_change(**input_data2)
        self.assertEqual(self.callee.kargs, input_data2)
        
    
if __name__=='__main__':
    unittest.main()