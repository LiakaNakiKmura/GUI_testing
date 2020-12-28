# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 16:02:25 2020

@author: thesh
"""

# Standard module

# 3rd party's module

# Original module
from src.interface.up_down import Abs_Fig_Box_Creater
from src.utility.mediator import (Caller, Callee)


class Pyqt_Fig_Box_Creater(Abs_Fig_Box_Creater):
    def __init__(self):
        self._updater = PyQtFigUpdater()
        self._up_caller = UpCaller()
        self._down_caller = PyQtDownCaller()
        
    def get_fig_updater(self):
        return self._updater
    
    def get_up_caller(self):
        return self._up_caller
    
    def get_down_caller(self):
        return self._down_caller

class PyQtFigUpdater(Callee):
    pass

class UpCaller(Caller):
    pass

class PyQtDownCaller(Caller):
    pass