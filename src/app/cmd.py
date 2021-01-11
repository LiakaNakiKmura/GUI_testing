# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 20:55:31 2020

@author: thesh
"""
# Standard module

# 3rd party's module

# Original module  
from src.interface.up_down import (Abs_Cmd_Processer)
from src.utility.mediator import (Caller, Callee)

class Up_Down_CMD_PRCR(Abs_Cmd_Processer):
    def __init__(self):
        self._fig_data_inputer = FigDataInputer()
        self._up_cmd = UpCmd()
        self._down_cmd = DownCmd()
        
    
    def get_fig_data_inputer(self) -> Caller: 
        return self._fig_data_inputer
        
    def get_up_cmd(self) -> Callee: 
        return self._up_cmd
        
    def get_down_cmd(self) -> Callee: 
        return self._down_cmd

class FigDataInputer(Caller):pass
class UpCmd(Callee):pass
class DownCmd(Callee):pass