#!/usr/bin/env python3

""" 
-----------------------------------------------------------------------------------------------
Walk in the Park (WitP) v1.02 - Input a keypad press options and nearest neighbors
-----------------------------------------------------------------------------------------------
Walk in the Park (WitP) is provided by Bernard Avenatti under the MIT License agreement.

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
"""

import numpy as np
import pandas as pd
import witp


# =============================
# EXAMPLE 1 - Generate Password 
#             Walks
# =============================

# 1. Read in a qwerty keyboard. 
keys = witp.read_csv_into_dataframe('keyboard_qwerty.csv')
# 2. Password Criteria: between 10-18 characters 
criteria = witp.PasswordCriteriaBuilder().set_min_length(10).set_max_length(18).build()
# 3. Passwords Knowns: Password starts with "1"
hints = witp.PasswordKnownsBuilder().set_pass(np.array(['1'])).build()
# 4. Generate walks for password list
witp.generate_keyboard_walks(keys, criteria, hints)


# =============================
# EXAMPLE 2 - Create Rainbow 
#             Walks
# =============================


# =============================
# EXAMPLE 3 - Shifted Password 
#             Walks
# =============================


# =============================
# EXAMPLE 4 - Generate Pin Walk
# =============================
