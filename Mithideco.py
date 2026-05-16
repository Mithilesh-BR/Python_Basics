# def greet(name,education,rank):
#     print(f"Hi {name},how are you ?")
#     print(f"you have done {education},but still have no value in society")
#
#     print(f"because of your hard work, you are rank is {rank} ")
#
# greet('Mithilesh','engineering',5+4546+449)
# greet('keerthi','engineering',6461)

# def add(*num):
#     c=5
#     print(num[0])
#     for i in num:
#         c=c+i
#     print(f'sum of num is {c}')
#
# add(1,2,3,4,5)
# add(6,7,6)

# def student_details(*args,**kwargs):
#     for a,b in kwargs.items():
#         print(a,b)
#     print(args)
#
# student_details(45,484,6,4848, name='Gautham',age=56,dept='spirituality')
# student_details(454,name='Ganesh',subject='science')
# student_details(1,5,9,94,9,name='Mithi',profession='Automation Expert')

# def multiply(*args):
#     c=1
#     for i in args:
#         c*=i
#     print(f'the multiplication of the given number is {c}')
#
# multiply(2,3,4,5,6,-8)
# multiply(5,8,6)

# def shout(text):
#     return text.upper()
#
# def whisper(text):
#     return text.upper()
#
# def greet(func):
#     greeting = func('Hi, Hindus please shout Jai Sri Sita Raam')
#     print (greeting)
#
# greet(shout)
# greet(whisper)

# def create_adder(x):
#     def adder (y):
#         return x+y
#     return adder
#
# add_15=create_adder(15)
# print(add_15(35))
#
# def hello_decorator(func):
#     def inner1():
#         print('Hello, this is before function execution')
#         func ()
#         print('This is after the function execution')
#     return inner1
#
# def function_inside():
#     print('This is inside the function')
#
# function_inside = hello_decorator(function_inside)
#
# function_inside()

# import time
# import math
#
# def calculate_time(func):
#     def inner1(*args,**kwargs):
# #
#         begin=time.time()
#         func (*args,**kwargs)
#         end=time.time()
#
#         print('Total time taken in : ', func.__name__, end - begin)
#     return inner1
# #
# @calculate_time
# def factorial (num):
#     time.sleep(2)
#     print(math.factorial(num))
#
# factorial(10)
#
#
# @calculate_time
# def factorial (num):
#     time.sleep(3)
#     print(math.factorial(num))
#
# factorial(5)

