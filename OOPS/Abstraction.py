'''
Definition: The concept of hiding complex implementation details and showing only the essential features of an object.

Implementation: Achieved through abstract classes and methods, interfaces, and high-level class design.

--> First we have to import ABC(Abstract Based Class) & abstract method
--> We give ABC as parameter while defining class
--> If we abstract any method, we have to decorate with abstract method ,
So whatever the abstract methods defined in the parent class, that should be inherited in the child class
--> We can't create object for this class : If you try to create an object,
it will throw an error saying that you are trying to create an
instantiation for the abstract base class '''

# from abc import ABC, abstractmethod
#
# class Bank(ABC):
#
#     @abstractmethod
#     def withdraw(self, amt):
#         print(f'Withdrawn {amt}')
#
#     @abstractmethod
#     def deposit(self, amount):
#         print(f'Deposited {amount}')
#
#     def sample(self):
#         print('Sample')
#
# class SBI(Bank):

# def withdraw(self, amt):
#     print(f'Withdrawn {amt}')
#
# def deposit(self, amount):
#     print(f'Deposited {amount}')
#
# def spam(self):
#     print('spam')
# # #
# b = Bank()
# b.deposit(1000)     ## Error,. Cant create object for Abstract class
#
# s = SBI()
# s.deposit(1000)
# s.withdraw(100)
# s.spam()
# s.sample()

# --------------------------------------------------------------------------

'''   https://www.geeksforgeeks.org/abstract-classes-in-python/

* This code defines an abstract base class called “Polygon” using the ABC (Abstract Base Class) module in Python. 
* The “Polygon” class has an abstract method called “no of sides” that needs to be implemented by its subclasses.
* There are four subclasses of “Polygon” defined: “Triangle,” “Pentagon,” “Hexagon,” and “Quadrilateral.”
* Each of these subclasses overrides the “no of sides” method and provides its own implementation by printing
 the number of sides it has.
* In the driver code, instances of each subclass are created, and the “no of sides” method is called on each
 instance to display the number of sides specific to that shape.'''

# ---------------------------------------

# from abc import ABC, abstractmethod
# class Polygon(ABC):
#     @abstractmethod
#     def noofsides(self):
#         pass
# #
# class Triangle(Polygon):
#     def noofsides(self):                    # overriding abstract method
#         print("I have 3 sides")
# #
from abc import BAC, abstractmethod
# class Pentagon(Polygon):
#     def noofsides(self):                    # overriding abstract method
#         print("I have 5 sides")
# #
# class Hexagon(Polygon):
#     def noofsides(self):                    # overriding abstract method
#         print("I have 6 sides")
#
# class Quadrilateral(Polygon):
#     def noofsides(self):                    # overriding abstract method
#         print("I have 4 sides")

# # Driver code
# R = Triangle()
# R.noofsides()                       #I have 3 sides
#
# K = Quadrilateral()
# K.noofsides()                       #I have 4 sides
#
# R = Pentagon()
# R.noofsides()                       #I have 5 sides
#
# K = Hexagon()
# K.noofsides()                       #I have 6 sides

# ---------------------------------------------------------------------

'''Here, This code defines an abstract base class called “Animal” using the ABC (Abstract Base Class)
module in Python. The “Animal” class has a non-abstract method called “move” that does not have any 
implementation. There are four subclasses of “Animal” defined: “Human,” “Snake,” “Dog,” and “Lion.” 
Each of these subclasses overrides the “move” method and provides its own implementation by printing
a specific movement characteristic.
'''

# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     def move(self):
#         pass
#
# class Human(Animal):
#     def move(self):
#         print("I can walk and run")
#
# class Snake(Animal):
#     def move(self):
#         print("I can crawl")
#
# class Dog(Animal):
#     def move(self):
#         print("I can bark")
#
# class Lion(Animal):
#     def move(self):
#         print("I can roar")

# Driver code
# R = Human()
# R.move()                #I can walk and run
# # #
# K = Snake()
# K.move()                #I can crawl
# #
# R = Dog()
# R.move()                #I can bark
# #
# K = Lion()
# K.move()                #I can roar

