.. include:: nav.rst

Lesson 03 - Reading an external file
================================================
Python provide built in functions to work with external files. The **open** function accepts a file and returns a file object. The file object is an *iterable*, which 
supports sequential access to each line of the file. The open function also optionally accepts the permission for the operation to perform on the file. 

    * **w** - write  (use **+** modifier to create the file if it does not already exist)
    * **r** - read
    * **a** - append

    .. note:: 

        Remember to call the close() function on the file object 


.. code:: Python

    fn = r"C:\Users\shopkins\mu_code\class.csv"
    file_obj = open(fn,'r')

Built-in functions to read an external file
-------------------------------------------------
Python provides built in methods to read all or parts of a file from the file object. 

    * read() - returns the entire text file. It optionally accepts and integer argument to indicate the number of characters to read.
    * readline() - returns a single line of the file. Together with the file objects support for interation can be used to read a file line by line.

    .. note:: 

        Reading the file line by line can be acomplished by iterating over the file object

    
    .. code:: Python

        # read the entire contents into a string
        f = open(r"class.csv")
        data = f.read()
        f.close()

        # read a csv file line by line
        f = open(r"class.csv")
        for line in f:
            print(line)
        f.close()


        # read a csv file into list of lists 
        data =[]
        f = open(r"class.csv")
        for line in f:
            data_line=line.strip().split(',')
            data.append(data_line)
        f.close()

Use **csv** module to read a file
-----------------------------------------------
Python **csv** module provides classes work with tabular data. The classes have methods to read and write data in CSV format. 

csv Read methods
++++++++++++++++++++++++
* reader() - returns an interable reader object the captures each row as list object. Default delimiter is ',' but can be specified using **delimiter=** parameter
* DictReader() - return a interable reader object that captures data as dictionary key-value pairs

.. code-block:: Python

    import csv

    f=open(r"class.csv")
    reader = csv.reader(f)
    for row in reader:
        print(row)
    f.close()        

    data = {}
    f=open(r"class.csv")
    reader = csv.DictReader(f)
    for row in reader:
        key  = row.pop('NAME').upper()
        data[key]=row
    f.close()    

    print(data['ALICE']['HEIGHT'])
            

Context manager
-------------------------
A context manager is just a contstruct that allows you to allocate and release resouces and define scope explicitly. Rather than using 
open and close statements to assign and release a file handler, with the **with** statement to define the context. There is also implicit 
exception handling in the if the file is unable to be opened, the manager will always close the file hander.

.. code-block:: Python

    # context manager
    data =[]
    with open(r"class.csv") as fn:
        for line in fn:
            data_line=line.strip().split(',')
            data.append(data_line)

    [print(i) for i in data] 






