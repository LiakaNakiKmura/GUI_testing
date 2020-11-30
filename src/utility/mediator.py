# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:34:06 2020

@author: thesh
"""

class Mediator():
    pass

class Mediated: 
    def __init__(self):
        self.mediator = None
        print(self.mediator)
        # Public variable.
        # 
        
    def on_change(self):
        pass