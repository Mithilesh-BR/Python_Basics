

'''OOPS'''

'''
Function, generators and decorators are procedural oriented programming technique
Combining data and its functionality and we can wrap it inside something called as object---object oriented programming technique

ADV of OOPS

OOPS is a programming technique, that relies on objects.
Individual objects are grouped into classes.
It integrates real world concepts into program such as inheritance, polymorphism, encapsulation and abstraction

IMP of OOPS

It allows more clarity in programming there by allowing simplicity in solving complex problems.
Code develop using classes and objects can be reused through inheritance
It allows data hiding through encapsulation and abstraction

class and object are main component in oops

class
Blueprint for objects, by using class we can create many objects
It is a logical entity that contains some attributes and methods.
Attributes are the variables that belong to a class. 

Method
When we define a function inside the class, we call it as method.
They are called class attributes and should have the first parameter as self

Self
It holds the address of an object, which is invoking the method  
first parameter is refer to object itself---self
i.e the first parameter for every method will be self
self is not mandatory word but we used everywhere


Object/Instance
It is physical entity of class like a mouse, keyboard, chair, table, pen etc.
It contains states and behaviours
State is represented by the attributes of an object and it reflects the properties of an object.
Behavior is represented by the methods of an object and it reflects the response of an object to other objects.
We can create any number of objects using class
Each and every objects are independent to each other.
The changes made in one object, will not reflect in other objects.
In main function, we create object

Constructor
It is a special method used to create and initialize an object of a class

--
* In case of classes,when you look up for an attribute,python tries to look for that attribute in the instance.
* If the attribute exists in the instance, then it will return the value of the instance attribute
* If the attribute doesn't exist in the instance, it will lookup for the attribute at class level.
* If the attribute exist in the class level, it will return the value of the class attribute.
* Changes made in one object will not effect in other object or in the class '''

'''
class ClassName:
    ...
    ...
    ...

obj_name1 = ClassName     #class address
obj_name2 = ClassName()

'''

# -------------------------------
# class Calculator:
#     def add(self, a, b):      # instance variables, which are assigned values when an object is created
#         print(a + b)
#
#     def sub(self, a, b):
#         print(a - b)
#
#     def mul(self, a, b):
#         print(a * b)
#
#     def div(self, a, b):
#         print(a/b)

# cal1 = Calculator()
# cal2 = Calculator()
# cal3 = Calculator()

# cal1.sub(1, 2)
# cal3.mul(8, 9)
# cal2.div(8, 2)
# cal3.add(2, 9)

'''self - will be holding the address of the invoking object'''

# --------------------------------------------------
# class Calculator:
#
#     x = 10
#     y = 5
#
#     def add(self):
#         print(self.x + self.y)
#
#     def sub(self):
#         print(self.x - self.y)
#
#     def mul(self):
#         print(self.x * self.y)
#
#     def div(self):
#         print(self.x / self.y)
#
# cal1 = Calculator()
# cal1.add()
# cal1.sub()
# cal1.mul()
# cal1.div()

# -------------------------------------
# class Calculator:
#
#     def __init__(self, x, y):   '''  #to iniatialize the object variables
#         self.x = x                # when the obj is created, the init method is automatically called with
#         self.y = y                # the given argument'''
#
#     def add(self):
#         print(self.x + self.y)
#
#     def sub(self):
#         print(self.x - self.y)
#
#     def mul(self):
#         print(self.x * self.y)
#
#     def div(self):
#         print(self.x / self.y)
#
# cal1 = Calculator(3, 5)
# cal1.add()
# cal1.sub()
# cal1.mul()
# cal1.div()

# -------------------------------------------------
## accessing class variable and object variable through object
# class Sample:
#
#     x = 100
#
#     def __init__(self, a):
#         self.a = a
#
#     def display(self):
#         print(f'The value of x is {self.x}')
#
# s1 = Sample(20)                 # combination of class variable and constructor variable
#
# print(s1.x)
# print(s1.a)

# --------------------------
# class Sample:
#
#     x = 100
#
#     def __init__(self, a):
#         self.a = a
#
#     def display(self):
#         print(f'The value of x is {self.x}')
#
# s1 = Sample(20)

# print(s1.x)               # accessing class variable through object
# print(Sample.x)           # Can access class Variable using classname
# Sample.display(s1)        # Acessing display method through classname
# s1.display()              # Accessing display method through object

