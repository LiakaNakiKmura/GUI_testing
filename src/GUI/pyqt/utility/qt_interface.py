# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 23:50:01 2021

@author: LiNaK
"""

# Standard module
import abc

# 3rd party's module
from PyQt5.QtWidgets import (QWidget, )

# Original module  


class WidgetCreater(metaclass = abc.ABCMeta):
    def __init__(self, parent = None):
        if parent is not None:
            self._validate_parent(parent)
        self._parent = parent
        # parent qt instance that will be set to widget.
    
    @abc.abstractmethod
    def get_widget(self): 
        pass
    
    @property
    def parent(self) -> QWidget:
        return self._parent
    
    @parent.setter
    def parent(self, parent : QWidget) -> None:
        self._validate_parent(parent)
        self._parent = parent
    
        
    def _validate_parent(self, parent):
        if not isinstance(parent, QWidget):
            raise TypeError('parent must be instance of parent.')
        
        if not parent.isWindow():
            raise TypeError('parent must be window.')
