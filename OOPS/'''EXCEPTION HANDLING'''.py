'''EXCEPTION HANDLING'''          '''TINKIS'''

# Type Error
# Indentation Error
# Name Error
# Key Error
# Index Error
# Syntax Error



# my_list = [1, 2, 3, 4, 5]'''EXCEPTION HANDLING'''

# my_list = [1, 2, 3, 4, 5]
# print(my_list[5])                   #IndexError

# ---------------------------

# a = 5
# b = '10'

# print(a+b)                          #TypeError

# ---------------------------

# a=10
# print(b)                            #NameError

# ---------------------------

# # a=10
# # print(a                             #SyntaxError

# ---------------------------

# # a=10
# #     print(a)                            #IndentationError

# # -------------------------

# # my_dict = {'a': 1, 'b': 2, 'c': 3}

# # value = my_dict['d']                #KeyError

# # -------------------------

# # a = 10
# # b = 0
#
# # print(a/b)              #ZerodivisionError
#
# #------------------------------------------
# # try:
# #     print(a / b)
# #
# # except:
# #     print('Except block executing')
#
# #--------------------------------------------
# '''EXCEPTION HANDLING'''
'''To handle unexpected termination of the program, exception handling is done.
To handle the exception, try and except block is used.'''

# 1. Default exception
# 2. Specific exception
# 3. Multiple exception
# 4. Generic exception


# #--------------------------------------
'''default exception block '''

# This Block will handle all the exceptions that are raised in try block
# Syntax :
#             try:
# 			    statements
# 			except:
# 			        Statements'''
# a = 10
# b = 0

# # try:
# #     print(a.append(9))                      ##AttributeError
# # except:
# #     print('Except block executing')
#
# #eg2
# # try:
# #     print(variable_name)     ##NameError
# # except:
# #     print('Except block executing')
#
# #------------------------------------
'''specific exception block :'''

# We can create an exception block specific to an error.
# Syntax :
#             try:
# 		       statements
# 		    except <exception_name>:
# 		       Statements'''

# Eg1

# # a = 10
# # b = 0
# # try:
# #     print(a/b)        ##ZeroDivisionError
# # except NameError:
# #     print('Except block executing')

'''In the above example, except block can only handle NameError,
but try block is throwing ZeroDivisionError, so except block can't handle the error thrown by try block.
So we get ZeroDivisionError as output'''

#eg2

# # a = 'hello'

# # try:
# #     print(a.pop())      ##AttributeError

# # except AttributeError:
# #     print('Except block executing')

# #------------------------------------------------------------------
 '''Multiple exception block :'''

# A single try block can have multiple except blocks.

# Syntax :

#         try :
# 		      statements
# 		except exception 1:
# 		       statements
# 		except exception 2 :
# 		        Statements'''

# # try:
# #     print(a)        ##NameError

# # except AttributeError:
# #     print('Except block handling AttributeError executing')
# # except IndexError:
# #     print('Except block handling InderError executing')
# # except ZeroDivisionError:
# #     print('Except block handling ZeroDivisionError executing')


# # ##Eg2

# # try:
# #     print(a)        ##NameError
# # except AttributeError:
# #     print('Except block handling AttributeError executing')
# # except IndexError:
# #     print('Except block handling IndexError executing')
# # except ZeroDivisi
# onError:
# #     print('Except block handling ZeroDivisionError executing')
# # except NameError:
# #     print('Except block handling NameError executing')

# #----------------------------------
'''Generic Exception handling :'''

'''Catching BaseException is a really bad idea, because you'll swallow every type of Exception,
including KeyboardInterrupt, the exception that causes your program to exit when you send a
SIGINT (Ctrl-C). Don't do it.'''

# Handles all types of exceptions in a single except block.
# Syntax :
#         try :
# 			statements
# 		except Exception/BaseException as alias_name:
# 			Statements'''

# # #Eg1
# # a = 10
# # b = 0

# # try:
# #     print(a.append(9))

# # except BaseException as error_msg:
# #     print('Except block executing')
# #     print(error_msg)

# # ##Eg2
# # try:
# #     print(x)
# # except NameError as error_msg:
# #     print('Except block executing')
# #     print(error_msg)

# #-------------------------------------------------------------------------------------
'''as keyword: Used to give alias name for the exception names written in the except block.

Syntax :	except <exception name> as alias_name:'''
# --------------------------------------------------------------------------------------
'''else:
It is a block which will get executed when the exception is not raised in the try block.'''

# Syntax :
#         try :
# 			statements
# 		except:
# 			statements
# 		else:
# 			Statements'''

# # a = 10
# # b = 8
# # try:
# #     res = b/a
# # except:
# #     print('except block executing')
# # else:
# #     print('else block executing')
# #     print(res)

