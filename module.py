"""This is a module level docstring. It documents the module, module.py.
The docstring has to go at the top of the module.

This is also a multiline string. It is NOT a comment. 
Comments aren't parsed. Strings are.

A module is typically a file that ends in .py, and contains Python code. 

If the module is imported, and help(module) called, 
the docstring will show as the help.

(Where you see `>>>` this is what you would see in an interactive Python shell.)

>>> import module
>>> help(module)
This is a module level docstring...
"""

# This is a comment. It isn't parsed by the Python interpreter.

# Keywords are words you can't use as variable names. 
# (You can assign variable names to point to values.)
# "import" is a keyword. 

# For example, let's import the module called keyword:

import keyword
# after you import a module, you can use things in that module.
# for example, kwlist is a list of all the keywords in Python:
# >>> keyword.kwlist
# ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 
#  'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 
#  'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 
#  'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 
#  'while', 'with', 'yield']

# we've now used the keyword, `import`

# the keyword module is now a global name in this module.
# any piece of code in this module can access it by name now.

# def starts a function statement
def a_function():
    """This is a function level docstring.
    This function takes no arguments, and returns None
    
    None is a single object that basically means no-value in Python.
    It represents the null value for Python.
    
    All functions return None unless they explicitly return something else.
    
    You can see the help on this function just like you can a module-level docstring:
    
    >>> help(a_function):
    This is a function level ...
    """
    
# we've now used the keyword def! 
# the function it defined is now a global name that can be accessed from any
# piece of code in the module.

def print_all_the_keywords():
    """This function iterates over the keywords and prints them out.
    again, because it doesn't return anything explicitly, it returns None
    """
    for each_keyword in keyword.kwlist:
        print(each_keyword)

def another_function(arg_1, arg2=None):
    """This function takes a required argument, arg_1, 
    and an optional argument, arg_2, which defaults to None.
    """
    if arg_2 is None:
        return arg_1
    return arg_1 + arg_2

def main():
    """
    This is the main process of this module when the module is 
    the entry point for the program.
    
    This will attempt to illustrate the value of 
    giving your functions descriptive names:
    """
    a_function()
    print_all_the_keywords()
    another_function(1, 2)


# This is at the end of most Python modules. 
# __name__ is a name in all Python modules
# it is usually the name of the module 
# (in this case, `module`, since the file is module.py)
# however, if you run your program with a module, it's __name__ is "__main__".
if __name__ == '__main__':
    main() # So this will run the main function when it's the main module.
