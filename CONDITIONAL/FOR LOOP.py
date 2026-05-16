# FOR LOOP

'''FOR is a keyword which is used as loop statement to execute some set of instruction again and again.
The number of iterations/executions of a for loop, it depends on length of collection.'''

'''A for loop is used for iterating over a sequence 
(that is either a list, a tuple, a dictionary, a set, or a string).'''


# str = 'hello'
#
# for ele in str:
#     # print(ele)
#     print(ele)

# import keyword
# print(keyword.kwlist)


'''i---------it is a orbitary variable name which holds individual item in each iteration.
   in--------it seperates the each item from the collection
   'hello'---it is a string collection, we can pass any collective data type'''


# l = {1,2,3,4}
#
# for i in l:
#     print(i)

# --------------

# a= {'a':1, 'b':2, 'c':3, 'd':4}
#
# for k in a:
#     print(k)

# ---------------------------------------------------------------------------------------------------------------

'''Range---
is used to generate sequence of numbers based on the special arguments. Range is considered as collection
but it doesn't have proper data structure to display the output, to over come this problem we can use typecasting'''

'''The range() function returns a sequence of numbers, 
starting from 0 by default, and increments by 1 (by default), and ends at a specified number.'''
# _____________________________________
'''Note that range(6) is not the values of 0 to 6, but the values 0 to 5.'''

'''The range() function defaults to 0 as a starting value, 
however it is possible to specify the starting value by adding a parameter: 
range(2, 6), which means values from 2 to 6 (but not including 6):'''


# __________________________________

# Using the range() function:

# for x in range(6):
#   print(x)

# _____________________________________
# print(list(range(0,5)))

# print(set(range(0,5)))

# print(tuple(range(0,5)))

# ---------------------

# print(str(range(0,5)))

# print(dict(range(0,5)))

# -------------------------

# print(list(range(0,5,2)))

# print(list(range(0,15,3)))

# print(tuple(range(0,10,2)))

# print(list(range(10,0,-1)))

# --------------------------------------------------------------------------------------------------------

'''1. wap to find the sum of n natural numbers'''

# number = int(input('Enter the num: '))
# total = 0
# for num in range(2, number+1):
#     total += num        #total = total + num
# print(total)

'''  0 = 0 + 2
     2 = 2 + 3
     5 = 5 + 4
     9 = 9 + 5
     14'''

'''total = total + num    
     0   =   0   +  0 
     0   =   0   +  1
     1   =   1   +  2
     3   =   3   +  3
     6   =   6   +  4
     10  =   10  +  5
     15  =   15  +  6
     21  =   21  +  7
     28  =   28  +  8
     36  =   36  +  9
     45  =   45  +  10
     55'''

#------------------------------------------------------------
'''2. Sum of all digits'''

# number = input('Enter the num: ')     #534
# # str_num = str(num)      #'534'
# digit_sum = 0
# for digit in number:
#     if digit.isdigit():
#         digit_sum += int(digit)
# print("Sum of digits:",digit_sum)

'''sum = sum + int(ele)
    0  =  0  +  5
    5  =  5  +  3
    8  =  8  +  4
    12'''

#------------------------------------------------------------
'''3. Wap to fetch the numbers which has 6 in them in the range(1, 100)'''
#
# list_ = []
# for ele in range(1, 100):
#     if '6' in str(ele):
#         list_.append(ele)
#
# print(list_)


# list=[]
# for digit in range(1,100):
#     if "6" in str(digit):
#         list.append(digit)
# print(list)

#-------------------------------------------------------------
'''4. create a list where even len elements should be as it is, odd
len elements should be reversed'''

# names = ['samsung', 'oneplus', 'apple', 'vivo', 'oppo', 'nokia', 'googlepixel']
# res_list = []
# for ele in names:
#     if len(ele) % 2 == 0:
#         res_list.append(ele)
#     else:
#         res_list.append(ele[::-1])
# print(res_list)


#--------------------------------------------------------------------
'''5. wap to reverse a string'''

# str = 'king'
# rev = ''
# for ele in str:
#     rev = ele + rev
# print(rev)

'''rev = ele + rev
    '' =  k  +  ''
     k =  i  +  k
    ik =  n  +  ik
   nik =  g  +  nik
  gnik'''

# -----------------------------------------------------------------

'''6. write a programm to build dictionary of each word and length pair from the given string only if the 
word ends with vowels'''

# sen="hello welcome to python"
# dict={}
# word = sen.split()
#
# for ele in word:
#     if ele[-1] in 'aeiouAEIOU':
#         dict[ele]=len(ele)
# print(dict)

# -------------------------------------------------------------
'''7. wap tp last character of each items in the given collections'''

# names = ['steve','smith','david','miller']
# for i in names:
#     # print(i[-1])
#     print(i[-1], end="")

# ------------------------------------------------------

'''8. create a dict of ele and its len pair'''

