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
from numpy.testing import assert_array_equal

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


@add_msg
class TestFigDataInputer_instance(TestForMethodExist, unittest.TestCase):
    _class_method_pairs=((FigDataInputer, 'set_graph_data'),
                         (FigDataInputer, 'update_graph')
                         )

@add_msg
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
        '''
        FigDataInputer allows following inputs
        x: np.ndarray (1D)
        y: np.ndarray (1D)
        number of x is the same as one of y.
        '''
        
        length = 5
        inputkargs_data =[]
        
        # name error
        inputkargs_data.append([TypeError,\
                                {'wrong name':np.random.rand(length),
                                 self._y_arg_name:np.random.rand(length)}])
        
        # wrong input data number
        inputkargs_data.append([TypeError,\
                                {self._x_arg_name:np.random.rand(length),
                                 self._y_arg_name:np.random.rand(length),
                                 'wrong name':np.random.rand(length)}])
        
        
        # wrong data types1
        inputkargs_data.append([TypeError,\
                               {self._x_arg_name:1,
                                self._y_arg_name:np.random.rand(length)}])
        inputkargs_data.append([TypeError,\
                                {self._x_arg_name:np.random.rand(length), 
                                 self._y_arg_name:[3,4,5]}])
        
        # wrong length data
        inputkargs_data.append([ValueError,\
                                {self._x_arg_name:np.random.rand(length), 
                                 self._y_arg_name:np.random.rand(length+3)}])
        
        # set2D data
        inputkargs_data.append([ValueError,\
                                {self._x_arg_name:np.random.rand(length, length),
                                 self._y_arg_name:np.random.rand(length, length)}])

        
        for error, inputkargs in inputkargs_data:
            self.input_data_with_error(error, **inputkargs)
                
    
    def input_data_with_error(self, error, *args, **kargs):
        self.assertRaises(error, self.fdi.set_graph_data,*args, **kargs)
    
    def test_input_data_pass_to_callee(self):
        '''
        If correct data is set to FigureDataInputer and updated, mock callee 
        get data.
        '''
        
        length = 10
        x = np.arange(length)
        y = np.arange(length)**2 
        
        # Check args set case.
        self.fdi.set_graph_data(x,y)
        self.updata_and_check_data(x, y)
        
        # Check kargs set case.
        data = {self._x_arg_name:x, self._y_arg_name:y}
        self.fdi.set_graph_data(**data)
        self.updata_and_check_data(x, y)
        
    
    def updata_and_check_data(self, x, y):
        self.fdi.update_graph()
        data = self.mock_callee.kargs
        assert_array_equal(data[self._x_arg_name], x)
        assert_array_equal(data[self._y_arg_name], y)

if __name__=='__main__':
    unittest.main()