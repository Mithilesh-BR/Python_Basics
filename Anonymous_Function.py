''' ANONYMOUS FUNCTION :

An anonymous function is a function that is defined without a name.

While normal functions are defined using the def keyword in Python,
anonymous functions are defined using the lambda keyword.



# __________________________________________________________________
Syntax: Var = lambda < arguments > : expression
# __________________________________________________________________


'if-else'

Syntax: Var = lambda < arguments > :TSB if < condition > else FSB

To call a fun
Var( Val1, Val2, .....)

'''
# ________________________________________________

'''1. write a lambda expression to add 2 numbers'''

# res = lambda a, b : a + b
#
# print(res(9, 3))
# print(res(a=2, b=9))


#------------------------------------------

'''2. Program to find the sum of variable number of arguments'''

# res = lambda *args : sum(args)
#
# print(res(2, 3, 4, 5))

#---------------------------------------

'''3. write a lambda expression to reverse a string'''

# rev = lambda str:str[::-1]
#
# print(rev('king kholi'))

# ___________________________________________________

'''4. wap to check if the num is even or odd'''
# def even_odd(n):
#     if n % 2 == 0:
#         print('even')
#     else:
#         print('odd')
#
# even_odd(8)

# ------____________________________________

# res = lambda n : n % 2 == 0
# print(res(7))
# # print(res(9))

# res = lambda n : 'even' if n%2==0 else 'odd'
# print(res(8))
# # print(res(9))

#-------------------------------------------

# num_list = [1, 2, 3, 4, 6, 1, 2, 3, 9, 90, 87, 88]
#
# res = lambda num_list : ['even' if ele%2==0 else 'odd' for ele in num_list]
# print(res(num_list))
#
# def even(num_list):
#     for ele in num_list:
#         if ele % 2 == 0:
#             print('even')
#         else:
#             print('odd')
#
# even([1, 2, 3, 4, 6, 1, 2, 3, 9, 90, 87, 88,  ])


# ___________________________________________________________________

'''5. wap to add the elements present in the list'''

# num = [1,2,3,4,5]
# def add(num):
#     count = 0
#     for ele in num:
#         count = count + ele
#         print(count)
# add(num)

# -----------------------------------------

'''6. wap to check the string is palindrome or not'''

# palindrome_or _not = lambda s:'palindrome' if s[::-1] else 'Not palindrome'
# print(palindrome_or_not)

# def palindrome(str):
#     if str == str[::-1]:
#         print('Palindrome')
#     else:
#         print('Not a Palindrome')
#
# palindrome('mom')

# res = lambda str : 'Palindrome' if str == str[::-1] else 'Not a palindrome'
# print(res('radar'))
# print(res('python'))

# ----------------------------------_______________________________________

'''7. wap to check the given number is perfect square or not'''

# sq = int(input('Enter: '))                #9
# res = sq ** 0.5                           #9 ** 0.5 -->3.0
# if sq == int(res)** 2:                    #9 == int(3.0)**2 --> 9== 3**2 --> 9==9
#     print('perfect square')
# else:
#     print('Not a perfect square')


# num = 16
# res = num ** 0.5
# result = lambda n : 'perfect square' if n == int(res)**2 else 'not perfect square'
# print(result(num))

#--------------------------------------------

'''8. wap to get the last element of the iterable'''

# res = lambda a : a[0:15:2]
#
# print(res('python is fun'))

#--------------------------------------------

'''9. op of the following expression  a^2 + b^2 + 2ab'''


# def formula(a, b):
#     print((a + b) * (a + b))
#
#
# formula(5, 2)

# ----------------------
# def formula(a,b):
#
#     print((a**2 + b**2 + 2*a*b))
#
# formula(2,3)
#
# # ----------------
#
# res = lambda a, b : a**2 + b**2 + 2*a*b         #4 + 25 + 20
# print(res(a=2, b=3))

# ------------------------------------------_________________
#
'''10.wap to find the cube of any num'''

# res = lambda num : num ** 3
#
# print(res(2))

#----------------------------------------

'''11. wap to get the last/First digit of the number'''

# res = lambda num : str(num)[3]
#
# print(res(678538))