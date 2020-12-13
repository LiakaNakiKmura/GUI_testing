# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:34:06 2020

@author: thesh
"""
# Standard module
import abc

# 3rd party's module

# Original module  

class Mediator(object):
    def on_change(self):
        pass

class Caller(metaclass = abc.ABCMeta): 
    def __init__(self):
        self._mediator = None
        # Public variables
        
    def on_change(self) -> None:
        pass
    
    @property
    def mediator(self) -> Mediator:
        return self._mediator
    
    @mediator.setter
    def mediator(self, _mediator : Mediator ):
        if not isinstance(_mediator, Mediator):
            raise TypeError('Caleer.mediator must be instance of Mediator')
        self._mediator = _mediator

    
class Callee(metaclass = abc.ABCMeta): 
    def on_change(self):
        pass
    
class Foo:
    @property
    def x(self, var):
        assert ()