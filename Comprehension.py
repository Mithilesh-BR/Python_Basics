'''
COMPREHENSIONS
* it is a phenomenon of creating a new collection by considering less lines of instructions to increase the
efficiency of the program.
* it can be applied only for mutable collection'''

'''SYNTAX :
No condition:
    res = [statements for ele in iterable]

Only if condition
    res = [statements for ele in iterable if <condition>]

Both if-else condition
    res = [True block if <condition> else False block for ele in iterable]'''

# -------------------------------------------------------

'''1. wap to print the squares of numbers in the list'''
#
# num_list = [1, 2, 3, 4, 5]
# res = []
# for num in num_list:
#     res.append(num ** 2)
# print(res)
#
# # Using list Comprehension
# res_ = [num**2 for num in num_list]
# print(res_)
#
# # ## Using set Comprehension
# res_ = {num**2 for num in num_list}
# print(res_)
# -------------------------------------------------

'''2. wap to print the even numbers from 1-50'''
#
# even_list = []
# for ele in range(1, 51):
#     if ele % 2 == 0:
#         even_list.append(ele)
# #
# print(even_list)
#
# ## Using list Comprehension
# list_ = [ele for ele in range(1, 51) if ele%2==0]
# print(list_)
#
# ## Using set Comprehension
# list_ = {ele for ele in range(1, 51) if ele%2==0}
# print(list_)
# -----------------------------------------

'''3. wap to create a list of vowel characters from the given string'''

# string = "hello world welcome to python"
# new_list = []
# for ele in string:
#     if ele in 'aeiouAEIOU':
#         new_list.append(ele)
# print(new_list)
#
# new_list = [ele for ele in string if ele in 'aeiouAEIOU']
# print(new_list)

# ------------------------------------------------------

'''4. wap to filter all the elements thats starts with 'p' from the given collection'''

# languages = ['python','perl','php','java','ruby','js']
#
# new_list = []
# for char in languages:
#     if char[0] == 'p':
#         new_list.append(char)
# print(new_list)
#
# new_list = [char for char in languages if char[0] == 'p']
# print(new_list)

# -----------------------------------------------------

'''5. wap to filter the names which are having more than 3 char'''

# languages = ['python','perl','php','java','ruby','js']
#
# new_list = []
# for char in languages:
#     if len(char)>3:
#         new_list.append(char)
# print(new_list)
#
# new_list = [char for char in languages if len(char)>3]
# print(new_list)
# ---------------------------------------------

'''6. wap to build a list of square numbers from the list'''

# num = [2,4,6,8,16,7,9]
# new_list = []
# for items in num:
#     if items % 2 == 0:
#         new_list.append(items ** 2)
# print(new_list)
#
# new_list = [items ** 2 for items in num if items % 2 == 0]
# print(new_list)

# --------------------------------------------

'''7. wap to get below output'''

# n1 = [1,3,5,7,9]
# n2 = [2,4,6,8,10]           #[3,7,11,15,19]
#
# res =[]
# for odd,even in zip(n1,n2):
#     res.append( odd + even)
#
# print(res)
#
# res = [odd + even for odd,even in zip(n1,n2)]
# print(res)
# ----------------------------------------------

'''8. wap to check the given char is consonants or not, if it is consonant build a list of 
its ASCII code'''

# s = 'hello python'
# res = []
# for char in s:
#     if char not in 'aeoiuAEOIU':
#         res.append(ord(char))
# print(res)
#
# res = [ord(char) for char in s if char not in 'aeiouAEIOU']
# print(res)
# ----------------------------------------------------

'''9. wap to print the element as it is if its len is even else reverse it'''

# data = ['tata', 'siri', 'cricket', 'alexa', 'google', 'chatgpt']
# res = []
# for ele in data:
#     if len(ele) % 2 == 0:
#         res.append(ele)
#     else:
#         res.append(ele[::-1])
# print(res)

##Using comprehension
# res = [ele if len(ele)%2==0 else ele[::-1] for ele in data]
# print(res)
#
# ##Using comprehension
# res = {ele if len(ele)%2==0 else ele[::-1] for ele in data}
# print(res)

# ------------------------------------------------

'''10'''

# data = [100,'hai',10.5,True,'hello']             #[1, 3, 1, 1, 5]
#
# res = []
# for ele in data:
#     if type(ele) in (int,bool,complex,float):
#         res.append('$')
#     else:
#         res.append(len(ele))
# print(res)
#
# res = ['$' if type(ele) in (int,bool,complex,float) else len(ele) for ele in data ]
# print(res)
# ---------------------------------------------

'''11. wap to fetch the elements who's length is less than 7 '''

# data = ['tata', 'siri', 'cricket', 'alexa', 'google', 'chatgpt']
#
# res = [ele for ele in data if len(ele)<7]
# print(res)
#
# res  = []
# for ele in data:
#     if len(ele)<7:
#         res.append(ele)
# print(res)

# ------------------------------------------------

'''12. wap to fetch the elements starting with vowel'''

# data = ['tata', 'siri', 'apple', 'alexa', 'google', 'orange']
# res = [ele for ele in data if ele[0] in 'aeiouAEIOU']
# print(res)
#
# res = []
# for ele in data:
#     if ele[0] in 'aeiouAEOUI':
#         res.append(ele)
# print(res)

# ----------------------------------------------
'''13. Build a list of tuples of ele and its len pair'''

# data = ['tata', 'siri', 'apple', 'alexa', 'google', 'orange']
# res = [(ele, len(ele)) for ele in data]
# print(res)
#
# res = []
# for ele in data:
#     res.append((ele,len(ele)))
# print(res)

# -------------------------------------------------

# res = [ele for ele in range(1, 10) if ele%2 ==0]
# print(res)
#
# res = []
# for ele in range(1, 10):
#     if ele % 2 == 0:
#         res.append(ele)
# print(res)
#
# #
# res = {ele for ele in range(1, 10) if ele%2 ==0}
# print(res)