##
# -------------------------------------------------
# class Point:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

# p = Point(1, 2)
# print(p.a)
# print(p.b)
# print(p.__dict__)       #{'a':1, 'b':2}


# p1 = Point(9, 7)
# print(p1.a)
# print(p1.b)
#
# print(p1.__dict__)      #{'a': 9, 'b': 7}

# p1.a = 100
# print(p1.a)
# print(p1.b)
# print(p1.__dict__)      #{'a': 100, 'b': 7}

# -----------------------------------------------
# class Data:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.z = 100
#
# d1 = Data(1, 2)
# d2 = Data(2, 3)
#
# print(d1.__dict__)      #{x:1, y:2, z:100}
# print(d2.__dict__)      #{x:2, y:3, z:100}

# -------------------------------------------------
# class Point:
#
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z

# p1 = Point(1, 2, 3)
# print(p1.__dict__)      #{'x': 1, 'y': 2, 'z': 3}

# p2 = Point()
# print(p2.__dict__)      #{'x': 0, 'y': 0, 'z': 0}
# #
# p3 = Point(1, 2)
# print(p3.__dict__)      #{'x': 1, 'y': 2, 'z': 0}
# #
# p4 = Point(x=10, y=20, z=30)
# print(p4.__dict__)      #{'x': 10, 'y': 20, 'z': 30}
# #
# p5 = Point(z=100)
# print(p5.__dict__)      #{'x': 0, 'y': 0, 'z': 100}

# -----------------------------------------------
# class Sample:
#
#     def __init__(self, a):
#         self.a = a
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def display(self):
#         print(f'The value = {self.a}')
#         print(f'The value = {self.x}, {self.y} ')

# s1 = Sample(9,2)
# s1.display()    #TypeError: Sample.__init__() missing 1 required positional argument: 'y'

'''If we are having two __init__, second init will be considered'''

# s2 = Sample(2, 3)
# s2.display()    #AttributeError: 'Sample' object has no attribute 'a'

# -----------------------------------------------------
# class Sample:
#
#     def __init__(self, a):
#         self.a = a
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def display(self):
#         print(f'The value = {self.x}, {self.y}')
#
# s1 = Sample(2, 3)
# s1.display()        #The value = 2, 3

# ------------------------------------------------------------
# class Sample:
#
#     def spam(self):
#         print('In spam1 executing')
#
#     def spam(self):
#         print('In spam2 executing')
#
# s1 = Sample()
# s1.spam()       #In spam2 executing

# ---------------------------------------------
# class Demo:
#
#     def apple(self):
#         print('Demo class apple method executing')
#
#     def google(self):
#         print('Demo class google method executing')
        # self.apple()
        # Demo.apple(self)

# d1 = Demo()
# d1.apple()
# print('--------------------------------------------')
# d1.google()

# -------------------------------------------------
# a = [10, 20]       #[20, 10]   ##a[0]=10, a[1]=20
# b = [1, 2]
#
# class Rearrange:
#
#     def swap(self):
#         temp = a[0]     #temp=10
#         a[0] = a[1]     #a[0]=20
#         a[1] = temp
#         print(a)
#
#     def reset(self):
#         a[0] = 0
#         a[1] = 0
#         print(a)

# obj1 = Rearrange()
# obj2 = Rearrange()
#
# # obj1.swap()
# obj2.reset()

# ----------------------------------
# class Rearrange:
#
#     def swap(self, a):
#         temp = a[0]     #temp=10
#         a[0] = a[1]     #a[0]=20
#         a[1] = temp
#         print(a)
#
#     def reset(self, b):
#         b[0] = 0
#         b[1] = 0
#         print(b)
#
# obj1 = Rearrange()
# obj2 = Rearrange()
#
# obj1.swap(['hello', 'hai'])
# obj2.reset(['hello', 'hai'])

# ----------------------------------
# class Rearrange:
#
#     a = ['hai', 'hello']
#
#     def swap(self):
#         temp = self.a[0]            #temp=10
#         self.a[0] = self.a[1]       #a[0]=20
#         self.a[1] = temp
#         print(self.a)
#
#     def reset(self):
#         self.a[0] = 0
#         self.a[1] = 0
#         print(self.a)
#
# obj1 = Rearrange()
# obj2 = Rearrange()
#
# obj1.swap()
# obj2.reset()

