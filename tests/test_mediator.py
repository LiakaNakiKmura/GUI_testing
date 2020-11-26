# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 01:17:22 2020

@author: thesh
"""

# Standard module
import unittest
from unittest.mock import patch

# 3rd party's module
import numpy as np
from numpy.testing import assert_array_almost_equal

# Original module  
from context import src # path setting
from testing_utility.unittest_util import cls_startstop_msg as add_msg

from test_interface import TestForMethodExist
from src.utility.mediator import Mediated

@add_msg
class TestCreaterInterfaces(TestForMethodExist, unittest.TestCase):
    _class_method_pairs=((Mediated,'on_change'),
                         )

if __name__=='__main__':
    unittest.main()