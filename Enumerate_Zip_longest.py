# print(dir(str))-----------to get string methods
# print(dir(list))----------to get list methods
# print(dir(set))-----------to get set methods
# print(dir(dict))----------to get dict methods
# print(dir(tuple))---------to get tuple methods


'''enumerate : It will return the enumerate object,Upon traversing or typecasting,
we will get the tuple consisting of two elements where the first ele is index and second element is item..
enumerate return tuple
'''
#
# a = 'hello world'
# print(enumerate(a))     #object
# print(list(enumerate(a)))
# #
# for ele in enumerate(a):
#     print(ele,end="      ")

# ---------------------------

# a = 'hello world'
# for index, item in enumerate(a):
#     print(index, item)

# a ='hello world'
# for ele in enumerate(a):
#     print(ele[1])

# ----------------------------

# num_list = [5, 3, 9, 7, 18, 2, 26]
# for index, item in enumerate(num_list):
#     print(index ** item)

# d = {}
# num_list = [5, 3, 9, 7, 18, 2, 26]
# for index, item in enumerate(num_list):
#     d[index] = item**index
# print(d)

#-------------------------------------------------------------

'''wap tp item and its index number from the given collection. start the index number from 1'''

# apps=['fb', 'qtalk', 'ola', 'uber', 'amazon']
# for index,item in enumerate(apps,start=1):
#     print(f'the item {item} is a {index} index')

# ---------------------------------------------------------------
'''wap tp item and its index number. only if the index no is even'''

# s='python1'
# for index, char in enumerate(s):
#     if not index %2==0:
#         print(index,char)
#
# # ------------------
#
# # alternate method
# for index, char in enumerate(s):
#     if index %2!=0:
#         print(index,char)

# --------------------------------------------------------------

'''wap tp index and its item from the collection, only if the item is string'''

# items = [10,10,5,True,'hello','hai']
#
# for index,item in enumerate(items):
#     if type(item)==bool:
#         # print(f'the item {item} is at {index} index')
#         print(f'{item},{index}')

#--------------------------------------------------------------------

'''create a dict where the elements will be the key and its index is the value'''

# names = ['puma', 'nike', 'sketchers', 'levis', 'adidas', 'bata']
# dict_ = {}
# for ele in enumerate(names):
#     dict_[ele[1]] = ele[0]
#
# print(dict_)

#---------------------------------------------------------------------
'''create a dict where the ele is the key and its index will be the value in the form of list'''

# a = 'hello world'
# #
# d = {}
# for ele in enumerate(a):
#     if ele[1] not in d:
#         d[ele[1]] = [ele[0]]
#     else:
#         d[ele[1]] += [ele[0]]
#
# print(d)
#------------------------------------------

'''zip: 
* The zip() function takes iterables, arranges them in a tuple and return it.
SYNTAX : zip(var1, var2,…)
'''
#
# brand = ['oneplus', 'samsung', 'iphone', 'nokia']
# tag_lines = ['never settle', 'together for tomorrow', 'think different', 'connecting people']
# print(zip(brand, tag_lines))    #<zip object at 0x000002128A8F0380>

# for ele in zip(brand, tag_lines):
#     print(ele)

# print(list(zip(brand, tag_lines)))

# for ele in zip(tag_lines, brand):
#     print(ele)

#-----------------

# country = ['india','india','brazil', 'china', 'egypt', 'mexico']
# code = [+91, +55, +86, +20]
# for ele in zip(country, code):
#     print(ele)

#-------------------

# country = ['india', 'brazil', 'china', 'egypt', 'mexico']
# code = [+91, +55, +86, +20]
#
# d = {}
# for i,j in zip(country, code):
#     d[i]=j
# print(d)

# ----------------------------

# a = [1, 2, 3 ,4]
# b = [10, 20, 30]
# c = [100, 200, 300, 400, 500]
# for ele in zip(a, b, c):
#     print(ele)

#-------------

# a = ['hai', 'hello', 'hey']
# b = 'python'
# c = {2, 3, 4, 5}
# for ele in zip(a, b, c):
#     print(ele)

#----------------

# a = 'python'
# b = {'India':'Delhi', 'SouthKorea':'Seoul', 'Srilanka':'Colombo'}
# for ele in zip(a, b.values()):
#     print(ele)

#----------

# a = 'hello'
# b = 'hai'
# for ele in zip(a, b):
#     print(ele)

#--------------------------

# char = 'ABCDE'
# ascii = [65,66,67,68,69]
#
# for i,j in zip(char,ascii):
#     print(f'the letter {i} ascii code is {j}')

# -------------------------------------

'''ZIP-LONGEST
NOTE: To include all the elements of iterables of different length, we can use zip_longest.
It will map to the extra element with None by default.
SYNTAX: zip_longest(var1, var2,……….., fillvalue = None)
'''
from itertools import zip_longest
#
# a = 'hello'
# b = 'hai'
# for ele in zip_longest(a, b):
#     print(ele)

# a = 'hello'
# b = 'hai'
# for ele in zip_longest(a, b, fillvalue=200):
#     print(ele)

#-----------------

'''create a dict of ele and its count pair'''
# a = 'abracadabra'   #{a:5, b:2,...}
# d = {}
# for ele in a:
#     d[ele] = a.count(ele)
# #
# print(d)

## Alternate solution
# a = 'abracadabra'   #{a:5, b:2,...}
# d = {}
# for ele in a:
#     if ele not in d:
#         d[ele] = 1
#     else:
#         d[ele] += 1
# print(d)

#--------------------------------


#--------------------------------------------

'''reversed() : Returns iterator object. Will reverse the given sequence'''

# a = 'hello'     #olleh
# print(reversed(a))      #<reversed object at 0x00000233D71AABC0>

# rev_ = list(reversed(a))        #['o', 'l', 'l', 'e', 'h']
# print(rev_)

# print(''.join(rev_))      #olleh

# --------------------

# a = 'hello'
# for ele in reversed(a):
#     print(ele, end='')

# --------------------------

# names = ['puma', 'nike', 'sketchers', 'levis', 'adidas', 'bata']
# print(list(reversed(names)))


'''
reverse method in the list will modify the original list, whereas reversed
will not modify the original list, it will give a new list

reverse method is a method of a list, whereas reversed is a class and can be applied on
other iterables
'''