"""
This is a module level docstring. It documents the module, module.py.

If the module is imported, and help(module) called, it will show this as the help. i.e.

>>> import module
>>> help(module)
This is a module level docstring...
"""

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
