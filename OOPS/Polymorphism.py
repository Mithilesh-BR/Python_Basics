'''POLYMORPHISM

Same function gives different result depend upon object of different class/type
it is achieve by overridden concept'''



## polymorphism wrt operators

# print(1 + 2)
# print(11.0 + 2.2)
# #
# print('hai' + 'hello')      #haihello

##------------------------------------------------------
## POLYMORPHISM wrt inbulit func

# print(len('python'))        ##characters
# print(len(['hai', 'hello', 'hey', 'python', 'pen', 10, 100, 2.3, True]))  ##elements
# print(len({1:1, 2:2, 3:3}))       ## key value pair

#--------------------------------------------------------
## wrt USER DEFINED functions

# def add(a, b=10, c=2):
#     print(a + b + c)

# add(1, 2, 3)
# add(1, 2)
# add(1)
# add()

#------------------------------------------------------
## POLYMORPHISM wrt CLASS

# class Sample:
#
#     def display(self):
#         print('Sample class display method executing')
#
#
# class Demo:
#
#     def display(self):
#         print('Demo class display method executing')
#
# s = Sample()
# d = Demo()
# s.display()
# d.display()

#-----------------------------------------------------------

# class ConsoleLogger:
#
#     def log(self, message):
#         print(message)
#
# class FilteredConsoleLogger(ConsoleLogger):
#
#     def log(self, message):
#         if 'error' in message:
#             super().log(message)
#         else:
#             raise Exception
#
# f = FilteredConsoleLogger()
# f.log('This is error message')
#
# f1 = FilteredConsoleLogger()
# f1.log('The is message')

#---------------------------------------------------------

# class Textfilelogger:
#
#     def __init__(self, file_obj):
#         self.file_obj = file_obj
#
#     def log(self, msg):
#         self.file_obj.write(msg)
#         self.file_obj.write('\n')
#
# file = open('sample.txt', 'w')
# text_log = Textfilelogger(file)
# text_log.log('This is a message')
#
# class FilteredTextFileLogger(Textfilelogger):
#
#     def __init__(self, file_object):
#         self.file_object  = file_object
#         super().__init__(file_object)
#
#     def log(self, message):
#         if 'error' in message:
#             super().log(message)
#
# with_error = open('spam.txt', 'w')
# without_error = open('sample.txt', 'w')
# logger = FilteredTextFileLogger(without_error)
# logger = FilteredTextFileLogger(with_error)
# logger.log('This error message is stupid')
# logger.log('This error is stupid')


#----------------------------------------------------------

# class ConsoleLogger:
#
#     def log(self, message):
#         print(message)
#
# class FilterLogger(ConsoleLogger):
#
#     def __init__(self, pattern):
#         self.pattern = pattern
#
#     def log(self, msg):
#         if self.pattern in msg:
#             super().log(msg)
#         else:
#             raise Exception
#
# f = FilterLogger('error')
# f.log('this is message')

#-------------------------------------------------------

# class ConsoleLogger:
#
#     def log(self, message):
#         print(message)
#
# class FilterLogger:
#
#     def __init__(self, pattern, logger):
#         self.pattern = pattern
#         self.logger = logger
#
#     def log(self, msg):
#         if self.pattern in msg:
#             self.logger.log(msg)
#         else:
#             raise Exception
#
# c = ConsoleLogger()
# f = FilterLogger('error', c)            # c---> object reference
# f.log('this is message')



#--------------------------------------------------------------
# Polymorphism with class methods:
# _____________________________________
# class India():
#     def capital(self):
#         print("New Delhi is the capital of India.")
#
#     def language(self):
#         print("Hindi is the most widely spoken language of India.")
#
#     def type(self):
#         print("India is a developing country.")
#
# class USA():
#     def capital(self):
#         print("Washington, D.C. is the capital of USA.")
#
#     def language(self):
#         print("English is the primary language of USA.")
#
#     def type(self):
#         print("USA is a developed country.")
#
# obj_ind = India()
# obj_usa = USA()
# for country in (obj_ind, obj_usa):
#     country.capital()
#     country.language()
#     country.type()


# _____________________________________________________________________________________________________
# Polymorphism with Inheritance:
_______________________________________

# class Bird:
#     def intro(self):
#         print("There are many types of birds.")
#
#     def flight(self):
#         print("Most of the birds can fly but some cannot.")
#
#
# class sparrow(Bird):
#     def flight(self):
#         print("Sparrows can fly.")
#
#
# class ostrich(Bird):
#     def flight(self):
#         print("Ostriches cannot fly.")
#
#
# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()
#
# obj_bird.intro()
# obj_bird.flight()
#
# obj_spr.intro()
# obj_spr.flight()
#
# obj_ost.intro()
# obj_ost.flight()

# ___________________________________________________________________________________________________
# Polymorphism with a Function and objects:
----------------------------------------------
# def func(obj):
#     obj.capital()
#     obj.language()
#     obj.type()
#
#
# obj_ind = India()
# obj_usa = USA()
#
# func(obj_ind)
# func(obj_usa)

______________________________________________


# class India():
#     def capital(self):
#         print("New Delhi is the capital of India.")
#
#     def language(self):
#         print("Hindi is the most widely spoken language of India.")
#
#     def type(self):
#         print("India is a developing country.")

#
# class USA():
#     def capital(self):
#         print("Washington, D.C. is the capital of USA.")
#
#     def language(self):
#         print("English is the primary language of USA.")
#
#     def type(self):
#         print("USA is a developed country.")
#
#
# def func(obj):
#     obj.capital()
#     obj.language()
#     obj.type()
#
#
# obj_ind = India()
# obj_usa = USA()
#
# func(obj_ind)
# func(obj_usa)

# ________________________________________________________________________________________________________________
'''polymorphism in Python using inheritance and method overriding:'''
# class Animal:
#     def speak(self):
#         raise NotImplementedError("Subclass must implement this method")
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
#
# # Create a list of Animal objects
# animals = [Dog(), Cat()]
#
# # Call the speak method on each object
# for animal in animals:
#     print(animal.speak())

_________________________________________________________________________________________________________________
'''What is method overriding in polymorphism?
# Method overriding occurs when a subclass provides a specific implementation of a method
# that is already defined in its superclass.
# This allows the subclass to customize or completely replace the behavior of the method inherited from the superclass.
'''
# class Animal:
#     def sound(self):
#         return "Some sound"
#
# class Dog(Animal):
#     def sound(self):
#         return "Bark"
#
# dog = Dog()
# print(dog.sound())  # Output: "Bark"

