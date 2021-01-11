# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 01:09:14 2020

@author: thesh
"""
# Standard module
import unittest
from unittest.mock import patch

# 3rd party's module
import numpy as np

# Original module  
from context import src # path setting
from testing_utility.unittest_util import cls_startstop_msg as add_msg

from test_interface import TestForMethodExist

from src.interface.up_down import (Abs_Fig_Box_Creater,
                                   Abs_Cmd_Processer)
from src.utility.mediator import (Caller, Callee, Mediator)
from src.utility.figdatacombiner import (FigDataInputer)
from test_mediator import MockCallee


@add_msg
class TestCommandBounderInterfaces(TestForMethodExist, unittest.TestCase):
    _class_method_pairs=((Abs_Fig_Box_Creater, 'get_fig_updater'),
                         (Abs_Fig_Box_Creater, 'get_up_caller'),
                         (Abs_Fig_Box_Creater, 'get_down_caller'),
                         (Abs_Cmd_Processer, 'get_fig_data_inputer'),
                         (Abs_Cmd_Processer, 'get_up_cmd'),
                         (Abs_Cmd_Processer, 'get_down_cmd')
                         )



class TestFigBoxCreater(object):
    '''
    Test FigboxCreater class. This class will be inherited to test the concrete
    class of FigboxCreater.
    '''
    _FigBoxCreater_class = None
    
    def test_inheritance(self):
        # Target class is Abs_Fig_Box_Creater.
        self.assertTrue(issubclass(self._FigBoxCreater_class, Abs_Fig_Box_Creater))
    
    def test_inheritance_of_getter(self):
        # figbox ccreater returns Callee and Caller.
        figbox = self._FigBoxCreater_class()
        self.assertTrue(isinstance(figbox.get_fig_updater(), Callee))
        self.assertTrue(isinstance(figbox.get_up_caller(), Caller))
        self.assertTrue(isinstance(figbox.get_down_caller(), Caller))

class TestCMD_PRCR(object):
    '''
    Test FigboxCreater class. This class will be inherited to test the concrete
    class of FigboxCreater.
    '''
    _CMD_PRCR_class = None
    
    def setUp(self):
        self.cmd_pro = self._CMD_PRCR_class()
        
    
    def test_inheritance(self):
        # Target class is Abs_Fig_Box_Creater.
        self.assertTrue(issubclass(self._CMD_PRCR_class, Abs_Cmd_Processer))
    
    def test_inheritance_of_getter(self):
        # Command processer returns Callee and Caller.
        # TODO: ADD inheritance
        #self.assertTrue(isinstance(self.cmd_pro.get_fig_data_inputer(), 
        #                           FigDataInputer))
        self.assertTrue(isinstance(self.cmd_pro.get_up_cmd(), Callee))
        self.assertTrue(isinstance(self.cmd_pro.get_down_cmd(), Callee))



class Test_FigBox_CombinedTest():
    '''
    fig data inputer must be instance of FigDataInputer
    '''
    
    def setUp(self):
        self.overwrite_in_inherated_class()
        self.get_fdi_from_cmd_pro()
        
    def overwrite_in_inherated_class(self):
        '''
        overwrite this method in inherated class to set target class or method
        or etc... to test.
        '''        
        self._CMD_PRCR_class = None # Command Processer class
        
    def get_fdi_from_cmd_pro(self):
        cmd_pro = self._CMD_PRCR_class()
        self.fdi = cmd_pro.get_fig_data_inputer()
        
    def test_inheritance_of_FigDataInputer(self):
        self.assertTrue(isinstance(self.fdi, FigDataInputer))


class TestFigDataInputer(unittest.TestCase):
        
    
    def setUp(self):
        self.create_instances()
        self.create_common_val()
 
    def create_instances(self):
        self.fdi = FigDataInputer()
        self.mock_callee = MockCallee()
        mediator = Mediator()
        mediator.add_caller_callee_pairs(self.fdi, self.mock_callee)
    
    def create_common_val(self):
        self._x_arg_name = 'x' 
        # x argument name from Fig Data inputer to Fig Updater. 
        
        self._y_arg_name = 'y' 
        # y argument name from Fig Data inputer to Fig Updater.
        
        
    def test_inheritance_of_FigDataInputer(self):
        self.assertTrue(issubclass(FigDataInputer, Caller))
        
    def test_input_data_validation(self):
        pass
    
    def test_input_data_pass_to_callee(self):
        pass
    
    """
    def _test_fig_data_inputer_value(self):
        '''
        fdi pass the data of x, y data.
        x is np.ndarray
        y is np.ndarray
        
        Callee get (x, y) data.
        '''
        number_of_data = 2 # x and y
        
        self.set_graph_data()
        self.fdi.update_graph()
        
        if len(self.mock_callee.args) > 0:
            data = self.mock_callee.args
            self.assertTrue(len(data) == number_of_data)
            self.check_data_val(data)
        
        else:
            data = self.mock_callee.kargs
            self.assertTrue(len(data) == number_of_data)
            self.assertTrue(self.x_arg_name in data.keys())
            self.assertTrue(self.y_arg_name in data.keys())
            self.check_data_val(data[self.x_arg_name, self.y_arg_name])
    
    def get_data_from_mock_callee(self):
        # get data passed from fig data inputer to mock callee
        
        number_of_data = 2 # x and y
        args = self.mock_callee.args
        kargs = self.mock_callee.kargs
    
        
        if len(args) > 0:
            self.assertTrue(len(args) == number_of_data)
            self._x_data = args[0]
            self._y_data = args[1]
        
        elif len(kargs) > 0 :
            self.assertTrue(len(kargs) == number_of_data)
            self._x_data = kargs[self._x_arg_name]
            self._y_data = kargs[self._y_arg_name]
            
        else:
            self.fail('correct data is not input')
        
    
    def check_data_val(self):
        for data in (self._x_data, self._y_data):
            # Data must be ndarray data.
            self.assertTrue(isinstance(data, np.ndarray))          
                
            # Data must be 1D (not matrix).
            self.assertTrue(data.ndim == 1 )
                
        # Data length must be same between x, y
        self.assertTrue(self._x_data.shape == self._y_data.shape)
    """

@add_msg
class TestFigDataInputer_instance(TestForMethodExist, unittest.TestCase):
    _class_method_pairs=((FigDataInputer, 'set_graph_data'),
                         (FigDataInputer, 'update_graph')
                         )




if __name__=='__main__':
    unittest.main()