# ---------------------------------------------
# class Rearrange:
#
#     def __init__(self, a):
#         self.a = a
#
#     def swap(self):
#         temp = self.a[0]            #temp=10
#         self.a[0] = self.a[1]       #a[0]=20
#         self.a[1] = temp
#         print(self.a)
#
#     def reset(self):
#         self.a[0] = 0
#         self.a[1] = 0
#         print(self.a)
#
# obj1 = Rearrange(['a', 'b'])
# obj2 = Rearrange([10, 20])
# #
# obj1.swap()
# obj1.reset()
# obj2.swap()
# obj2.reset()

# --------------------------------------------

# class Sample:
#
#     x = 100
#
#     def display(self):
#         print(f'The value of x is {self.x}')
#
# s1 = Sample()
# s2 = Sample()

# accessing class variable using objects
# print(s1.x)
# print(s2.x)

## accessing class variable through classname
# print(Sample.x)

## calling the methods through objects
# s1.display()
# s2.display()
#
# ## calling the method using classname
# Sample.display(s1)
# Sample.display(s2)


# ----------------------------------
# class Sample:
#
#     x = 100
#
#     def display(self):
#         print(f'The value of x is {self.x}')
#
# s1 = Sample()
# s2 = Sample()

# print(s1.x)     #100
# s1.x = 'hai'
# print(s1.x)     #'hai'
# print(s2.x)     #100
# print(Sample.x)     #100
#
# Sample.x = 'hello'
# print(Sample.x)     #hello
# print(s1.x)     #hello
# print(s2.x)     #hello
# #
# ## The changes made in one object will  not reflect in other object or in class

# ----------------------------------------------
# class Employee:
#
#     company_name = 'dell EMC'
#
#     def __init__(self, name, empid):
#         self.name = name
#         self.empid = empid
#
#     def display(self):
#         print(f'Hello {self.name}, Welcome to {self.company_name}. Your EmpID is {self.empid}')
#
#     def email(self):
#         print(f'{self.name}_{self.empid}@{self.company_name}.com')
#
# emp1 = Employee('Mithilesh', '001')
# emp2 = Employee('Keerthy', '002')
# emp3 = Employee('Vinayak', '003')
# emp4 = Employee('Sathya', '004')
#
# emp1.display()
# emp1.email()
# # #
# print('---------------------------')
# emp2.display()
# emp2.email()
# #
# print('----------------------------')
# emp3.display()
# emp3.email()
# #
# print('----------------------------')
# emp4.display()
# emp4.email()

# --------------------------------------

# class Sample:
#
#     a = 100
#
#     def display(self):
#         self.a = 1000
#         print(f'the value is {self.a}')
#
#
# s1 = Sample()
# print(s1.a)
# print(Sample.a)
#
# s1.display()
# Sample.display(s1)


# ----------------------
# class Sample:
#
#     a = 100
#
#     def display(self, b):
#         if b > self.a:
#             self.a = 1000
#
#         print(f'The value is {self.a}')
#
# s1 = Sample()
#
# s1.display(50)


# -----------------------------------



'''class method'''

# class ChiefMinister:
#
#     current_cm = 'Siddaramaiah'
#
#     def display(self):
#         print(f'The current CM is {self.current_cm}')
#
#     def replacement(self, votes):
#         if votes > 100:
#             self.current_cm = 'DK Shivakumar'
#
# congress = ChiefMinister()
# opposition = ChiefMinister()
# common_people = ChiefMinister()

# congress.display()          #The current CM is Siddaramaiah
# opposition.display()        #The current CM is Siddaramaiah
# common_people.display()     #The current CM is Siddaramaiah
# # #
# congress.replacement(70)
# congress.display()          #The current CM is Siddaramaiah
# opposition.display()        #The current CM is Siddaramaiah
# common_people.display()     #The current CM is Siddaramaiah
#
# congress.replacement(110)
# congress.display()
# opposition.display()
# common_people.display()

