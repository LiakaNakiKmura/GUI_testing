# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 18:02:02 2021

@author: thesh
"""
# Standard module

# 3rd party's module

# Original module  

from src.utility.mediator import (Caller)


class FigDataInputer(Caller):
    '''
    '''
    
    def set_graph_data(self, x, y):
        '''
        

        Parameters
        ----------
        x : TYPE
            DESCRIPTION.
        y : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        self._x = x
        self._y = y
    
    def update_graph(self):
        self.on_change(x = self._x, y = self._y)