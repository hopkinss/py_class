.. include:: nav.rst

Lesson 01 - Basic Syntax
==================================


Variables
--------------------
*  Not declared and dynamically typed based on the value - type is mutable 
*  A variable name must start with a letter or the underscore character
*  Variable names are case-sensitive (age, Age and AGE are three different variables)
*  Convention is to use lower case and delimit words in a variable with **_** (e.g. subject_age)

    .. code-block:: Python

        # Variable assignment
        my_var = "Test"

        # Assign more than one variable
        a,b,c = 1,2,3

        # Change the type of a variable
        x='10' # is a string 
        x=1    # now it's an int

        # You can display the variables with print function or just typing the variable name in ipython
        print(my_var)

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


Python built-in data types
+++++++++++++++++++++++++++++
Python's built-in data types can be grouped into several classes. These are numeric types, sequences, sets and mappings.
Python stores the type of an object with the object, and checks when the operation is performed whether that operation
makes sense for that object (e.g. dynamic typing). Think of the variable as a drawer and the type is defined by the value contained in the drawer, which can change at any time.

.. csv-table:: Common built-in data types
   :header: "Type ","Description"
   :widths: 20,80

    "int"," Integers"
    "float"," Floating-Point numbers"
    "str"," String"
    "list","A mutable ordered sequences of objects"
    "tuple","An imutable ordered sequences of objects"
    "set","An unordered collection of unique objects"
    "dict","A collection of paired items made of a key and a value."

.. code-block:: Python

   # Display and evaluate the type of a variable
   my_float = 1.1
   print(type(my_float))

   # Evaluate the type
   if type(my_float) == float:
       print("it's a float")

   if isinstance(my_float,float):
       print("it certainly is a float")

Type conversions
+++++++++++++++++++++
The table lists functions available to cast variables into different data types

.. csv-table:: Type conversion functions
   :header: "Function","Description"
   :widths: 20,80

    "ascii()","Returns a string containing a printable representation of an object"
    "bin()","Converts an integer to a binary string"
    "bool()","Converts an argument to a Boolean value"
    "chr()","Returns string representation of character given by integer argument"
    "complex()","Returns a complex number constructed from arguments"
    "float()","Returns a floating-point object constructed from a number or string"
    "hex()","Converts an integer to a hexadecimal string"
    "int()","Returns an integer object constructed from a number or string"
    "oct()","Converts an integer to an octal string"
    "ord()","Returns integer representation of a character"
    "repr()","Returns a string containing a printable representation of an object"
    "str()","Returns a string version of an object"
    "type()","Returns the type of an object or creates a new type object"

.. code-block:: Python

      # Cast into another type
      my_str='33.9'
      my_float=float(my_str)

      # Be aware of types when performing manipulations
      try:
          my_val = my_str + 44
          print(my_val)
      except TypeError:
          print("You must cast string to number to do math")
          my_val = float(my_str) + 44;
          print(my_val)


Code blocks
---------------------
Python provides no braces to indicate blocks of code for class and function definitions or flow control. Blocks of code are denoted by line **indentation**, which is rigidly enforced.
The number of spaces in the indentation is variable (to not use 4 is barbaric), but all statements within the block must be indented the same (or more for nested blocks).

A block code is indicated by using **:** and indenting the associated lines accordingly

    .. code-block:: Python

        if var>1:
            print("Hi")

            if var >100:
               print("Very hi")
        else:
            print("Bye")


Operators
-------------------------

.. csv-table:: Arithmetic Operators
   :widths: 20,80

    "\+","Adds values on either side of the operator."
    "\-","Subtracts right hand operand from left hand operand."
    "\*","Multiplies values on either side of the operator"
    "/","Divides left hand operand by right hand operand"
    "%","Divides left hand operand by right hand operand and returns remainder"
    "**","Performs exponential (power) calculation on operators"
    "//","Floor Division - The division of operands where the result is the quotient in which the digits after the decimal point are removed."
    "+=,-=,/=,*=","[Expression on left] = [self] [operator][expression on left]  (e.g. increment, decrement)"


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

.. code-block:: Python

   # Evaluate equality
   a,b=1,1
   print( a == b)

   # Membership
   my_list=[1,2,3,4]
   print(1 in my_list)

   # Identity - does the symbol point to the same object
   a=None
   print (a is None)