# -------
# class ChiefMinister:
#
#     current_cm = 'Siddaramaiah'
#
#     def display(self):
#         print(f'The current CM is {self.current_cm}')
#
#     @classmethod
#     def replacement(cls, votes):
#         if votes > 100:
#             cls.current_cm = 'DK Shivakumar'
#
# congress = ChiefMinister()
# opposition = ChiefMinister()
# common_people = ChiefMinister()
#
# congress.display()          #The current CM is Siddaramaiah
# opposition.display()        #The current CM is Siddaramaiah
# common_people.display()     #The current CM is Siddaramaiah
#
# congress.replacement(70)
# congress.display()          #The current CM is Siddaramaiah
# opposition.display()        #The current CM is Siddaramaiah
# common_people.display()     #The current CM is Siddaramaiah
#
# opposition.replacement(110)
# congress.display()          #The current CM is DK Shivakumar
# opposition.display()        #The current CM is DK Shivakumar
# common_people.display()     #The current CM is DK Shivakumar

# --------------
## Static method

# class Sample:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     @staticmethod
#     def add(x, y):
#         print(x + y)
#
# s1 = Sample(1, 2)
# s1.add(7, 9)
# Sample.add(1, 2)

## ------------------------------------
# def func():
#     print('in func')
#
# func()
# print(dir(func))        #__call__

# -------------------
'''making objects callable'''

# class Sample:
#
#     def __init__(self, value):
#         self.value = value
#
#     def display(self):
#         print(f'The value is {self.value}')
#
# s1 = Sample(100)
# s1()                    #TypeError: 'Sample' object is not callable
# print(dir(s1))
# print(callable(s1))       #False


'''Objects are not callable. So to call the objects we have to define __call__'''
# -----------------------
# class Sample:
#     def __init__(self, value):
#         self.value = value
#
#     def __call__(self):
#         print('In call method executing')
#
#     def display(self):
#         print(f'The value is {self.value}')
#
# s1 = Sample(100)
#
# s1.display()    #The value is 100
# s1()            #In call method executing
# s1.__call__()   ##In call method executing
# print(callable(s1))     #True

# -------------------------------------------------------------------------------
'''create a class that prints 'hello world' on calling its object'''

# class Greet:
#
#     def __call__(self):
#         print('hello world')
#
# greet_obj1 = Greet()
# greet_obj1()

# -----------------------------------------------
'''create a class which returns the list squares when the object is called'''

# class List_:
#
#     def __init__(self, iterable):
#         self.iterable = iterable
#
#     def __call__(self):
#         for num in self.iterable:
#             print(num ** 2)
#
#
# l1 = List_([1, 2, 3, 4])
# l1()

### Alternate solution
# class List_:
#
#     def __call__(self, iterable):
#         for num in iterable:
#             print(num ** 2)
#
#
# l1 = List_()
# l1([1, 2, 3, 4])

# ------------------------------------------------
'''create a class that checks whether the user input num is even or odd when it is called'''

# class EvenOdd:
#
#     def __init__(self, num):
#         self.num = num
#
#     def __call__(self, *args, **kwargs):            # *args, **kwargs----for dict format outcomes
#         if self.num % 2 == 0:
#             print('even')
#         else:
#             print('odd')
#
# e1 = EvenOdd(3)
# e1()
# e2 = EvenOdd(8)
# e2()

# ----------------------------------------
# def outer(func):
#     def wrapper(*args, **kwargs):
#         print('hai')
#         func(*args, **kwargs)
#     return wrapper
#
# @outer      #spam = outer(spam)
# def spam():
#     print('In spam')
#
# spam()

# ----------------
'''class decorators 
* Among class and objects, only class is callable.
* In order to make an object callable,there must be __call__() present in the respective class of that object. 
* callable(obj) - It is a function used to check if any object is callable or not.'''


# structure of class decorator
# class ClassName:
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, *kwargs):
#         pre task
#         self.func(*args, **kwargs)
#         post task
#
# OR
#
# class ClassName:
#
#     def __call__(self, func):
#         def wrapper(*args, *kwargs):
#             pre task
#             func(*args, **kwargs)
#             post task
#         return wrapper
#
# @ClassName()
# def function():
#     pass
'''

write a class deco to print 'hai' before execution of main func....'''

# class Sample:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print('hai')
#         self.func()
#
# @Sample                  # spam =  Sample(spam)
# def spam():
#     print('In spam')
# spam()

## Alternate solution

