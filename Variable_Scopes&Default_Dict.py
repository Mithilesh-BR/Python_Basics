'''VARIABLE SCOPES'''

'''Local Variables: Created inside a function. it can't be accessed outside the function'''

# def fun():
#     a=10            #local var
#
# print(a)            #Name error

'''Global Variable: Created outside a function.
 * Can only be accessed inside a func, but can't modify
 * In order to modify var inside a function we have to use global keyword  '''

# a = 10
# def func():
#     a = 15
#     print(a)        #15

# func()
# print(a)             #10

#------------------------------------------


# a = 100
#
# def func():
#     global a
#     a = 150
#     print(a)        #15
#
# func()
# print(a)             #15

# ---------------------------------------

# x = "awesome"
#
# def myfunc():
#   global x
#   x = "fantastic"
#
# myfunc()
#
# print("Python is " + x)

# -----------------------------------

'''Non Local Scope

* these are neither local or global
* if a nested function, has to access and modify the variable of outer function, non local keyword is used'''

# def outer():
#     a=15
#     def inner():
#         a=10
#         print(a)        #10
#     inner()
#     print(a)            #15
#
# outer()

# -----------------------------------

# def outer():
#     a=20
#     def inner():
#         nonlocal a
#         a=30
#         print(a)            #30
#     inner()
#     print(a)                #30
#
# outer()

# ---------------------------------------

# a = 100
# b = 19
# def func():
#     global a,b
#     a += 10         # a = a + 10
#     b += 10
#     print(a)
#     print(b)
#
# print(a, b)
# func()
# print(a, b)

#-----------------------------------
# a = 10
# def spam():
#     b = 20
#     def display():
#         global a
#         nonlocal b
#         c = 100
#         b += 20
#         a += 10
#
#     display()
#     print(b)
# spam()
# print(a)

# #-------------------------------------------------
# a = 10
# def spam():
#     global a
#     a = 100
#     def display():
#         print(a)
#     display()
#
# spam()
# print(a)

# -----------------------------------------------

# x=1
# def outer():
#     global x
#     x=2
#     def inner():
#         global x                  # non local occurs only one time out side of the function
#         x=3
#         print(f'inner sees x equal to {x}')
#         return
#     inner()
#     print(f'outer sees x equal to {x}')
#     return
# outer()
# print(f'global sees x equal to {x}')

# -------------------------------------------------

'''default dict :

* In Normal dictionaries a key cannot be updated without initialization, that is updation can only be done 
  after initialization.
* In default dict, updation as well as initialization can be done simultaneously'''


'''wap to create a dict of ele and its count pair'''

# a= 'she sells seashells on the seashore'

# d={}
# for char in a:
#     if char in d:
#         d[char] += 1
#     else:
#         d[char] = 1
#
# print(d)

# ------------------

# using default dict

# from collections import defaultdict
#
# dd = defaultdict(int)
# for char in a:
#     dd[char] += 1
#
# print(dd)

# -------------------------------------

# from collections import defaultdict
#
# a = 'karnataka'
#
# def_dict = defaultdict(int)
# for ele in a:
#     def_dict[ele] += 1
#
# print(def_dict)


#------------------------------------------

'''wap to create a dict of ele, starting from the letter'''

# s = 'python is a programming language and programs are fun'

# {p:[python, programming, programs], i:[is], a:[a, and, are], l:[language], f:[fun]}

# s_ = s.split()
# print(s_)
# d = {}
# for ele in s_:
#     if ele[0] not in d:
#         d[ele[0]] = [ele]
#     else:
#         d[ele[0]] += [ele]      #d[ele[0]] = d[ele[0]] + [ele]
#
# print(d)

#------------------
# s = 'python is a programming language and programs are fun'
#
# from collections import  defaultdict
#
# def_dict = defaultdict(list)
# for ele in s.split():
#     def_dict[ele[0]] += [ele]
#
# print(def_dict)