# ##Eg2
# # a = 10
# # b = 0
# # try:
# #     print('try executing')
# #     res = a/b
# # except:
# #     print('**************************')
# #     print('except block executing')
# # else:
# #     print('**************************')
# #     print('else block executing')
# #     print(res)

# #-------------------------------------------------------------------------

'''finally :
# * It is a block which will get executed even when the exception is raised or not.

# It defines a block of code to run when the try... except...else block is final.
# The finally block will be executed no matter if the try block raises an error or not.
# This can be useful to close objects and clean up resources.'''

# Syntax :
#         try :
# 			statements
# 		except:
# 			statements
# 		finally :
# 			Statements'''

# # a = 10
# # b = 0

# # try:
# #     res = a/b
# # except NameError:
# #     print('Except block executing')
# # else:
# #     print(res)
# # finally:
# #     print('hello world')

# ##Eg2

# # a = 10
# # b = 0
# # try:
# #     res = a/b
# # except:
# #     print('Except block executing')
# # else:
# #     print(res)
# # finally:
# #     print('hello world')

# #--------------------------------------------------------------------
'''raise
# * Used to raise a specific exception whenever the condition is matched.
# * Once an exception is raised, it searches for the specific except block and handles the exception.'''

# Syntax :	raise error_name(“message”)'''

# # a = 10
# # if a > 35:
# #     print('pass')
# # else:
# #     raise NameError


# # a = 10
# # if a > 35:
# #     print('pass')
# # else:
# #     raise AttributeError('The value of a is less than 35')

# #-----------------------------------------------------------------
'''wap to handle key error while creating dict of word and its count pair'''

# # l = ['hello', 'hai', 'hai', 'python']       #{hello:1, hai:2, python:1}
# # # Using for loop
# # d = {}
# # for word in l:
# #     if word not in d:
# #         d[word] = 1
# #     else:
# #         d[word] += 1
# # print(d)

'''Using exception handling'''

# # l = ['hello', 'hai', 'hai', 'python']
# # d = {}
# # for word in l:
# #     try:
# #         d[word] += 1
# #     except KeyError:
# #         d[word] = 1

# # print(d)        ## {hello:1, hai:2, python:1}

# #---------------------------------------------------------------
'''wap to handle the ZeroDivisionError in the list, print the result of the division
if there is no exception, and print the numbers for all iterations'''

# # l = [(2, 3), (9, 0), (9, 6), (5, 0), (8, 0), (1, 9), (4, 0)]
# # for ele in l:      #For each tuple, 0th index of element is 2 and 1st index of element is 3 and viceversa
# #     try:
# #         res = ele[0]/ele[1]
# #     except ZeroDivisionError:
# #         print('Except block is executing')
# #     else:
# #         print(res)
# #     finally:
# #         print(f'The numbers are {ele[0]} and {ele[1]}')
# #     print('**********************************')

# #-----------------------------------------------------------------------
# '''wap to find the factorial of a num, if the num is invalid, raise exception'''

# # num = int(input('Enter the num: '))
# # if num > 0:
# #     fact = 1
# #     for i in range(1, num+1):
# #         fact *= i
# #     print(fact)
# # elif num==0:
# #     print(1)
# # else:
# #     print('cant find fact for neg numbers')


# # import math

# # def fact(n):
# #     if n < 0:
# #         raise TypeError('Invalid number')
# #     elif n == 0:
# #         print(f'The factorial of {n} is 1')
# #     else:
# #         res = math.factorial(n)
# #         print(res)

# # fact(0)
# # fact(4)
# # fact(-9)


# # num = int(input('Enter the num : '))
# # try:
# #     print(math.factorial(num))
# # except BaseException as error_msg:
# #     print(error_msg)

# #---------------------------------------------------------------------------
# # a = 0
# # if a:
# #     print('hai')
# # else:
# #     raise IndexError('index of a is 0')
#
# #------------------------------------------------------------------------
# '''custom exception handling :
#
# * Custom exceptions can be created by inheriting Exception class Or BaseException
# Syntax :
# class user_exception_name(Exception):
# 	pass
# '''
#
# # class DataError(Exception):
# #     pass
# #
# # a = 0
# # if a:
# #     print('hai')
# # else:
# #     raise DataError('value of a is 0')
#
# #---------------------------------------------------------------------

# # class InsufficientFunds(Exception):
# #     pass

# # class Bank:

# #     bank_name = 'Karnataka Grameena Bank'

# #     def __init__(self, name, acc_num, balance):
# #         self.name = name
# #         self.acc_num = acc_num
# #         self.balance = balance

# #     def deposit(self, amount):
# #         self.balance += amount
# #         print(f'Successfully deposited Rs.{amount}')

