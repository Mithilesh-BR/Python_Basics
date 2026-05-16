# '''Return'''
#
# def add(a,b):
#     print(a+b)
#
# add(3,5)
#
# # ----------
#
# def add(a,b):
#     return a+b
#
# print(add(3,5))

# -------------
'''1. wap to get sum of two numbers'''

# def add():
#     a = int(input('enter the number:'))
#     b = int(input('enter the number:'))
#     return a+b
#
# print(add())

# ------------------------------------
'''2. wap to extract first letter from given string'''

# def char(str):
#     return(str[0])
#
# print(char('hello'))

# -------------------------

'''3. wap to extract upper case char in given string'''

# def u(str):
#     for char in str:
#         if char.isupper():
#             return char             # single char as output, but we should get more
# print(u('khOli'))

# print(dir(str))

# -------------------------------------
'''4. wap tp num from 0-10'''

# def num(start,end):
#     for i in range(start,end):
#         return i
# print(num(0,10))

# ------------------------------------------
'''5.'''
# def func():
    # return 'hai'
    # return 'hello'
    # return 'python'

# res = func()
# print(res)

# We can have multiple return statements in the function, but only one return gets executed
# -------------------------------

'''6. Wap to check the given number is even or not'''

# def even_odd(num):
#     if num%2 == 0:
#         return 'even'
#     else:
#         return 'odd'
#
# res = even_odd(9)
# print(res)

#---------------------------------------------
'''7. wap tp reverse the string'''

# str_1 = 'python'
# str_2 = 'selenium'
#
# def reverse(variable):
#     rev_str = ''
#     for ele in variable:
#         rev_str = ele + rev_str
#     return f'The reverse of {variable} is {rev_str}'
#
# print(reverse(str_1))
# print(reverse(str_2))

'''  rev = ele + rev
      '' =  p  +  ''
       p =  y  +  p
      yp =  t  +  yp
     typ =  h  +  typ
    htyp = o  +  htyp
   ohtyp = n  +  ohtyp
  nohtyp '''

#--------------------------------------------
'''8.'''
# def virat(a, b):
#     return a + b
#
# res = virat(2, 4)
# print(res)

#-------------------------------------
'''9.wap tp the length of given string'''

# def length_(str):
#     length = 0
#     for ele in str:
#         length += 1

    # '''length = length + 1
    #     0     =   0  +  1
    #     1     =   1  +  1
    #     2     =   2  +  1
    #     3     =   3  +  1
    #     4     =   4  +  1
    #     5'''

#     return length
#
# res = length_('abcd')
# print(res)

# ---------------------------------------------


'''ARGUMENTS'''

'''1. POSITIONAL ARGUMENTS'''

'''To accept/pass 0 to n number of positional arguments, we have to prefix * before argument
and positional argument. It will get stored into a tuple'''

# def cars(*args):
#     print(type(args))
#     return args                         #<class 'tuple'>
# print(cars('kia','MG'))                 #('kia', 'MG')

# ----------------------------------------------

'''positional only arguments ( / ):  The arguments before the / should be positional arguments,
 the elements after / can either be positional or keyword arguments'''

# def add(a, b, c, /, e, d, f):
#     print(a + b + c + d + e + f)
#
# add(1, 2, 3, 4, 5, 6)
# add(1, 2, 3, d=5, e=4, f=6,)
# add(a=1, b=2, c=3, d=4, e=5, f=6)       #TypeError

# -----------------------------------------

'''positional arguments: mandatory arguments'''

# def greet(name, age):
#     return f'My name is {name} and I am {age} years old'
# #
# print(greet('Hanuman', 1000))
# print(greet(1000,'Hanuman'))

# -----------------------------------------

'''2. KEYWORD ARGUMENTS'''

'''To accept/pass 0 to n number of keyword arguments, we have to prefix ** before arguments
and keyword argument. It will get stored into a dictionary'''

# def sample(**kwargs):
#     print(type(kwargs))
#     return kwargs                       #<class 'dict'>
# print(sample(a=0,b=1,c=2))              #{'a': 0, 'b': 1, 'c': 2}

# -------------------------------------------------

'''keyword only arguments ( * ):  The arguments after the * should be keyword arguments,
 the elements before * can either be positional or keyword arguments'''
# def add(a, b, c, *, d, e, f):
#     print(a + b + c + d + e + f)
#
# add(1, 2, 3, d=4, e=5, f=6)
# # add(1, 2, 3, 4, 5, 6)                   #TypeError
# add(1, b=2, c=4, d=5, e=6, f=10)

# --------------------------------------------------

'''keyword arguments: not mandatory, bcoz it has default values'''

# def greet(name, age, place):
#     print(f'My name is {name} and I am {age} years old and I am from {place}')
#
# greet(name='Hanuman', age=1000, place='Anjanadri')
# greet(place='Anjanadri', age=1000, name='Hanuman')

# --------------------------------------------------

'''3. COMBINATION ARGUMENTS'''

# def sample(*args,**kwargs):
#     return args,kwargs
# print(sample(1,2,3,1,b=2))                #((1, 2, 3), {'a': 1, 'b': 2})

#---------------------------------------
'''combination of positional and keyword arguments:'''
# def add(a, b, c, d, e, f):
#     print(a + b + c + d + e + f)

# add(1, 2, 3, 4, 5, 6)
# add(a=1, b=2, c=3, d=4, e=5, f=6)
# add(1, 2, 3, d=4, e=5, f=6)
# add(a=1, b=2, 3, 4, 5, 6)     #SyntaxError
# add(1, 2, c=3, 4, 5, 6)         #SyntaxError
# add(1, 2, 3, a=1, b=2, c=3)     #TypeError
# add(1, 2, 3, d=1, e=2, f=3)     #12

#---------------------------------------
'''combination of positional only and keyword only arguments'''

# def add(a, b, /, c, *, d, e, f):
#     print(a + b + c + d + e + f)
#
# add(1, 2, c=4, d=4, e=10, f=8)

# --------------------------------

# def add(a, b, *, c, /, d, e, f, *, g, h, i):
#     print(a + b + c + d + e + f + g+ h + i)
#
# add(1, 2, c=4, d=4, e=10, f=8, g=10, h=5, i=4)      #SyntaxError: / must be ahead of *
#
# --------------------------------------
# -------------------------------------


# def func(*args):
#     print(args)
#
# func('hai', 1, 2, 3, True, 10, 'python', '100')

# -------------------------------

# def numbers(*args):
#     print(args)
#
# numbers(1, 2, 3, 4, 4, 5, 6)

# --------------------------------

# def numbers(**kwargs):
#     print(kwargs)
#
# numbers(a=1, b=2, c=3, d=4, e=4, f=5, g=6)

# ------------------------------------

# def numbers(*args, **kwargs):
#     print(args, kwargs)
#
# numbers(1, 2, z=3, d=4, e=4, f=5, g=6)

#-------------------------------------------------