Strings
------------------
In Python a string is a collection, a sequence of chars. Unlike the implementation of string in SAS/Base, Python string
is an object. This means it can have properties and functions, known as *Methods*. You will find Python provides
every string function provided in SAS, and them some. The big difference here is the concept that when you call a
string method, you are implicitly passing the string object on which the method is invoked.

.. note::

    * Strings are immutable, you cannot update an existing string.

    * (A big benefit of OOP using an IDE is intellisense. Using the 'dot' notation, the IDE display all the
      available properties and methods for the object...(more on this in OOP)

      |intel|


Python String Methods
+++++++++++++++++++++++++++++++++++++++
.. csv-table:: String Methods
   :header: "Methods", "Description","Method", "Description"
   :widths: 20,80,20,80

    "capitalize()","Converts first character to Capital Letter","ljust()","returns left-justified string of given width"
    "center()","Pads string with specified character","rjust()","returns right-justified string of given width"
    "casefold()","converts to casefolded strings","lower()","returns lowercased string"
    "count()","returns occurrences of substring in string","upper()","returns uppercased string"
    "endswith()","Checks if String Ends with the Specified Suffix","swapcase()","swap uppercase characters to lowercase; vice versa"
    "expandtabs()","Replaces Tab character With Spaces","lstrip()","Removes Leading Characters"
    "encode()","returns encoded string of given string","rstrip()","Removes Trailing Characters"
    "find()","Returns the index of first occurrence of substring","strip()","Removes Both Leading and Trailing Characters"
    "format()","formats string into nicer output","partition()","Returns a Tuple"
    "index()","Returns Index of Substring","maketrans()","returns a translation table"
    "isalnum()","Checks Alphanumeric Character","rpartition()","Returns a Tuple"
    "isalpha()","Checks if All Characters are Alphabets","translate()","returns mapped charactered string"
    "isdecimal()","Checks Decimal Characters","replace()","Replaces Substring Inside"
    "isdigit()","Checks Digit Characters","rfind()","Returns the Highest Index of Substring"
    "isidentifier()","Checks for Valid Identifier","rindex()","Returns Highest Index of Substring"
    "islower()","Checks if all Alphabets in a String are Lowercase","split()","Splits String from Left"
    "isnumeric()","Checks Numeric Characters","rsplit()","Splits String From Right"
    "isprintable()","Checks Printable Character","splitlines()","Splits String at Line Boundaries"
    "isspace()","Checks Whitespace Characters","startswith()","Checks if String Starts with the Specified String"
    "istitle()","Checks for Titlecased String","title()","Returns a Title Cased String"
    "isupper()","returns if all characters are uppercase characters","zfill()","Returns a Copy of The String Padded With Zeros"
    "join()","Returns a Concatenated String","format_map()","Formats the String Using Dictionary"

`List of string methods <https://www.programiz.com/python-programming/methods/string/>`_


Examples of calling string functions in Python
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Python

    # Find the position of substring withing a string
    my_string="this is only a test"
    pos=my_string.find('is')
    print(pos)

    # Capitaliztaion
    new_string=my_string.upper()

    # Concatenate strings
    my_string += " of strings"

    # Format strings
    item_name='bicycle'
    item_cost=100.4552423
    y="The price of a {} is {:0.2f}".format(item_name,item_co

    # Split a string and take a specific element (e.g. SAS SCAN function)
    path_var = r'O:\projects\sgn-35\sg035-014\csr\test.sas';
    print(path_var.split('\\')[-1])

    # Chain functions
    my_string = "Brentuximab Vedotin"
    if my_string.lower().startswith("bren"):
        print('do some things')


    #Substring using slice (remember a string is an immutable collection of characters)
    #Slice  [start:end (not inclusive):stride]
    y=my_string[:4]  #  -> this
    y=my_string[5:7] # -> is
    y=my_string[::-1] # -> tset a ylno si siht
    y=my_string[:-1] # ->this is only a tes
    y=my_string[-4:] # ->test
    y=my_string[::2] # -> ti sol  et

String formatting 
------------------------------
#. Format() method - allows replacement by index in the string expression. (`Number format examples <https://mkaz.blog/code/python-string-format-cookbook/>`__)

    .. code-block:: Python

        fruit1 = "orange"
        fruit2= "apple"

        var1="My favorite fruit is an {}, but {} is good too".format(fruit1,fruit2)

        # Python number formatting 
        i=99




#. String interpolation **f-string** - embed Python expressions inside of string contstants.  

    .. code-block:: Python

        var1 = f"you can't compare an \"{fruit1}\" to an \"{fruit2}\""

        var2 = (f"{','.join(map(str.upper,['bill','joe','steve']))}")

#. Python number formatting 

    i=99
    print("{:0>6d}".format(i))


       

Introduction to collections
--------------------------------------------
In order to make program flow more meaningful, we will introduce collections in Python. There are others, but
these three sequence data structures provide enough functionality for the foundation. These objects have properties
and methods for working with themselves.

Lists
+++++++++++++
A list is a mutable zero-origin sequence of values of any type, enclosed by [] and delimited by commas. Unlike SAS, each
element can be of a different type, it can even contain other lists. Python provides a comprehensive array of functionality
to work with lists.

.. csv-table:: List Methods and Built-in Functions
   :widths: 20,80,20,80

   "Method:  append()","Add Single Element to The List","Function: bool()","Converts a Value to Boolean"
   "Method:  extend()","Add Elements of a List to Another List","Function: enumerate()","Returns an Enumerate Object"
   "Method:  insert()","Inserts Element to The List","Function: filter()","constructs iterator from elements which are true"
   "Method:  remove()","Removes Element from the List","Function: iter()","returns iterator for an object"
   "Method:  index()","returns smallest index of element in list","Method: () Function","creates list in Function:"
   "Method:  count()","returns occurrences of element in a list","Function: len()","Returns Length of an Object"
   "Method:  pop()","Removes Element at Given Index","Function: max()","returns largest element"
   "Method:  reverse()","Reverses a List","Function: min()","returns smallest element"
   "Method:  sort()","sorts elements of a list","Function: map()","Applies Function and Returns a List"
   "Method:  copy()","Returns Shallow Copy of a List","Function: reversed()","returns reversed iterator of a sequence"
   "Method:  clear()","Removes all Items from the List","Function: slice()","creates a slice object specified by range()"
   "Function: any()","Checks if any Element of an Iterable is True","Function: sorted()","returns sorted list from a given iterable"
   "Function: all()","returns true when all elements in iterable is true","Function: sum()","Add items of an Iterable"
   "Function: ascii()","Returns String Containing Printable Representation","Function: zip()","Returns an Iterator of Tuples"
   "Function: map","Returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)"


`List of List methods <https://www.programiz.com/python-programming/methods/list/>`_

.. code-block:: Python

   # list methods
   my_list=[1,2,3,4]

   my_list.append(5)
   my_list.pop()
   my_list.count(2)
   my_list.sort() # May require *key* argument or override __lt__ dunder - more on that later

   # built in functions
   len(my_list)
   max(my_list)

   # useful list functions
    my_list = ['a','b','c']
    my_var = ','.join(my_list);
    print(my_var)

    my_var = ','.join(map(str.upper,my_list));
    print(my_var)


Tuple
++++++++++++
A tuple is an imutable zero-origin sequence of values of any type, enclosed by () and delimited by commas. Tuples are
very simlar to lists, except they cannot be modified, and

.. code-block:: Python

    my_tuple=(33,22,99)

Dictionary
+++++++++++++++
A dictionary is collection of key:value pairs, not necessarily in order, and not assesible by a numeric index. The dictionary is enclosed by {},
key and value elements are delimited by colors, and pairs are delimited by commas. Keys must be immutable data types (int, strings, tuples) 

Dictionaries and lists share the following characteristics:

    * Both are mutable.
    * Both are dynamic. They can grow and shrink as needed.
    * Both can be nested. A list can contain another list. A dictionary can contain another dictionary. A dictionary can also contain a list, and vice versa.

Dictionaries differ from lists primarily in how elements are accessed:

    * List elements are accessed by their position in the list, via indexing.
    * Dictionary elements are accessed via keys.

.. csv-table:: Dictionary  Methods and Built-in Functions
   :widths: 20,80,20,80

   "Method: clear()","Removes all Items","Function: ascii()","Returns String Containing Printable Representation"
   "Method: copy()","Returns Shallow Copy of a Dictionary","Function: bool()","Converts a Value to Boolean"
   "Method: fromkeys()","creates dictionary from given sequence","Function: dict()","Creates a Dictionary"
   "Method: get()","Returns Value of The Key","Function: enumerate()","Returns an Enumerate Object"
   "Method: items()","returns view of dictionary's (key, value) pair","Function: filter()","constructs iterator from elements which are true"
   "Method: keys()","Returns View Object of All Keys","Function: iter()","returns iterator for an object"
   "Method: popitem()","Returns & Removes Element From Dictionary","Function: len()","Returns Length of an Object"
   "Method: setdefault()","Inserts Key With a Value if Key is not Present","Function: max()","returns largest element"
   "Method: pop()","removes and returns element having given key","Function: min()","returns smallest element"
   "Method: values()","returns view of all values in dictionary","Function: map()","Applies Function and Returns a List"
   "Method: update()","Updates the Dictionary","Function: sorted()","returns sorted list from a given iterable"
   "Function: any()","Checks if any Element of an Iterable is True","Function: sum()","Add items of an Iterable"
   "Function: all()","returns true when all elements in iterable is true","Function: zip()","Returns an Iterator of Tuples"

`List of Dictionary methods <https://www.programiz.com/python-programming/methods/dictionary/>`_

.. code-block:: Python

   # Declare a dictionary
   my_dict={'bob':1, 'jim':2,'steve':3}

   # Retieve values by key
   steves_number = my_dict['steve']
   steves_number2= my_dict.get('steves','missing') # Get a value with a default if key doesnt exist

   #add/update an item to a dictionary
   my_dict['wayne']=99

   # Add or uppdate using update method
   wayne={"wayne":88}
   bill={'bill':23}
   my_dict.update(wayne)
   my_dict.update(bill)
   print(my_dict)


Program flow control
-----------------------------
Python, like SAS, has a concept of "truthy" in that an expression evaluates to True if not None, False, 0 (int,
float, or complex), or an empty sequence (e.g. my_empty_list=[] is Falsey). 


IF, ELIF, ELSE
++++++++++++++++++
You already know this one, but pay attention to the indentation!


.. code-block:: Python

    if my_int == 1:
        [ statements indented with the IF block]
    elif my_int == 2:
        [statements]
    else:
        [statements]

FOR
++++++++++++++++++++++++++++++++
The for statement in Python supports repeated execution of a statement or block of statements that is controlled by an
iterable expression. The FOR statement will execute over each element in the collection implicitly.

    .. note::

        More on what makes something interable later, for now, think any collection (string, list, tuple, dict) is iterable

.. code-block:: Python

    my_list=["this", "is","really", "only", "a", "test"]

    # for each element in my_list
    for i in my_list:
        print("i={}".format(i))

    # enumerate create an int that captures the iteration, j captures the nth element of my_list.
    # break exits a loop
    for i,j in enumerate(my_list):
        if i != 3:
            print("i={} j={}".format(str(i),j))
        else:
            print("i'm leaving")
            break

    # the range function returns a zero-based integer sequence. It optionally accepts (start,end) but only requires end
    for i in range(10):
        print(i)

     # Continue loop but omit an interation
    for i,j in enumerate(my_list):
        if i != 3:
            print("i={} j={}".format(str(i),j))
        else:
            continue



WHILE
++++++++++++++++++
With the while loop we can execute a set of statements as long as a condition is true.

.. code-block:: Python

    # prompt user for a name until they provide a non-empty string
    greeting= input("Enter your name>")
    while not greeting:
        greeting=input("I said enter your name>")

    # The WHILE loop executes until the exit condition is satistified and the ELSE condition is executed
    counter = 0
    while counter < 10:
        counter +=1
    else:
        print("that worked well")

    # The WHILE loop terminates before the exit condition the the statements in the ELSE are not executed
    counter = 0
    while counter < 10:
        counter +=1
        if counter == 5:
            break
    else:
        print("that worked well")

TRY EXCEPT FINALLY
++++++++++++++++++++++
The try block lets you test a block of code for errors. The except block lets you handle the error. The finally block
lets you execute code, regardless of the result of the try and except blocks.

.. code-block:: Python

    # Trying to print a variable that doesnt exist will cause an error
    try:
        print(no_exist)
    except:
        print("no_exist was not defined")

    # a better approach is to handle the specfic exception
    try:
        print(no_exist)
    except NameError:
        print("no_exist was not defined")
    except:
        print('something else happened')


    # use Finally to execute cleanup code (e.g. close a file or database connection in the case of an error)
    import io

    try:
        f = open("test.txt")
        f.write("Lorum Ipsum")
    except io.UnsupportedOperation:
        print("Something went wrong when writing to the file")
    finally:
        f.close()