# ----------------------------------------------

'''Implementation of Abstract through Subclass

By subclassing directly from the base, we can avoid the need to register the class explicitly.
In this case, the Python class management is used to recognize Plugin implementation as implementing
the abstract PluginBase.

* A side-effect of using direct subclassing is, it is possible to find all the implementations of your
plugin by asking the base class for the list of known classes derived from it.
'''

import abc

# class parent:
#     def geeks(self):
#         pass
#
# class child(parent):
#     def geeks(self):
#         print("child class")
#
# # Driver code
#
# print( issubclass(child, parent))               #True
# print( isinstance(child(), parent))             #True


# -------------------------------------------------

'''Concrete Methods in Abstract Base Classes

Concrete classes contain only concrete (normal) methods whereas abstract classes may contain both 
concrete methods and abstract methods.

The concrete class provides an implementation of abstract methods, the abstract base class can also
provide an implementation by invoking the methods via super(). Let look over the example to invoke
the method using super():

* In the above program, we can invoke the methods in abstract classes by using super(). 
'''

# from abc import ABC
#
# class R(ABC):
#     def rk(self):
#         print("Abstract Base Class")
#
# class K(R):
#     def rk(self):
#         super().rk()
#         print("subclass ")
#
# # Driver code
# r = K()                     #Abstract Base Class
# r.rk()                      #subclass

# ---------------------------------------------------------

'''Abstract Properties in Python
Abstract classes include attributes in addition to methods, you can require the attributes in 
concrete classes by defining them with @abstractproperty.

* In the above example, the Base class cannot be instantiated because it has only an abstract version
of the property-getter method.
'''

# import abc
# from abc import ABC,  abstractmethod
#
# class parent(ABC):
#     @abc.abstractproperty
#     def geeks(self):
#         return "parent class"
#
# class child(parent):
#
#     @property
#     def geeks(self):
#         return "child class"
# #
# try:
#     r = parent()
#     print(r.geeks)
# except Exception as error:
#     print(error)
#
# r = child()
# print(r.geeks)     #Can't instantiate abstract class parent with abstract methods geeks child class

# --------------------------------------------

'''Abstract Class Instantiation
Abstract classes are incomplete because they have methods that have nobody. 
If Python allows creating an object for abstract classes then using that object if anyone calls 
the abstract method, but there is no actual implementation to invoke.

So, we use an abstract class as a template and according to the need, we extend it and build on it 
before we can use it. Due to the fact, an abstract class is not a concrete class, it cannot be 
instantiated. When we create an object for the abstract class it raises an error. '''

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print("I can walk and run")


class Snake(Animal):
    def move(self):
        print("I can crawl")


#
class Dog(Animal):
    def move(self):
        print("I can bark")


#
class Lion(Animal):
    def move(self):
        print("I can roar")


#
c = Animal()

'''Traceback (most recent call last):
  File "/home/ffe4267d930f204512b7f501bb1bc489.py", line 19, in 
    c=Animal()
TypeError: Can't instantiate abstract class Animal with abstract methods move '''

# ----------END-----------------#


# # Import required modules
# from abc import ABC, abstractmethod
#
#
# # Create Abstract base class
# class Car(ABC):
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

    # Create abstract method
#     @abstractmethod
#     def printDetails(self):
#         pass
#
#     # Create concrete method
#     def accelerate(self):
#         print("Speed up ...")
#
#     def break_applied(self):
#         print("Car stopped")
#
#
# # Create a child class
# class Hatchback(Car):
#     def printDetails(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Year:", self.year)
#
#     def sunroof(self):
#         print("Not having this feature")


# Create a child class
# class Suv(Car):
#     def printDetails(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Year:", self.year)
#
#     def sunroof(self):
#         print("Available")
#
#
# # Create an instance of the Hatchback class
# car1 = Hatchback("Maruti", "Alto", "2022")
#
# # Call methods
# car1.printDetails()
# car1.accelerate()
# car1.sunroof()

# ______________________________________________________________________________






