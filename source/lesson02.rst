.. include:: nav.rst

Lesson 02 - Modules and Functions
================================================
A Python module is a file(s) containing Python statments suffixed with the .py extension. A modules define variables, functions, and classes. Each module Has 
a private symbol table to manage the scope of objects (avoid collions with other modules). Optionally a module can have executable code as well. Python modules are often organized in 
Python packages, which for now we will consider as collections of one or more modules. Millions of Python packages are available at the Python Package Index **PyPI**, easily installable with 
using **PIP** or through the package interface in the PyCharm editor. 

.. warning::

    Python packages are 3rd party software that typically have a permissive software license (e.g. MIT) that frees developers from any liability from issues arising from use 
    of the software. It's the developer's responsibility to verify the accuracy of software, typically through the inclusion of a unit testing framework (future class). 


Modules are imported into the current program using a the **import** statement. The interpreter will search for the module in the directories defined in the OS variable **PYTHONPATH**. Typically *import* statements 
are defined at the top of the module.

Importing a module
----------------------------
There are several way to import a module into the programming environment. 

Import the entire module
+++++++++++++++++++++++++++
Importing the entire module provides a collision-proof way to bring the entire module in the environment. Reference the contents of the module using dot notation.


.. code-block:: Python

    import statistics , pandas as pd

    numbers = [5,12,3.5,9,22]
    mean = statistics.mean(numbers)
    print(mean)

Import specific objects of the module
++++++++++++++++++++++++++++++++++++++++
Selectively import element of the module into the programming environment. The granular approach give the developer control of the environment and simplifies referencing the 
modules objects.

.. code-block:: Python

    from statistics import mean,median

    numbers = [5,12,3.5,9,22]
    mean_val = mean(numbers)
    print(mean_val)

Import the entire module into the programming environment
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Import the entire contents of a module into the programming environment. This shorthand approach is succint way to expose all the objects within the module to the programming environment, 
but the risk of collisions is high, especially for 3rd party modules.     

.. code-block:: Python

    from statistics import *

    numbers = [5,12,3.5,9,22]
    mean_val = mean(numbers)
    print(mean_val)


    .. note:: 

        In Python, there is no Main() function to define the entry point to an application. When a .py file is run, the built-in variable **__name__** evaluates to "__main__", 
        and can be used to drive execution..

        .. code-block:: 

            #my .py file

            # includes fuction definitions....


            # bottom of program, no indent
            if __name__ == '__main__':
                # do my code        

Creating functions
============================
A Python function is a block of code that only executes when called. It accepts parameters, which are dynamically typed depending on the value passed.  The **def** keyword 
begins the function defintion. The return value can be pretty much anything, a string, two strings, a collection, but there will always be a return value, even if it's *None*.

Functions are first-class objects, which will make more sense later, but for now, know that when the are invoked, they must end in **()**, even if there are no arguments, but they can be 
passed as arguments without the *()*

Hello world
------------------
Our first function return a string, which we can print to the console.

.. code-block:: Python

    def hello_world:
        return "Hello world"

Nothing happens until you call the function, very similar to a SAS macro

.. code-block:: Python

    print(hello_world())

Function parameters
-----------------------------
Functions accepts parameters much the same way as a SAS macro, positional or named (e.g. keyword). Named parameters can have default values. Parameters can also be collections of 
an unknown type or number of arguments e.g.  the *args and **kwargs convention.

    .. code-block:: Python

        # a single string
        def my_func(arg1):
            return f"hello {arg1}"

        print(my_func('cruel world'))

        # dynamic types
        def my_func(arg1, arg2):

            arg_list = [arg1,arg2]

            for arg in arg_list:
                if isinstance(arg,list):
                    print(f"{arg} is a list")
                    for i in arg:
                        print(i)
                elif isinstance(arg,str):
                    print(f"{arg} is a string")

        my_func([1,2,3,],"Hi")

        # accept *n* positional arguments
        def my_func(*args):

            counter = 0
            for i in args:
                counter += 1
                print(f"{counter}) {i} is the number {counter} argument of type {type(i)}")

        my_func('junk', 1, [1,2,3],('a','b','c') )

        











