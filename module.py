"""
This is a module level docstring. It documents the module, module.py.
The docstring has to go at the top of the module.

This is also a multiline string. It is NOT a comment. 
Comments aren't parsed. Strings are.

A module is a file that ends in .py, and contains Python code. 

If the module is imported, and help(module) called, 
the docstring will show as the help.

(Where you see `>>>` this is what you would see in an interactive Python shell.)

>>> import module
>>> help(module)
This is a module level docstring...
"""

# This is a comment. It isn't parsed by the Python interpreter.

def a_function():
    """
    This is a function level docstring.
    This function takes no arguments, and returns None
    All functions return None unless they explicitly return something else.
    
    You can see the help on this function just like you can a module-level docstring:
    
    >>> help(a_function):
    This is a function level ...
    """

def another_function(arg_1, arg2=None):
    """
    This function takes a required argument, arg_1, 
    and an optional argument, arg_2, which defaults to None.
    """
