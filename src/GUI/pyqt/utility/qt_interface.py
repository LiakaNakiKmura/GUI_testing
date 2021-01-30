# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 23:50:01 2021

@author: LiNaK
"""

# Standard module
import abc

# 3rd party's module

# Original module  


class WidgetCreater(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def get_widget(self): 
        pass
