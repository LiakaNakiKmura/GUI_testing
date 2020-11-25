# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:15:52 2020

@author: thesh
"""

# 3rd party's module

# Original module  
from context import src # path setting
from src.plot.graph import XY_Graph_Creater
from src.calc.xy_calc import XY_Calc
from src.GUI.updown_graph import XY_UI_Creater
from src.utility.mediator import Mediator

#interfaces
from src.interface.up_down import (Abs_XY_Graph_Creater, 
                                     Abs_XY_Calc,
                                     Abs_UI_Creater)


class UpDown_Graph_Maker():
    def __init__(self):
        self._create_instances()
    
    def _create_instances(self):
        self._xycalc = XY_Calc()
        self._graph =XY_Graph_Creater()
        self._ui = XY_UI_Creater()
        self._mediator = Mediator()
    
    
    def _set_relations(self):
        self._graph.set_xylist(self._xycalc)
        # graph get xy data from  xycalc.
        self._ui.canvas = self._graph.canvas
        # ui add canvas(graph).
        
        
    def _set_mediator(self):
        pairs = [(self._ui.up_mediated, self._graph.up_caller),
                 ]
        
        self.mediator.add_pairs()
        
    
    def run(self):
        self._ui.run()
    
if __name__ == '__main__':
    updown = UpDown_Graph_Maker()
    updown.run()