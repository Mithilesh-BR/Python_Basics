''' MAP FUNCTION

map() applies a function to all the items in an input_list(iterable).
Syntax: map(function_to_apply, list_of_inputs) ⇒ map object

map() function takes another function and a sequence of iterables as parameters and returns the output
after executing the function to each item in the sequence'''

# num_list = [1, 2, 3, 4, 6, 1, 2, 3, 9, 90, 87, 88]

# odd_nums = map(lambda n:n*n, num_list)
# print(list(odd_nums))

# -------------------------

# res = map(lambda n : 'even' if n%2==0 else 'odd', num_list)
#
# print(res)              #<map object at 0x00000184DB7FB6D0>
# print(list(res))

# --------------------------

# names_list =['malayalam', 'radar', 'mom', 'hai', 'hello', 'dad']
#
# res = map(lambda n : n==n[::-1], names_list)            # by using map we get boolean answer
# print(res)
# print(list(res))
#
# ----------------------------------

# names_list =['malayalam', 'radar', 'mom', 'hai', 'hello', 'dad']
#
# def s(n):
#     if n == n[::-1]:
#         return 'Palindrome'
#     else:
#         return 'not a palindrome'
# #
# res = map(s, names_list)
# print(res)
# print(list(res))

#-----------------------------------------

'''wap to check if the number is prime or not using map'''

# def is_prime(num):
#     for ele in range(2, num):
#         if num % ele == 0:
#             return f'{num} is not prime'
#     else:
#         return f'{num} is prime'
#
# res = map(is_prime, range(2, 10))
# for element in res:
#     print(element)

## --------------------
''' FILTER

The filter()is a function and it takes an iterable as argument.
This offers an elegant way to filter out all the elements of a sequence, for which the function returns True.
Filter creates an object of elements for which a function returned value will be True.
Syntax: filter(func, iterable) ⇒ object'''

# names_list =['malayalam', 'radar', 'mom', 'hai', 'hello', 'dad']
#
# res = filter(lambda n : n==n[::-1], names_list)
#
# print(res)               #filter object
# print(list(res))                                # by using filter we get actual answers


'''wap to print all the prime numbers from 2-20 using filter'''

# def is_prime(num):
#     for ele in range(2, num):
#         if num % ele == 0:
#             break
#     else:
#         return num
#
# res = map(is_prime, range(2, 9))
# print(list(res))
# #
# res = filter(is_prime, range(2, 9))
# print(list(res))