# #     def withdraw(self, amount):
# #         if amount > self.balance:
# #             raise InsufficientFunds('Insufficient balance')
# #         else:
# #             self.balance -= amount
# #             print(f'Successfully withdrawn Rs.{amount}')

# #     def check_balance(self):
# #         print(f'The remaining balance is Rs.{self.balance}')

# # kgb_1 = Bank('Jyothi', 'kgb1111', 10000)
# # kgb_1.check_balance()
# # kgb_1.deposit(5000)
# # kgb_1.check_balance()

# # kgb_1.withdraw(5000)
# # kgb_1.check_balance()
# # kgb_1.withdraw(50000)
# # kgb_1.check_balance()

# #-------------------------------------------------------------------------

# print(my_list[5])                   #IndexError

# -------------------------------------------------------------------------

# a = 5
# b = '10'
#
# print(a+b)                          #TypeError

# -----------------------

# a=10
#
# print(b)                            #NameError

# -----------------------

# a=10
#
# print(a                             #SyntaxError

# ------------------------

# a=10
#
#     print(a)                            #IndentationError

# -------------------------

# my_dict = {'a': 1, 'b': 2, 'c': 3}
#
# value = my_dict['d']                #KeyError

# ------------------------

# a = 10
# b = 0

# print(a/b)              #ZerodivisionError

#------------------------------------------
# try:
#     print(a / b)
#
# except:
#     print('Except block executing')

#--------------------------------------------
'''EXCEPTION HANDLING'''
'''
* To handle unexpected termination of the program, exception handling is done.
* To handle the exception, try and except block is used.

1. Default exception
2. Specific exception
3. Multiple exception
4. Generic exception
'''

#--------------------------------------
'''default exception block

This Block will handle all the exceptions that are raised in try block
Syntax :
            try:
			    statements
			except:
			        Statements'''

# a = 10
# b = 0
#
# try:
#     print(a.append(9))                      ##AttributeError
# except:
#     print('Except block executing')

#eg2
# try:
#     print(variable_name)     ##NameError
# except:
#     print('Except block executing')

#------------------------------------
'''specific exception block :
We can create an exception block specific to an error.
Syntax :	
            try:
		       statements
		    except <exception_name>:
		       Statements'''
# ##Eg1
# a = 10
# b = 0
# try:
#     print(a/b)        ##ZeroDivisionError
# except NameError:
#     print('Except block executing')

## in the above example, except block can only handle NameError,
## but try block is throwing ZeroDivisionError, so except block can't handle the error thrown by try block.
## So we get ZeroDivisionError as output

##eg2
# a = 'hello'
#
# try:
#     print(a.pop())      ##AttributeError
#
# except AttributeError:
#     print('Except block executing')

#------------------------------------------------------------------------
'''Multiple exception block :

A single try block can have multiple except blocks.
Syntax :	
        try :
		      statements
		except exception 1:
		       statements
		except exception 2 : 
		        Statements'''
# try:
#     print(a)        ##NameError
#
# except AttributeError:
#     print('Except block handling AttributeError executing')
# except IndexError:
#     print('Except block handling InderError executing')
# except ZeroDivisionError:
#     print('Except block handling ZeroDivisionError executing')
#
# ##Eg2
# try:
#     print(a)        ##NameError
# except AttributeError:
#     print('Except block handling AttributeError executing')
# except IndexError:
#     print('Except block handling InderError executing')
# except ZeroDivisionError:
#     print('Except block handling ZeroDivisionError executing')
# except NameError:
#     print('Except block handling NameError executing')

#---------------------------------------------------------------------
'''Generic Exception handling : 

Catching BaseException is a really bad idea, because you'll swallow every type of Exception,
including KeyboardInterrupt , the exception that causes your program to exit when you send a 
SIGINT (Ctrl-C). Don't do it.

Handles all types of exceptions in a single except block.
Syntax :	
        try : 
			statements
		except Exception/BaseException as alias_name: 
			Statements'''
# #Eg1
# a = 10
# b = 0
#
# try:
#     print(a.append(9))
#
# except BaseException as error_msg:
#     print('Except block executing')
#     print(error_msg)

a=10
b=0

try:
    print(a.append(15))

except BaseException as error_msg:
    print('Except block is executing')
    print(error_msg)


# ##Eg2

# try:
#     print(x)
# except NameError as error_msg:
#     print('Except block executing')
#     print(error_msg)

#----------------------------------------------------------------------
'''as keyword: Used to give alias name for the exception names written in the except block.
Syntax :	except <exception name> as alias_name:'''
##----------------------------------------------------------------------
'''else:
It is a block which will get executed when the exception is not raised in the try block.
Syntax :	
        try :
			statements
		except:
			statements
		else:
			Statements'''
# a = 10
# b = 8
# try:
#     res = b/a
# except:
#     print('except block executing')
# else:
#     print('else block executing')
#     print(res)

