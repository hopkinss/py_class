.. include:: nav.rst

Lesson 01 - Basic Syntax
==================================

Variables
--------------------
An identifier starts with a letter A to Z or a to z or an underscore (_) followed by zero or more letters, underscores and digits (0 to 9). Convention is to use lower case and demlimit words
with **_**.

    .. code-block:: Python

        # Variable assignment
        my_var = "Test"

        # Assign more than one variable
        a,b,c = 1,2,3

.. csv-table:: Reserved Words
   :widths: 20,20,20

    "and","False","nonlocal"
    "as","finally","not"
    "assert","for","or"
    "break","from","pass"
    "class","global","raise"
    "continue","if","return"
    "def","import","True"
    "del","in","try"
    "elif","is","while"
    "else","lambda","with"
    "except","None","yield"

Code blocks
---------------------
Python provides no braces to indicate blocks of code for class and function definitions or flow control. Blocks of code are denoted by line **indentation**, which is rigidly enforced.
The number of spaces in the indentation is variable (to not use 4 is barbaric), but all statements within the block must be indented the same amount .

A block code is indicated by using **:** and indenting the associated lines accordingly

    .. code-block:: Python

        if var==1:
            print("Hi")
            return true
        else:
            print("Bye")
            return false

Operators
-------------------------

.. csv-table:: Arithmatic Operators
   :widths: 20,80

    "\+","Adds values on either side of the operator."
    "\-","Subtracts right hand operand from left hand operand."
    "\*","Multiplies values on either side of the operator"
    "/","Divides left hand operand by right hand operand"
    "%","Divides left hand operand by right hand operand and returns remainder"
    "**","Performs exponential (power) calculation on operators"
    "//","Floor Division - The division of operands where the result is the quotient in which the digits after the decimal point are removed."
    "+=,-=,/=,*=","[Expression on left] = [self] [operator][expresison on left]  (e.g. increment, decrement)"


.. csv-table:: Logical Operators
   :widths: 20,80

    "==","If the values of two operands are equal, then the condition becomes true."
    "!=","If values of two operands are not equal, then condition becomes true."
    "<>","If values of two operands are not equal, then condition becomes true."
    ">","If the value of left operand is greater than the value of right operand, then condition becomes true."
    "<","If the value of left operand is less than the value of right operand, then condition becomes true."
    ">=","If the value of left operand is greater than or equal to the value of right operand, then condition becomes true."
    "<=","If the value of left operand is less than or equal to the value of right operand, then condition becomes true."
    "in, not in","Membership"
    "or, and, not","Boolean"
    "is, is not","Identity"

Python Functions and Methods vs. SAS Functions
--------------------------------------------------
Python, unlike the typical implementation of SAS/Base, is an object-oriented language. This implies that everything is an
object, and as such, has properties and associated functions, known as *Methods*. In Python, a string is an object (a
collection of characters), and has methods that correspond to the string functions is SAS with which you are very
familiar. The big difference here is the concept that when you call a string method, you are implicitly passing the
string object on which the method is invoked.

`List of string methods <https://www.programiz.com/python-programming/methods/string/>`_

.. note::

    A big benefit of OOP using an IDE is intellisense. Using the 'dot' notation, the IDE display all the
    available properties and methods for the object...(more on this in OOP)

    |intel|


String Methods
++++++++++++++++++
.. code-block:: Python

    # What's the value of pos?
    my_string="this is only a test"
    pos=my_string.find('is')

    # The equivalent of var=upcase(my_string) in SAS
    new_string=my_string.upper()

    # Will this change the value of my_string to upcase?
    my_string.upper()

Collections
---------------------------
todo













Additionally,  Python is infinitely extensible with an endless assortment of modules that can provide an analog of
any element of SAS functionality you can imagine (more on this later).







