#!/usr/bin/env python3

""" 
-----------------------------------------------------------------------------------------------
Walk in the Park (WitP) v1.02 - Input a keypad press options and nearest neighbors
-----------------------------------------------------------------------------------------------
WitP is provided by Bernard Avenatti under the MIT License agreement.

Bernard Avenatti
bjavenatti@ualr.edu

Copyright (c) 2022 Bernard Avenatti.  All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software 
and associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute, 
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or 
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT 
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
-----------------------------------------------------------------------------------------------
Classes:
    PasswordCriteria
    PasswordCriteriaBuilder
    PasswordKnowns
    PasswordKnownsBuilder
Functions:
    read_generate_walks
-----------------------------------------------------------------------------------------------
Change Log:
2022.02.01 - Create basic function for generating qwerty keyboard walks. Define classes for input (context) objects.
2022.01.31 - Created version 1.02
-----------------------------------------------------------------------------------------------
"""

import readkeys as rp
import numpy as np

in_type = rp.FileType.CSV
out_type = rp.PythonType.DATAFRAME

keys = rp.read_keys(in_type, out_type, 'keyboard_qwerty.csv')

class PasswordCriteria:
    """
    Structure to hold requirements about passwords.
    """
    def __init__(self):
        pass
    criteria = None
    min_length = None
    max_length = None
    req_numbers = None
    req_special = None
    req_upper = None
    req_lower = None
    omitted = None

class PasswordCriteriaBuilder:
    """
    Construct password criteria object.
    """
    def __init__(self):
        self._passwordcriteria = PasswordCriteria()
        return None

    def set_min_length(self, min_length: int):
        self._passwordcriteria.min_length = min_length
        return self

    def set_max_length(self, max_length: int):
        self._passwordcriteria.max_length = max_length
        return self

    def set_req_numbers(self, req_numbers: int):
        self._passwordcriteria.req_numbers = req_numbers
        return self
    
    def set_req_special(self, req_special: int):
        self._passwordcriteria.req_special = req_special
        return self
    
    def set_req_upper(self, req_upper: int):
        self._passwordcriteria.req_upper = req_upper
        return self

    def set_req_lower(self, req_lower: int):
        self._passwordcriteria.req_lower = req_lower
        return self

    def set_omitted(self, omitted: np.array):
        self._passwordcriteria.omitted = omitted
        return self

    def build(self):
        if self._passwordcriteria is None:
            raise ValueError('PasswordCriteria is empty. Please construct properly.')
        return self._passwordcriteria

class PasswordKnowns:
    """
    Structure to hold any known characters in the password.
    """
    def __init__(self):
        pass
    password = None

class PasswordKnownsBuilder:
    """
    Construct password object.
    """
    def __init__(self):
        self._passwordknowns = PasswordKnowns()
        return None

    def set_pass(self, password: np.array):
        self._passwordknowns.password = password
        return self

    def build(self):
        if self._passwordknowns is None:
            raise ValueError('PasswordKnowns is empty. Please construct properly.')
        return self._passwordknowns

def read_generate_walks(keys, criteria: PasswordCriteria, knowns: PasswordKnowns):
    """
    Consider cyber physical system keyboard input. 
    Consider any known password criteria: length complexity etc.
    Consider any known password portion.

    Args:
        input_type (int): The input file format. Use FileType class.
        output_type (int): The output data type. Use PythonType class.
        file_path (str): Target input file path.
    
    Returns: Specified output_type from parameters.
    """

    # TODO algorithm

    r = None

criteria = PasswordCriteriaBuilder().set_min_length(10).set_max_length(18).build()
hints = PasswordKnownsBuilder().set_pass(np.array(['1', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])).build()

read_generate_walks(keys, criteria, hints)

