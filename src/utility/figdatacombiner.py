# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 18:02:02 2021

@author: thesh
"""
# Standard module

# 3rd party's module
import numpy as np

# Original module  

from src.utility.mediator import (Caller)


class FigDataInputer(Caller):
    '''
    Validate and Update the data to figure graph.
    set_graph_data: set x,y graph data. This validate x, y data.
    update_graph: Update graph to call by mediator
    '''
    
    def set_graph_data(self, x : np.ndarray, y : np.ndarray) -> None:
        '''
        x, y data is set in this instance but not update yet.
        
        Parameters
        ----------
        x : np.ndarray (1D)
        y : np.ndarray (1D)
        
        size of x and y must be the same.

        Returns
        -------
        None.

        '''
        
        self._validate_data(x,y)
        self._x = x
        self._y = y
    
    def update_graph(self):
        '''
        Update graph. the graph data is needed to be set by set_graph_data 
        before calle this method.

        Returns
        -------
        None.

        '''
        self.on_change(x = self._x, y = self._y)
    
    def _validate_data(self,x,y):
        '''
        Validate x and y 
        the followings is checked if not raise type error.
        Is type of np.ndarray?
        Is the dimension of x and y is 1D?
        Is the length of x, y is the same?

        '''
        
        for data in (x,y):
            if type(data) is not np.ndarray:
                raise TypeError('x, y must be numpy.ndarray')
            elif data.ndim != 1:
                raise ValueError('The dimension of input data must be 1D.')
        
        if x.shape != y.shape:
                raise ValueError('the shape of x and y is differet.')
            