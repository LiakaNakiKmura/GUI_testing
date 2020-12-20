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
    '''
    This mediate from caller to callee.
    User set caller and callee pairs.
    If caller is on_change mediator will call callee.
    '''
    def __init__(self):
        self._pairs = {}
    
    def on_change(self, caller, *args, **kargs):
        callee = self._pairs[caller]
        callee.on_change(*args, **kargs)
    
    def add_caller_callee_pairs(self, caller : 'Caller', callee : 'Callee')\
        -> None:
        '''
        Parameters
        ----------
        caller : 'Caller'
            instance of Caller object. This calls mediator.on_change 
        callee : 'Callee'
            instance of Callee object. This is called if caller is on_change

        Returns
        -------
        None
        '''
        self._validate_caller(caller)   
        self._validate_callee(callee)
             
        self._pairs[caller] = callee
        caller.mediator = self
        
    def _validate_callee(self, callee : 'Callee') -> None:
        if not isinstance(callee, Callee):
            raise TypeError('callee must be instance of Callee')
    
    def _validate_caller(self, caller : 'Caller') -> None:
        '''
        caller must be instance of Caller.
        Warn if caller is already exist in self._pairs.
        '''
        
        if not isinstance(caller, Caller):
            raise TypeError('caller must be instance of Caller')
        if caller in self._pairs.keys():
            warnings.warn('{} is already assigned to mediator'.format(caller), 
                          ValueWarning)
            

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