# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:35:57 2020

@author: thesh
"""

# Standard module
import abc

# 3rd party's module

# Original module
from src.utility.mediator import (Caller, Callee)

class Abs_XY_Graph_Creater(metaclass = abc.ABCMeta):
    _canvas = None
    @abc.abstractmethod
    def get_up_caller(self):
        pass
    
    @abc.abstractmethod
    def get_down_caller(self):
        pass
    
    @property
    def canvas(self):
        return self._canvas
    
class Abs_XY_Calc(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def up(self):
        pass
    
    @abc.abstractmethod
    def down(self):
        pass
    
    @abc.abstractmethod
    def get_xy_list(self):
        pass
    
class Abs_UI_Creater(metaclass = abc.ABCMeta):
    _canvas = None
    
    @abc.abstractmethod
    def up_mediated(self):
        pass
    
    @abc.abstractmethod
    def down_mediated(self):
        pass
    
    @property
    def canvas(self):
        return self._canvas
    
    @canvas.setter
    def canvas(self, canvas):
        self._validate_canvas(canvas)
        self._canvas = canvas
    
    @abc.abstractmethod
    # Validation Canvas object that is the graph object.
    def _validate_canvas(self, canvas):
        pass

class Abs_Fig_Box_Creater(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def get_fig_updater(self) -> Callee: 
        pass
    
    @abc.abstractmethod
    def get_up_caller(self) -> Caller:
        pass
    
    @abc.abstractmethod
    def get_down_caller(self) -> Caller:
        pass

class Abs_Cmd_Processer(metaclass = abc.ABCMeta):pass