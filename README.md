# metapython

This is going to be a repo with legal python that describes python.

I'm writing this under the theory that you learn more when you read code.

## Introduction

Python is an interpreted language. Python code runs in a program called an 
interpreter. 

## Interactive shell

If you have it on your computer, you can probably run it 
like this:

``` shell
$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

The `>>>` is the interactive prompt. The value returned by whatever expression you give
is echoed after the `>>>`

## Running Python programs

Python programs can be modules or packages. A module is a file that
ends with `.py`.
You usually run a python program by typing something like this:

```
$ python module.py
```

This make the module.py code the entry point for the Python program. 
The code inside `module.py` will be immediately compiled and then
run in the Python interpreter.

# Outline

Use this repository as an outline of how Python can and should be
coded. I will attempt to follow best practices and literate
coding principles. Go to these files in order (will be expanded later):

- module.py