##Eg2
# a = 10
# b = 0
# try:
#     print('try executing')
#     res = a/b
# except:
#     print('**************************')
#     print('except block executing')
# else:
#     print('**************************')
#     print('else block executing')
#     print(res)

#---------------------------------------------------------------------
'''finally :
* It is a block which will get executed even when the exception is raised or not.

It defines a block of code to run when the try... except...else block is final. 
The finally block will be executed no matter if the try block raises an error or not. 
This can be useful to close objects and clean up resources.

Syntax :	
        try :
			statements
		except:
			statements
		finally :
			Statements'''
# a = 10
# b = 0
# try:
#     res = a/b
# except NameError:
#     print('Except block executing')
# else:
#     print(res)
# finally:
#     print('hello world')

##Eg2
# a = 10
# b = 0
# try:
#     res = a/b
# except:
#     print('Except block executing')
# else:
#     print(res)
# finally:
#     print('hello world')

#---------------------------------------------------------------------------
'''raise 
* Used to raise a specific exception whenever the condition is matched.
* Once an exception is raised, it searches for the specific except block and handles the exception.

Syntax :	raise error_name(“message”)'''

# a = 10
# if a > 35:
#     print('pass')
# else:
#     raise NameError

# a = 10
# if a > 35:
#     print('pass')
# else:
#     raise AttributeError('The value of a is less than 35')

#--------------------------------------------------------------------------
'''wap to handle key error while creating dict of word and its count pair'''

l = ['hello', 'hai', 'hai', 'python']       #{hello:1, hai:2, python:1}

d = {}
for word in l:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
print(d)

# Using exception handling
# l = ['hello', 'hai', 'hai', 'python']
# d = {}
# for word in l:
#     try:
#         d[word] += 1
#     except KeyError:
#         d[word] = 1

# print(d)        ## {hello:1, hai:2, python:1}

#-------------------------------------------------------------------------
'''wap to handle the ZeroDivisionError in the list, print the result of the division
if there is no exception, and print the numbers for all iterations'''

# l = [(2, 3), (9, 0), (9, 6), (5, 0), (8, 0), (1, 9), (4, 0)]
# for ele in l:      #For each tuple, 0th index of element is 2 and 1st index of element is 3 and viceversa
#     try:
#         res = ele[0]/ele[1]
#     except ZeroDivisionError:
#         print('Except block is executing')
#     else:
#         print(res)
#     finally:
#         print(f'The numbers are {ele[0]} and {ele[1]}')
#     print('**********************************')

#---------------------------------------------------------------------------
'''wap to find the factorial of a num, if the num is invalid, raise exception'''

# num = int(input('Enter the num: '))
# if num > 0:
#     fact = 1
#     for i in range(1, num+1):
#         fact *= i
#     print(fact)
# elif num==0:
#     print(1)
# else:
#     print('cant find fact for neg numbers')


# import math

# def fact(n):
#     if n < 0:
#         raise TypeError('Invalid number')
#     elif n == 0:
#         print(f'The factorial of {n} is 1')
#     else:
#         res = math.factorial(n)
#         print(res)

# fact(0)
# fact(4)
# fact(-9)


# num = int(input('Enter the num : '))
# try:
#     print(math.factorial(num))
# except BaseException as error_msg:
#     print(error_msg)

#-------------------------------------------------------------------------
# a = 0
# if a:
#     print('hai')
# else:
#     raise IndexError('index of a is 0')

#--------------------------------------------------------------------------
'''custom exception handling :

* Custom exceptions can be created by inheriting Exception class Or BaseException
Syntax :	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
class user_exception_name(Exception):
	pass
'''

# class DataError(Exception):
#     pass

# a = 0
# if a:
#     print('hai')
# else:
#     raise DataError('value of a is 0')

#----------------------------------------------------------------------------

# class InsufficientFunds(Exception):
#     pass

# class Bank:
#     bank_name = 'Karnataka Grameena Bank'

#     def __init__(self, name, acc_num, balance):
#         self.name = name
#         self.acc_num = acc_num
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f'Successfully deposited Rs.{amount}')

#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise InsufficientFunds('Insufficient balance')
#         else:
#             self.balance -= amount
#             print(f'Successfully withdrawn Rs.{amount}')

#     def check_balance(self):
#         print(f'The remaining balance is Rs.{self.balance}')

# kgb_1 = Bank('Jyothi', 'kgb1111', 10000)
# kgb_1.check_balance()
# kgb_1.deposit(5000)
# kgb_1.check_balance()

# kgb_1.withdraw(5000)
# kgb_1.check_balan
# kgb_1.withdraw(50000)
# kgb_1.check_balance()

#-----------------------------------------------------------------------------

