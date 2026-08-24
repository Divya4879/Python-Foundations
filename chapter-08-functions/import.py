# Problem 8-16: Imports

"""
TASKS:-
1. import module_name
2. from module_name import function_name
3. from module_name import function_name as fn
4. import module_name as mn
5. from module_name import *
"""

# TASK 1

import printing_functions

printing_functions.printing_dict({
    'language':'Python',
    'Specialization':'Backend development',
    'field_of_study':'computer science',
    'book':'python crash course'
    })

# TASK 2

from printing_functions import printing_dict

printing_dict({
    'language':'Python',
    'Specialization':'Backend development',
    'field_of_study':'computer science',
    'book':'python crash course'
    })

# TASK 3

from printing_functions import printing_dict as pd

pd({
    'language':'Python',
    'Specialization':'Backend development',
    'field_of_study':'computer science',
    'book':'python crash course'
    })

# TASK 4

import printing_functions as pf

pf.printing_dict({
    'language':'Python',
    'Specialization':'Backend development',
    'field_of_study':'computer science',
    'book':'python crash course'
    })

# TASK 5

from printing_functions import *

printing_dict({
    'language':'Python',
    'Specialization':'Backend development',
    'field_of_study':'computer science',
    'book':'python crash course'
    })