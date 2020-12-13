# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:34:06 2020

@author: thesh
"""
# Standard module
import abc
import warnings

# 3rd party's module

# Original module  
from src.interface.warning import (ValueWarning)

class Mediator(object):
    def __init__(self):
        self._pairs = {}
    
    def on_change(self, caller, *args, **kargs):
        print('Mediator Called')
        callee = self._pairs[caller]
        print(callee)
        callee.on_change(*args, **kargs)
    
    def add_caller_callee_pairs(self, caller : 'Caller', callee : 'Callee')\
        -> None:
        if not isinstance(callee, Callee):
            raise TypeError('callee must be instance of Callee')
        elif not isinstance(caller, Caller):
            raise TypeError('caller must be instance of Caller')
        if caller in self._pairs.keys():
            warnings.warn('{} is already assigned to mediator'.format(caller), 
                          ValueWarning)
        
        self._pairs[caller] = callee
        caller.mediator = self         

class Caller(metaclass = abc.ABCMeta): 
    def __init__(self):
        self._mediator = None
        # Public variables
        
    def on_change(self, *args, **kargs) -> None:
        # Call mediator to pass the data to callee.
        
        if self._mediator is not None:
            self._mediator.on_change(self, *args, **kargs)
    
    @property
    def mediator(self) -> Mediator:
        return self._mediator
    
    @mediator.setter
    def mediator(self, _mediator : Mediator ):
        if not isinstance(_mediator, Mediator):
            raise TypeError('Caleer.mediator must be instance of Mediator')
        self._mediator = _mediator

    
class Callee(metaclass = abc.ABCMeta): 
    def on_change(self, *args, **kargs):
        pass