# names = ['samsung', 'oneplus', 'apple', 'vivo', 'oppo', 'nokia', 'googlepixel']
# dict_ = {}
# for ele in names:
#     dict_[ele] = len(names)
# print(dict_)

#---------------------------------------------------------
'''9. create a dict, if len of ele is even, retain the same. for value, else reverse for value'''

# names = ['samsung', 'oneplus', 'apple', 'vivo', 'oppo', 'nokia', 'googlepixel']
# dict_ = {}
# for ele in names:
#     if len(ele)%2 == 0:
#         dict_[ele] = ele
#     else:
#         dict_[ele] = ele[::-1]
# print(dict_)

# d={i:i if len(i)%2==0 else i[::-1] for i in names}
# print(d)

#------------------------------------------------------------
'''10. find the factorial of a number'''

# num = int(input('Enter the num: '))     #5
# fact = 1
# for ele in range(1, num+1):
#     fact *= ele     #fact = fact * ele

# print(fact)

''' fact = fact * ele
      1  =   1  *  1
      1  =   1  *  2
      2  =   2  *  3
      6  =   6  *  4
      24 =  24  *  5
      120 '''

#----------------------------------------------------------------------------------------------
'''11. wap to count the total number of alphabets, numericals and special characters
in the given string'''

# str = '123h#LL0 @ w0rLd pyT#0n'
# count_alpha = 0
# count_digit = 0
# spec_chr=0
#
# for i in str:
#     if i.isalpha():
#         count_alpha+=1
#     elif i.isdigit():
#         count_digit+=1
#     else:
#         spec_chr+=1
# print(f"Total number of Alphabets are {count_alpha},\nTotal numericals are {count_digit}\nTotal special characters are {spec_chr} ")
#
#---------------------------------------------------------------------------------------------
'''12. Calculate the sum of all the numbers present in the string'''

# str_ = 'h3ll0 123'
# sum_ = 0
# for ele in str_:
#     if ele.isdigit():
#         sum_ += int(ele)
#
# print(sum_)

''' sum = sum + ele
     0  =  0   + 3
     3  =  3   + 1
     4  =  4   + 2
     6  =  6   + 3
    9'''

#--------------------------------------------------------------------------------------------
'''13. wap to get the maximum number'''

# # Method 1
# num_list = [10, 2, 11, 4, 9.8, 56, 55, 43.9, 28, 99, 87, 11.8]
# max_num = 0
# for num in num_list:
#     if num > max_num:
#         max_num = num

# Method 2
# num_list = [10, 2, 11, 4, 9.8, 56, 55, 43.9, 28, 99, 87, 11.8]
# num_list.sort()
# print(num_list)     #[2, 4, 9.8, 10, 11, 11.8, 28, 43.9, 55, 56, 87, 99]
# print(num_list[-1])     #99

# Method 3 using max func
# num_list = [10, 2, 11, 4, 9.8, 56, 55, 43.9, 28, 99, 87, 11.8]
# print(max(num_list))

#----------------------------------------------------------------------------------------------
'''14. wap to get the minimum number'''

# Method 1
# num_list = [10, 2, 11, 4, 9.8, 56, 55, 43.9, 1, 99, 87, 11.8]
# min = num_list[0]
# for num in num_list:
#     if num < min:
#         min = num
# print(min_)

# ## Method 2
# num_list = [10, 2, 11, 4, 9.8, 56, 55, 43.9, 1, 99, 87, 11.8]
# num_list.sort()
# print(num_list)
# print(num_list[0])

# ## MethodZ 3 using min func
# num_list = [10, 2, 11, 4, 9.8, 56, 55, 43.9, 1, 99, 87, 11.8]
# print(min(num_list))

#--------------------------------------------------------------------------------------------
'''15. Create a dict with ele of a string as a key and its ASCII value as value '''

# str_ = 'hello world'
# dict_ = {}
# for ele in str_:
#     dict_[ele] = ord(ele)
# print(dict_)

# s=")&^#@#%$ %^&8&*(&$"
# d={i:ord(i) for i in s}
# print(d)

#-------------------------------------------------------------------
'''16. wap to get the below output'''

# s = 'python is a programming language and programs are fun'
# # {p:[python, programming, programs], i:[is], a:[a, and, are], l:[language], f:[fun]}
#
# s_ = s.split()
# # print(s_)   #['python', 'is', 'a', 'programming', 'language', 'and', 'programs', 'are', 'fun']
# d = {}
# for ele in s_:
#     if ele[0] not in d:
#         d[ele[0]] = [ele]
#     else:
#         d[ele[0]] += [ele]      #d[ele[0]] = d[ele[0]] + [ele]
#
# print(d)

s = 'python is a programming language and programs are fun'


#--------------------------------------------------------------

'''Nested Loops
A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":'''
# __________________________
# Example
# Print each adjective for every fruit:

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
#
# for x in adj:
#   for y in fruits:
#     print(x, y)