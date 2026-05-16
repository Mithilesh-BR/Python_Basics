# class A:
#
#     def feature1(self):
#         print('feature1 is executing')
#
#     def feature2(self):
#         print('feature2 is executing')
#
# class B(A):
#
#     def feature3(self):
#         print('feature3 is executing')
#
#     def feature4(self):
#         print('feature4 is executing')
#
# obj = B()
# obj.feature1()
#
# obj.feature2()
# obj.feature3()
# obj.feature4()


'''Since we are inheriting A to B, object of class B can access the methods inside class A'''
#-----------------------------
'''
Four types of inheritance
1. Single level inheritance :  Single Parent, single child
2. Multilevel inheritance
3. Multiple inheritance   :    One child, multiple parent classes
4. hierarchial inheritance   :   One parent, multiple child
'''

#-----------------------------------------------
'''Single level : Single Parent, single child'''

# class Parent:
#     a = 100
#
#     def display(self):
#         print(f'The value of a is {self.a}')
#
# class Child(Parent):
#     b = 200
#
#     def sample(self):
#         print(f'The value of b is {self.b}')
#
# c = Child()
# c.sample()
# c.display()

#-----------------------------
'''Multilevel Inheritance'''

# class A:
#     x = 100
#
#     def display(self):
#         print(f'The value of a is {self.x}')
#
# class B(A):
#     y = 100
#
#     def sample(self):
#         print(f'The value of b is {self.y}')
#
# class C(B):
#     z = 100
#
#     def spam(self):
#         print(f'The value of c is {self.z}')
#
# obj = C()
# obj.spam()
# obj.sample()
# obj.display()

#------------------------------------
'''Multiple inheritance : One child, multiple parent classes'''

# class A:
#     x = 10
#     def display(self):
#         print(f'The value of x is {self.x}')
#
# class B:
#     y = 50
#     def sample(self):
#         print(f'The value of y is {self.y}')
#
# class C(A,B):
#     z = 100
#     def spam(self):
#         print(f'The value of z is {self.z}')
#
# obj = C()
# obj.spam()
# obj.sample()
# obj.display()

#------------------------------------
'''Hierarchial Inheritance : One parent, multiple child'''

# class A:
#     pass
#
# class B(A):
#     pass
#
# class C(A):
#     pass
#
# class D(A):
#     pass

# ---------------------------

# class Apple:
#     def tomato(self):
#         print('red color')
#
# class Pineapple(Apple):
#     def carrot(self):
#         print('orange color')
#
# class Mango(Apple):
#     def onion(self):
#         print('white color')
#
# obj1 = Mango()
# obj1.tomato()
#
# obj2 = Pineapple()
# obj2.carrot()
# obj2.tomato()

#-----------------------------------------------
# class Parent:
#
#     a = 100
#
# class Child(Parent):
#
#     a = 'hello world'
#
#     def display(self):
#         print(f'The value of a is {self.a}')
#
# obj1 = Child()
# obj1.display()              #The value of a is hello world

#-----------
# class A:
#     x = 'hello universe'
#
# class B:
#     x = 'hello world'
#
# class C(A,B):
#
#     x = 'python'
#
#     def display(self):
#         print(self.x)
#
# obj = C()
# obj.display()

#-----------------------------------------------
# class Parent:
#
#     def __init__(self, value):
#         self.value = value
#
#     def apple(self):
#         print(f'parent class apple method executing')
#
# class Child(Parent):
#
#     def apple(self):                                      ##overridden method
#         print(f'Child class apple method executing')
#
#     def google(self):                                     ## independent
#         print(f'Child class google method executing')
#
# c = Child('hai')
# c.google()                                                #Child class google method executing
# c.apple()                                                 #Child class apple method executing

#-----------------------------------------------
# class Sample:
#
#     def apple(self):
#         print('Sample class apple method executing')
#
#     def apple(self):
#         print('Sample class google method executing')
#
# s = Sample()
# s.apple()       #Sample class google method executing


'''If we are having same attributes inside the class, second defined attribute will execute'''

#-------------------------------------

'''method chaining'''

## To chain the overridden methods

# class Sample:
#
#     def apple(self):
#         print('Sample class apple method executing')
#
#     def google(self):
#         print('Sample class google method executing')
#
# class Spam(Sample):
#
#     def yahoo(self):                                    ##independent method
#         print('Spam class yahoo method executing')
#
#     def google(self):                                   ## Overridden method
#         print('Spam class google method executing')
#         Sample.google(self)                              ## Sample class google method will execute
#
# obj = Spam()
# obj.google()            ##Spam class google method executing, Sample class google method will execute


