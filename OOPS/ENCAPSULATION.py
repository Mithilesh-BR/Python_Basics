'''ENCAPSULATION

--> Binding of data(attributes/variables) and methods(functions) into a single unit, called class
and to hide or restrict the sensitive data from the user.
--> We can restrict the data and methods access globally by making it private and protected.
--> data hiding + controlled access = Encapsulation

BENEFITS::

Controlled Access: Encapsulation allows controlled access to the internal state of an object,
protecting the data from unintended interference.

Data Hiding: It hides the internal workings of a class, making the implementation details invisible to outside code
and reducing the risk of accidental data modification.

Improved Maintenance: Changes to the internal implementation of a class do not affect code that uses the class,
as long as the public interface remains unchanged.

Enhanced Flexibility: Encapsulation promotes modular design, making it easier to modify or extend
functionality without impacting other parts of the program.
'''
# ------------------------------------------------------
'''PROTECTED MEMBER/VARIABLE

The protected variable can be accessed out of the class as well as in the derived class.
By prefixing the name of the member by a single underscore “_”

If the variable is protected, we can access through function under the same class
through class object we can access outside of the class as well under the same class object

If we dont give any thing then it will be public and can access inside and outside of the class
'''
# class person:
#     def __init__(self, name):
#         self.__name = name
#
# p = person('Mithilesh')
# print(p.__name)
# print(p._person__name)                            #name mangling
class person
# ---------------------------------------------------
# Creating a base class

# class Base:
# 	def __init__(self):
# 	    self._a = 2

# class Derived(Base):
# 	def __init__(self):
# 		Base.__init__(self)
# 		print("Calling protected member of base class: ", self._a)

		# self._a = 'a'
		# print("Calling modified protected member outside class: ", self._a)

# obj1 = Derived()
# obj2 = Base()
                                                                                    # # # # Calling protected member
                                                                                    # # # # Can be accessed but should not be done due to convention
# print("Accessing protected member of obj1: ", obj1._a)
                                                                                    # Accessing the protected variable outside
# print("Accessing protected member of obj2: ", obj2._a)

# ------------------------------------------------------------------

'''PRIVATE MEMBER/VARIABLE

The class members declared private should neither be accessed outside the class nor by any base class.
In Python, there is no existence of Private instance variables that cannot be accessed except inside a class.
To define a private member prefix the member name with double underscore “__”.

If we want to make our variable private, we can access under the same class through function.
Now the function is public and variable is private
If variable is private, we can access under the same class through public function
If function is private, can access variable under the same class and can't access class object outside of class
If we make it private we can't access outside of the class

If we dont give any thing then it will be public and can access inside and outside of the class
'''

# Creating a Base class

# class Base:
# 	def __init__(self):
# 		self.a = "Geeks for Geeks"
# 		self.__c = "india"

# class Derived(Base):
# 	def __init__(self):
# 		Base.__init__(self)
# 		print("Calling private member of base class: ")
# 		print(self.__c)

# Driver code
# obj1 = Base()
# print(obj1.a)
# print(obj1.__c)

# obj2 = Derived()
# print(obj2.__c)
# Uncommenting print(obj1.__c) will raise an AttributeError

# Uncommenting obj2 = Derived() will also raise an AttributeError as private member of base class
# is called inside derived class

# ---------------------------------------------------
# -----------------------------------------------------

# class Bank:
#
#     bank_name = 'SBI'
#
#     def __init__(self, name, acc_num, balance):
#         self.name = name
#         self.acc_num = acc_num
#         self.balance = balance
#
#     def display(self):
#         print(f'The acc holder {self.name} has {self.balance} in his acc. Acc num is {self.acc_num}' )
#
# b1 = Bank('Rocky', 'sbi1100', 10000)
# b2 = Bank('Garuda', 'sbi1101', 20000)
# b3 = Bank('Adheera', 'sbbi1111', 15000)
#
# b1.display()
# b2.display()
# b3.display()

#---------------------------------------------
# class Bank:
#
#     bank_name = 'SBI'
#
#     def __init__(self, name, acc_num):
#         self.name = name
#         self._acc_num = acc_num
#
#     def display(self):
#         print(f'The acc holder {self.name} Acc num is {self._acc_num}' )
#
#
# class ATM(Bank):
#
#     _acc_num = 'sbi0000'
#
#     def spam(self):
#         print(f'The acc num is {self._acc_num}')
#
# atm_obj1 = ATM('Rocky', 'sbi1100')
# atm_obj1.display()
# atm_obj1.spam()                         # we can't modify protected variable value even in the other class


#------------------------------------------------------------
# class A:
#
#     a = 10
#     _b = 'hai'
#
# class B(A):
#
#     def display(self):
#         print(f'The values are {self.a} and {self._b}')
#
# b = B()
# b.display()

# print(b.a)
# print(b._b)
#
# print(b.__dict__)       #{}
# print(A.__dict__)
# #
# b._b = 'python'
# print(b._b)              # we can modify protected variable value outside the class, after creating the object
# # #
# print(b.__dict__)           #{'_b': 'python'}
# print(A.__dict__)

#---------------------------
# class A:
#
#     a = 10
#     _b = 'hai'
#
#     def _display(self):
#         print(f'The values are {self.a} and {self._b}')
#
# class B(A):
#     def _spam(self):
#         if len(self._b) < 5:
#             self._b = 'bengaluru'
#
# b = B()
# b._display()
# b._spam()
# b._display()

#-----------------------------------------------------------
# class A:
#
#     __a = 100

# a = A()
# print(a.__a)        #AttributeError
# print(A.__a)        #AttributeError

# class B(A):
#
#     def display(self):
#         print(f'The value of a is {self.__a}')
#
# b = B()
# b.display()       #AttributeError

#------------------------------
# class A:
#
#     __a = 100
#
# a = A()

# print(a.__a)                ## AttributeError
# print(A.__a)                ## AttributeError
# print(A.__dict__)
# print(a.__dict__)         #{}
# print(__a.__dict__)         # NameError

#-----------------------------------------

# class A:
#
#     __a = 1000
#
#     def display(self):
#         print(f'The value of a is {self.__a}')
#
# a = A()
# a.display()                 # Private variable can be printed in the same class using method

#-------------------------------------
# class A:
#     __a = 1000
#
#     def display(self):
#         print(f'The value of a is {self.__a}')
#
#
# class B(A):
#
#     def sample(self):
#         print(f'The value of a is {self.__a}')
#
# b = B()
# # # b.sample()                  #AttributeError
# b.display()

#-----------------------------------------

'''When a variable is "private", it means that the value of the variable can only be accessed from 
inside the class the variable is declared in. You cannot directly access or change the value of the 
variable outside the class'''

# class Bank:
#     emi = 10
#     _interest = 9
#     __principal = 100000
#
#     def spam(self):
#         print(f'The principal amount is {self.__principal}')
#
# class Account(Bank):
#     emi = 20
#     _interest = 11
#     __principal = 200000
#
#     def display(self):
#         print(f'The principal amount is {self.__principal}')
#
# a = Account()
# print(a.emi)
# print(a._interest)
# a.display()                 # updated private variable can be printed in child class method
# a.spam()


#----------------------------------------------------
# class A:
#
#     __salary = 20000
#
#     def spam(self, age):
#         if age > 40:
#             self.__salary = 30000
#             print(self.__salary)
#
#     def display(self):
#         print(f'The salary is {self.__salary}')
#
# a = A()
# a.display()
# a.spam(30)
# a.display()

#----------------------------------