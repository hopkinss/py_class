my_string="this is only a test"
my_list=["this","is","only",'a',"test"]


my_dict={'bob':1, 'jim':2, \
         'steve':3}

steves_number=my_dict['steve']

my_list=["this", "is","really", "only", "a", "test"]



# for i,j in enumerate(my_list):
#     if i != 3:
#         print("i={} j={}".format(str(i),j))
#     else:
#         continue
#
# import io
#
# try:
#     f = open("test.txt")
#     f.write("Lorum Ipsum")
# except io.UnsupportedOperation:
#     print("Something went wrong when writing to the file")
# finally:
#     f.close()

# # Show the type
# my_float=1.1
# print(type(my_float))
#
# # Evaluate the type
# if type(my_float) == float:
#     print("it's a float")
#
# if isinstance(my_float,float):
#     print("it certainly is a float")
#
# # Cast into another type'
# my_str='33.9'
#
# # Be aware of types
# try:
#     my_val = my_str + 44
#     print(my_val)
# except TypeError:
#     print("You must cast string to number to do math")
#     my_val = float(my_str) + 44;
#       print(my_val)
#
# # Evaluate equality
# a,b=1,1
# print( a == b)
#
# # Membership
# my_list=[1,2,3,4]
# print(1 in my_list)
#
# # Identity - does the symbol point to the same object
# a=None
# print (a is None)

# path_var = r'O:\projects\sgn-35\sg035-014\csr\test.sas';
# print(path_var.split('\\')[-1])

# my_string = "Brentuximab Vedotin"
# if my_string.lower().startswith("bren"):
#     print('do some things')

# list methods
my_list=[1,2,3,4]
#
# my_list.append(5)
# my_list.pop()
# my_list.count(2)
# my_list.sort() # May require *key* argument or override __lt__ dunder - more on that later
#
# # built in functions
# len(my_list)
# max(my_list)

# Declare a dictionary
my_dict = {'bob': 1, 'jim': 2, 'steve': 3}

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