#-------------
# class Sample:
#
#     def apple(self):
#         print('Sample class apple method executing')
#
#     def google(self):
#         print('Sample class google method executing')
#
# class Name:
#
#     def google(self):
#         print('Name class google method executing')
#
# class Spam(Sample,Name):
#
#     def yahoo(self):                                        ##independent method
#         print('Spam class yahoo method executing')
#
#     def google(self):                                       ## Overridden method
#         print('Spam class google method executing')
#         super().google()                                    # Sample.google(self)
# #
# obj = Spam()
# obj.google()     ##Spam class google method executing, Sample class google method will execute

'''super():function used to give access to the methods of parent class, returns a temporary object of a 
parent class when used'''

#------------
# class A:
#
#     def log(self, x):
#         print('class A log method executing')
#         print(f'The value of x is {x}')
#
# class B(A):
#     def log(self,x):
#         print('class B log method executing')
#         print(x)
#         super().log(50)
#         # A.log(self,100)
#
# obj = B()
# obj.log(25)     #class B log method executing, class A log method executing, The value of x is 100

#---------------------------------------
'''constructor chaining'''
# class Demo:

#     def __init__(self, pattern):
#         self.pattern = pattern

#     def display(self):
#         print(f'Demo class pattern {self.pattern}')

# class Spam(Demo):

#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         super().__init__(a)   ## Here one value for __init__ because, Demo class init takes one argument

#     def sample(self):
#         print(f'The values are {self.a} and {self.b}')

# s = Spam(10, 20)
# s.sample()
# s.display()

#------------------------------------------------
# class Demo:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def display(self):
#         print(f'Demo class values are {self.a} and {self.b}')
#
# class Spam(Demo):
#
#     def __init__(self, c, value1, value2):
#         self.c = c
#         self.value1 = value1
#         self.value2 = value2
#         super().__init__(value1, value2)  ## In this case, Demo class self.a=value1, self.b=value2
#
#     def sample(self):
#         print(f'The values are {self.c} and {self.value1}')
#
# s = Spam(10, 20, 30)
# s.sample()
# s.display()

#---------------------------------------
## Constructor chaining in multiple inheritance

# class Spam1:
#
#     def __init__(self, a):
#         self.a = a
#
#     def apple(self):
#         print(f'The value of a is {self.a}')
#
# class Spam2:
#
#     def __init__(self, c, d):
#         self.c = c
#         self.d = d
#
#     def yahoo(self):
#         print(f'The values are {self.c} and {self.d}')
#
# class Display(Spam2, Spam1):                #Here Spam2 is the super/parent class
# #
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#         # super().__init__(x)             ## Spam1 is not super class, so we get error
#         Spam1.__init__(self, x)
#         super().__init__(y,z)
#         # Spam2.__init__(self, y, z)
#
# g = Display(1, 2, 3)
# g.apple()
# g.yahoo()

#-----------------------------------------------------

# class Spam1:
#
#     def __init__(self, a):
#         self.a = a
#
#     def apple(self):
#         print(f'The value of a is {self.a}')
#
# class Spam2:
#
#     def __init__(self, c, d):
#         self.c = c
#         self.d = d
#
#     def yahoo(self):
#         print(f'The values are {self.c} and {self.d}')
#
# class Example(Spam2, Spam1):
#
#     def __init__(self, p , q, r):
#         self.p = p
#         self.q = q
#         self.r = r
#         super().__init__(p, q)
#
# class Spam3(Spam2, Spam1):
#     def __init__(self, a, b, c):
#         Spam1.__init__(self, a)
#         Spam2.__init__(self, a, c)
#
# # e = Example(10, 20, 30)
# e = Spam3(10, 20, 30)
# e.yahoo()

#-----------------------------------------------
## Constructor and method chaining in multilevel inheritance

# class A:
#     def demo(self):
#         print('class A demo method executing')
#
# class B(A):
#     def demo(self):
#         print('class B demo method executing')
#         super().demo()
#
# class C(B):
#     def demo(self):
#         print('class C demo method executing')
#         super().demo()
#
# x = C()
# x.demo()

#-----------------------------------------
# class A:
#
#     def __init__(self, name):
#         self.name = name
#
# class B(A):
#     def __init__(self, num1, num2, name):
#         self.num1 = num1
#         self.num2 = num2
#         super().__init__(name)
#
# class C(B):
#     def __init__(self, c1, c2, c3):
#         super().__init__(c1, c2, c3)
#
# obj = C(10,20,30)




# #-------------------------------------------
# class A:
#
#     a = 100
#
#     def display(self):
#         print(f'The value of a is {self.a} ')
#
# class B(A):
#
#     a = 200
#
#     def spam(self):
#         print(f'The value of a is {self.a}')
#
# b = B()
# b.display()     #The value of a is 200
# b.spam()        #The value of a is 200


# ---------------------------