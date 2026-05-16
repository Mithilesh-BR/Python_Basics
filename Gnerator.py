'''GENERATORS

* Python Generator is used to create python iterator
* This is done by defining a function but instead of the return statement returning from the function,
  use the yield keyword
* A generator is a function that returns an iterator. it generates values using the yield keywords
* Yield keyword suspends/pauses the execution of the function but return statements ends the function

ITERATOR AND ITERABLES

* Everything we can loop over is called iterables. eg:list,tuple,sets,dict,str

list = [1,2,3,4]

for ele in list
    print(ele)

1
2
3
4

* Iterables gives iterators to us
* Iterators are the elements that present inside the iterables
* Both iterators and iterables will be having __iter__ which helps in traversing
* Iterators will be having __next__ in them, but iterables will not have __next__
* Iterables have __len__, iterators donot have __len__
* Iterators will give the iterator object, but iterables will not give any object

__next__ : This returns the next value. This would return the StopIteration error once all the objects
 have been looped through.
We can apply next() only on iterators.

Note : Once an iterator object is traversed completely we can not traverse through it again from the
 beginning until the iterator object is initiated.


RETURN :
* Stops the execution, can't return to the function block.
* Multiple return statements can be written in a function, but only one return gets executed.
* Can return multiple elements, it will not create any object

YIELD:
* Pauses the execution, can return to the function block.
* Multiple yield keywords can be written in a function.
* Can return multiple elements, it will create generator object.
'''

# def func():
#     return 100
#     return 199
#     return 'hai'
#     return 'hello'
# #
# print(func())
# print(func())
# print(func())

# ---------------------
# def func():
#     return 'hai', 100, True, 0, 9.0, 'hello'
#
# print(func())

# --------------------------
# def func():
#     yield 10
#     yield 100
#     yield '1000'
#     yield ['hai', 'hello']
#     yield 'python'
#
# res = func()
# print(res)
#
# for ele in res:
#     print(ele)

# print(list(res))

#----------------
# def func():
#     yield 10
#     yield 100
#     yield '1000'
#     yield ['hai', 'hello']
#     yield 'python'
#
# res = func()
#
# print(next(res))        #10
# print(next(res))        #100
# print(next(res))        #'1000'
# print(next(res))        #['hai', 'hello']
# print(next(res))        #'python'
# print(next(res))

# -----------------------

# l = [10, 20, 30]
#
# def func():
#     yield 10
#     yield 20
#     yield 30
#
# res = func()
# print(next(res))
# print(next(res))
# print(next(res))

# ------------------

# l = [10, 20, 30]
# print(next(l))

#------------------------------------------
# def func():
#     yield 10
#     yield 100
#
# res = func()
# #
# print(res)
# for ele in res:
#     print(ele)
#
# print(list(res))

# -----------------------
#
# print(dir(list))        #__iter__, __len__
# print(dir(res))         #__iter__, __next__

#-------------------------------------------------------
'''1. Generate all the numbers in the range of 1 - 10'''

# Generator function
# def numbers():
#     for num in range(1, 11):
#         yield num
#
# res = numbers()
# print(res)                #<generator object numbers at 0x000001E050AC5700>
# print(list(res))

# Generator expression
# n = (num for num in range(1, 11))
# print(n)                #<generator object <genexpr> at 0x000001494D475700>
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
#-----------------------------------------------------------
'''2. wap which yields the name starting with vowels'''

# names = ['ananya', 'rashmika', 'esha', 'kareena', 'aishwarya', 'urvashi']
#
# ## Generator function
# def starting_with_vowel(names):
#     for name in names:
#         if name[0] in 'aeiouAEIOU':
#             yield name
# #
# res = starting_with_vowel(names)
# print(list(res))

# -------------------

# ## Generator expression
# vowels = (name for name in names if name[0] in 'aeiouAEIOU')
# print(vowels)               #<generator object <genexpr> at 0x000001E70CBD5700>
# print(list(vowels))
#----------------------------------------

'''3. wap to yield even numbers from 1-20'''

# ## Generator function
# def numbers():
#     for num in range(1, 21):
#         if num % 2 == 0:
#             yield num
#
# res = numbers()
# print(list(res))
#
#
# ## Generator expression
# even_num = (num for num in range(1, 21) if num%2==0)
# print(even_num)                       #<generator object <genexpr> at 0x000001DF498F5700>
# print(list(even_num))

# print(next(even_num))
# print(next(even_num))
# print(next(even_num))
# print(next(even_num))


#----------------------------------------

'''4. write a generator func and exp to extract the names which are of even length'''

# names = ['deepika', 'aliya', 'jhanvi', 'yami', 'sara', 'nora']

## generator function
# def even_length(names):
#     for ele in names:
#         if len(ele)%2==0:
#             yield ele
#
# res = even_length(names)
# print(list(res))

# print(next(res))
# print(next(res))
# print(next(res))

## Generator expression
# e = (ele for ele in names if len(ele)%2==0)
# print(e)
# print(list(e))
#------------------------------------------

'''5. wap to yield the names ending with vowel'''

# names = ['Rocky', 'Reena', 'Garuda', 'Kamal', 'Ramika', 'Adheera']
#
# ## generator function
# def even_length(names):
#     for ele in names:
#         if ele[-1] in 'aeiouAEIOU':
#             yield ele
#
# res = even_length(names)
# print(list(res))
# #
# # ## Generator expression
# even = (ele for ele in names if ele[-1] in 'aeiouAEIOU')
# print(even)
# print(list(even))
#---------------------------------------
'''6. wap to print the numbers from 10-1'''

# ## Generator func
# def numbers():
#     for num in range(10, 0, -1):
#         yield num
#
# res = numbers()
# # print(list(res))

## gen exp
# numbers_ = (num for num in range(10, 0, -1))
# # print(list(numbers_))
#
# print(next(res))
# print(next(res))
# print(next(res))
#-----------------------------------
'''7. wap to create a list tuples of word and its length pair'''

# names = ['KGF', 'Bahubali', 'Kantara', 'Rolex', 'PS1', 'RRR']
#
# def element_length_pair(names):
#     for ele in names:
#         yield (ele, len(ele))
#
# res =  element_length_pair(names)
# print(list(res))

## gen exp
# length_pair = ((ele, len(ele)) for ele in names)
# print(list(length_pair))
#-------------------------------------------
'''8. wap to yield numbers from -10 to 0'''

## gen func
# def numbers():
#     for ele in range(-10,1,1):
#         yield ele
#
# res = numbers()
# print(list(res))
#
# ## gen exp
# numbers_ = (ele for ele in range(-10,1,1))
# print(list(numbers_))