# class Sample:
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print('hai')
#             func(*args, **kwargs)
#         return wrapper
#
# @Sample()     # spam =  Sample(spam)   # only when we use decorator function(wrapper and return) under the class,
# def spam():                           # decorate the function with @classname()
#     print('In spam')
#
# spam()
# ---------------------
'''write a class deco to execute the main func for 3 times'''

# class Sample:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         for u_i1 in range(5):
#             self.func(*args, **kwargs)
#
# @Sample         #add = Sample(add)
# def add(a, b):
#     print(a + b)
# add(1, 2)

# -------------------------------------------

# class Sample:
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         for _ in range(5):
#             self.func(*args, **kwargs)
#
# @Sample         #add = Sample(add)
# def add(a, b):
#     print(a + b)
#
# add(1, 2)
#
# @Sample
# def sub(a, b):
#     print(a - b)
#
# sub(3, 2)

# ---------------------------------
'''write a class deco to execute one func for 3 times and other for 5 times '''

# class Sample:
#     def __init__(self, n):
#         self.n = n
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             for _ in range(self.n):
#                 func(*args, **kwargs)
#         return wrapper
#
# @Sample(3)         #add = Sample(add)
# def add(a, b):
#     print(a + b)
#
# add(1, 2)
#
# @Sample(1)
# def sub(a, b):
#     print(a - b)
# #
# sub(3, 2)

# -----------------------------------------
'''delay the execution of main func by 3 seconds using class deco'''

# import time
# class Delay:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         time.sleep(3)
#         self.func()
#
# @Delay                    #spam = Delay(spam)
# def spam():
#     print('In spam')
# spam()
#
# @Delay
# def display():
#     print('In display')
#
# display()

# -------------------------------------
'''delay the execution of spam by 5 seconds and display by 3 seconds using class decorators'''

# import time
# class Delay:
#
#     def __init__(self, n):
#         self.n = n
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             time.sleep(self.n)
#             func(*args, **kwargs)
#         return wrapper
#
# @Delay(5)               #spam = Delay(spam)
# def spam():
#     print('In spam')
#
# spam()
#
# @Delay(3)
# def display():
#     print('In display')
#
# display()

# -----------------------------------------------------------
# class ShoppingCart:
#     # class variable
#     # products inventory
#     products = {'iPhone': 5, 'iMac': 3, 'iWatch': 2, 'iPad': 4}
#     # prices are same for all the customer
#     prices = {"iPhone": 900, "iMac": 2500, 'iWatch': 3500, 'iPad': 3500}
#
#     def __init__(self):
#         self.cart = []
#
#     def add_item(self, name, quantity):
#         # validating the name of the product
#         if name not in ShoppingCart.products:
#             raise Exception(f"Cannot add product {name}")
#         # validating the quantity that the user is byuing
#         if quantity > ShoppingCart.products[name]:
#             raise Exception(f"Product out of stock")
#         # if everything is fine, add the item to the cart
#         d = {"name": name, "quantity": quantity, "price": ShoppingCart.prices[name]}
#         self.cart.append(d)
#         ShoppingCart.products[name] = ShoppingCart.products[name] - quantity
#
#     def remove_item(self, name):
#         for item in self.cart:
#             if item['name'] == name:
#                 if item['quantity'] == 1:
#                     self.cart.remove(item)
#                 else:
#                     item['quantity'] = item['quantity'] - 1
#
#     def total_cost(self):
#         prices = [item['quantity'] * item['price'] for item in self.cart]
#         total = 0
#         for price in prices:
#             total = total + price
#         return total
#
#
# c1 = ShoppingCart()
# c2 = ShoppingCart()


# ------------------------------------

# class Sample:
#
#     a = 10
#
#     def __init__(self, a):
#         self.a = a
#
#     def display(self):
#         print(self.a)
#
#
# s = Sample('hai')
# # print(s.a)
#
# print(Sample.a)



# ------

# links = ['www.google.com','www.gmail.com','www.youtube.com','www.wikipedia.com']
#
# for ele in links:
#     print(ele.removeprefix('www.'))
#     print('--------')
#     print(ele.removesuffix('.com'))
#     print('--------')

    # print(ele.lstrip('www.'))

# ----------------------------------------

# num=range(1,100)
#
# def prime(num):
#
#     for x in range( 2, num ):
#         if ( num % x ) ==0:
#             return False
#         return True
#
# print(list(filter(prime, num)))
