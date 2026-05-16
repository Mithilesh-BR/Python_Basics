'''FUNCTION'''

'''Function is a name given to memory location, where the instructions are stored which are 
used to perform specific task

2 types in functions

1. Built-in functions: Pre-defined by Developer. len(), type(),dir(), id(), ord(), chr(),.....

2. User defined functions: Based on user requirement it is created

Components of a function

1. Name of the function
2. Number of arguments
3. Return type'''

# --------------------------------------------

'''Function with arguments 

syntax:

def Fname(arg1, arg2, arg3,....)        # formal parameter
    statement block
    return(val1, val2, val3,....)

To call a function
print(Fname(arg1, arg2, ....)           # actual parameter

# --------------------------------------------------------------------------------------
NOTE:-

# def:- It is a keyword which is used to define the function

# Fname:- Function name is used to identify the particular task

# Arguments: These are requirements to perform specific tasks

# Return:- It is a keyword which is used to return the values and return the control from the
function block

Once after creating a function, it is possible to call it nth number of items.
In user defined functions, passing arguments and return is not mandatory.'''

'''Function with arguments and without return values'''

# ______________________________________________________________________________________


'''1. waf to get the sum of three numbers'''

# def s(a,b,c):
#     print(a+b*c)
#
# s(11,21,3)
# -----------------------------------------------

# fruits = ["apple", "banana", "cherry"]
#
# def my_function(fruits):
#   for x in fruits:
#     print(x)
#
# my_function(fruits)

# -------------------------------------------
'''2. wap to multiply two numbers'''

# def multiply(x,y):
#     print(x*y)
#
# multiply(2,3)

# ----------------------------------------------
'''3. wap to square a num only if the num is integer'''

# def square(a):
#     if type(a) == int:
#         print(a**2)
#
# square(4)

# ----------------------------------------------------
'''4. wap to reverse a string'''

# def rev(str):
#     print(str[::-1])
#
# rev('ghost')

# -----------------------------------------
'''5. wap to check the given string is palindrome or not'''

# def palindrome(str):
#     if str[::-1] == str:
#         print('str is palindrome')
#     else:
#         print('str is not a palindrome')
#
# palindrome('dad')

# ----------------

'''6. wap to count number of upper case characters in a string and create function'''

# def upper_case():
#     str = input('enter the string:')
#     count = 0
#     for ele in str:
#         if ele.isupper():
#             count = count + 1
#     print('the num of upper case ele is', count)
#
# upper_case()

# -----------------------------------------------------

'''7 wap tp a first char of string and define a function'''

# def first_char(str):
#     print(str[0])
#
# first_char('python')

# ------------------------------------------------------

# def non_repeated():
#     word = 'stress'

#     d=[]
#     for element in word:
#         if element!='s':
#             d.append(element)
#     print(d)
#
# non_repeated()

# -----------------------------------------------------

# def divide(a,b):
#     if b == 0:
#         raise ValueError("it can not be divided by zero")
#     return a/b
#
# divide (8, 0)
# -------------------------------------------------------------
# import pytest
#
# def test_add():
#     assert add(2,3) == 5, "2+3 should be 5"
#     assert add(-1,1)== 1, "-1+1 should be 0"
#     assert add(0,0) == 0, "0+0 should be 0"

# ---------------------------------------------------------------

# s= 'my profile: https://auth.geeksforgeeks.org/user/Rayy/articles'
#
# x=s.split()
#
#
# res=[]
# for i in x:
#     if i.startswith("https") or i.startswith("http"):
#         res.append(i)
#
# print("Urls: ", res)

# ---------------------------------------------------------------------

