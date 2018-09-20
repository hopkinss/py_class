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
import io

try:
    f = open("test.txt")
    f.write("Lorum Ipsum")
except io.UnsupportedOperation:
    print("Something went wrong when writing to the file")
finally:
    f.close()