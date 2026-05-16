
'''DECORATOR

Decorator is a function which is used to add some extra functionality/features to the existing function

Decorators can be used when we have common pre-task and post-task for doing some operations

Decorators contains main function and decorator function, without modifing main function,
we should write a extra function

A single decorator can decorate many number of function

def decorator_name(function):
    def inner(*args,**kwargs):
        pre-task
        result = function(*args,**kwargs)    # call main func(), inside the inner with arguments
        post-task
        return result
    return inner

print(def decorator_name(function))                   #call function
print(def decorator_name)                           #gives address
'''


# def spam(func, *args, **kwargs):
#     print('In spam')
#     func(*args, **kwargs)
#     print('In display')

# spam(func,*args, **kwargs )

# def add(a, b):
#     print(a + b)
#
# spam(add, 2, 5)

#----------------------------------

# def outer(func):
#     def inner(*args, **kwargs):
#         print('In spam')
#         func(*args, **kwargs)
#     return inner

# @outer                      #add = outer(add)
# def add(a, b):
#     print(a + b)

# add(11, 4)

# -------------------

# def outer(func):
#     def inner(*args, **kwargs):
#         print('In spam')
#         func(*args, **kwargs)
#     return inner

# @outer                      #rev_str = outer(rev_str)
# def rev_str(n):
#     print(n[::-1])
#
# rev_str('python')

#-----------------------------------------------

'''write a decorator to reverse the string'''

# def outer(func):
#     def inner(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res[::-1]
#     return inner
#
# @outer              #string = outer(string)
# def string(str):
#     return str
#
# print(string('selenium'))

#---------------------------------------------

# def outer(func):
#     def inner(*args, **kwargs):
#         total = len(args) + len(kwargs)
#         print(total)
#         func(*args, **kwargs)
#     return inner
#
# @outer                      #spam = outer(spam)
# def spam(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# spam(1, 2, 3, 4, 5,'hai',a=10, b=20, c=30, d=100, z=10000)

#------------------------------------------------------------------------------

# def outer(func):
#     def inner(*args, **kwargs):
#         total = 0
#         for ele in args:                  # _ -----> Through away variable
#             total += 1
#         for ele in kwargs:                # _ -----> Through away variable
#             total += 1
#         print(total)
#         func(*args, **kwargs)
#     return inner
#
# @outer      #spam = outer(spam)
# def spam(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# spam(1, 2, 3, 4, 5, a=10, b=20, c=30, d=100, z=10000, m='hai')

#--------------------------------------

def outer(func):
    def inner(*args, **kwargs):
        total_args = 0
        total_kwargs = 0
        for ele in args:
            total_args += 1
        for ele in kwargs:
            total_kwargs += 1

        print(f'The total number of positional args are {total_args}')
        print(f'The total number of keyword args are {total_kwargs}')
        func(*args, **kwargs)
    return inner

@outer      #spam = outer(spam)
def spam(*args, **kwargs):
    print(args)
    print(kwargs)
    pass
#
# spam(1, 2, 3, 4, 5, a=10, b=20, c=30, d=100, z=10000, m='hai')

# ----------------------------------------------

'''wap which should give 5 seconds of delay time'''

# from time import sleep
#
# def delay(function):
#     def inner(*args,**kwargs):
#         sleep(3)
#         res = function(*args,**kwargs)
#         return res
#     return inner

# @delay
# def greet():
#     return "hello world"
# print(greet())

# @delay
# def greeting(name):
#     return f"hello {name}"
# print(greeting('Indian'))


# --------------------------------------------------
# ----------------------------------------------------

# def rev(func):
#     def inner(*args,**kwargs):
#         res = func(*args,**kwargs)
#         if type(res)==str:
#             return res[::-1]
#     return inner
#
# @rev
# def string(str):
#     return str
#
# print(string('selenium'))


# -----------------------------------------------

# def code(func):
#     def inner(*args,**kwargs):
#         res = func(*args, **kwargs)
#         if type(res) == str:
#             return ord(res[0])
#     return inner
#
# @code
# def string(str):
#     return str
#
# print(string('apython'))

# -----------------------------------------------

# def post(func):
#     def inner(*args,**kwargs):
#         res = func(*args, **kwargs)
#         if type(res) == float:
#             return abs(res)
#     return inner
#
# @post
# def num(n):
#     return n
#
# print(num(-12.5))

# ------------------------------------------------










# -------------------------------------------------------------------------
# 1.

# def my_decorator(my_function):
#     def wrapper():
#         print("run before the task")
#         my_function()
#         print("run after the task")
#     return wrapper
#
# @my_decorator
# def run_task():
#     print("running task.....")
#
# run_task()

"""2. count how many times we are calling functions"""

# count=0
# def count_(func):
#     def wrapper (*args,**kwargs):
#         global count
#         count += 1
#         func(*args, **kwargs)
#     return wrapper
#
# @count_
# def add(a,b):
#     print(f"sum of the two numbers:{a+b}")
# add(3,6)
# add(5,6)
# add(8,6)
# add(2,9)
# add(7,6)
#
# print(f"{count} times the add function is used")

# ---------------------------------------------------
"""3. to delay 8sec before execution of function:"""

# from time import sleep
#
# def delay(func):
#     def inner (*args, **kwargs):
#         sleep(8)
#         func(*args, **kwargs)
#     return inner
#
# @delay
#
# def add(a,b):
#     print(f"sum of two numbers:{a+b}")
# add(3,6)


# -----------------------------------------------------------
"""4. print wish message before executing function"""

# def deco(func):
#     def inner (*args, **kwargs):
#         print("Hello guys good afternoon")
#         func(*args, **kwargs)
#         print("cricket")
#     return inner
#
# @deco
# def display_(msg):
#     print(msg)
# display_("welcome to python class")
#
# print()
#
# @deco
# def class_(boys, girls):
#     print (f'total class strength:{boys+girls}')
# class_(6,9)

#   ----------------------------------------------------------------
"""5. find the execution time of a function"""

# import time
# #
# def ex_time(func):
#     def inner (*args, **kwargs):
#         start_time=time.time()
#         result=func(*args, **kwargs)
#         end_time=time.time()
#         execution_time = end_time - start_time
#         print(f"The execution time is : {execution_time:.4f}")
#         # return result
#     return inner
#
# @ ex_time
# def add(a,b):
#     time.sleep(5)
#     print(f'sum of two numbers:{a+b}')
# add(3,6)
#
# ==================================================
# #
# import time
# from functools import wraps
#
# def measure_time(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f"Function {func.__name__} executed in {execution_time:.4f} seconds")
#         return result
#     return wrapper
#
#
# @measure_time
# def my_function():
#     time.sleep(5)
# my_function()