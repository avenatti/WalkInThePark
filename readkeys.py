#!/usr/bin/env python3

""" 
-----------------------------------------------------------------------------------------------
Read Pin Pad (rp) v1.02 - Input a keypad press options and nearest neighbors
-----------------------------------------------------------------------------------------------
Read Pin Pad is provided by Bernard Avenatti under the MIT License agreement.

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
    FileType
    PythonType

Functions:
    read_pin
-----------------------------------------------------------------------------------------------
Change Log:
2022.01.31 - Created version 1.02
-----------------------------------------------------------------------------------------------
"""

import sys
import xmltodict
import pandas as pd


class FileType:
    """
    Enum to describe expected file type.
    XML = 1
    """

    # TODO support pickle, yaml, etc
    # XML= 1
    CSV = 1
    # PICKLE = 3
    # JSON = 4
    # YAML = 5


class PythonType:
    """
    Enum to describe expected file type.
    DICTIONARY = 1
    """
    # TODO support pandas etc
    # DICTIONARY = 1
    DATAFRAME = 1

  
def read_keys(input_type, output_type, file_path):
    """
    Transform the supplied file into a pickled object file.

    Args:
        input_type (int): The input file format. Use FileType class.
        output_type (int): The output data type. Use PythonType class.
        file_path (str): Target input file path.
    
    Returns: Specified output_type from parameters.
    """

    r = None
    if output_type == 1 and input_type == 1:
        try:
            df = pd.read_csv(file_path)
            r = df
            return r
        except OSError as err:
            print("OS error: {0}".format(err))
        except ValueError:
            print("Could not convert data to an integer.")
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
        raise