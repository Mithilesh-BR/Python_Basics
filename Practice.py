# s="amazon"
# if s[0].lower() in"aeiouAEIOU":
#     print(f'{s} starts with vowel')

# num=79
# if num>0:
#     print(f'{num},is positive')

# num=56
# if num%2==0:
#     print(f'{num} is even')

# class_time=10:00 am
# student_allowed_time=float(input('enter class time:'))
# if student_allowed_time<=10:
#     print("Allow student to join class")
# else:
#     print('Student is not allowed')

# s=input('Enter the string:')
# if len(s)%2==0:
#     print(f'{s}','has even length',sep='\n')
# else:
#     print(f'{s}','has odd length',sep='\n')

# s=input('Enter the Name:')
# if ord('A')<ord(s[0])<ord('Z'):
#     print(f'{s}','starts with uppercase',sep='\n')
# else:
#     print(f'{s}','starts with lowercase',sep='\n')

# char='5'
# if char.isdigit():
#     print('yes')
# else:
#     print('no')

# year=int(input('Enter the Year:'))
# if year%2==0 or year%100!=0 and year%4==0:
#     print(f'{year}','Leap Year',sep='\n')
# else:
#     print(f'{year}','Not a leap year',sep='\n')

# n=int(input('Enter the number:'))
# if (n%10)%3==0 :
#     print(n,'number is divisible by 3')
# else:
#     print(n,'is not divisible by 3')

# s='samsung'
# if s[len(s)//2] in 'aeiouAEIOU':
#     print(s,'is a vowel',end='___________________')
# else:
#     print(s,'is a consonant',end='_______________')

# n=int(float(input('Enter the num:')))
#
# if isinstance(n,(int,float)):
#     print(f"square:{n**2} \n cube:{n**3}")
# else:
#     print(n,'is not a integer')

# loan_amount=int(input('Enter the amount:'))
# print(f'{'='*50}\n',f'options:\n',f'personal_loan:1\n',f'car_loan:2\n',f'house_loan:3\n','{'='*50}\n')
#
# option=int(input('Enter your options:'))
#
# if option=='1':
#     interest=loan_amount*(0.11)
#     print(f'loan_amount:{'loan_amount'}\n)',f'interes_charges:Rs {'interest'}n\',f'Total_amount:{})


# lst=['jasmine flower','rose flower','toger animal','cow animal','apple fruit', 'mango fruit']
#
# res={}
#
# for wrd in lst:
#     wrd=wrd.split(' ')
#     if wrd[1] not in res:
#         res[wrd[1]]=[wrd[0]]
#     else:
#         res[wrd[1]]+=[wrd[0]]
# print(res)

# n=5
# for i in range (1,n+1):
#     for j in range (1, n+1):
#         if i==1 or i==n or j==1 or j==n:
#             print('#',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# print()

# n=5
# for i in range(1,n+1):
#     for j in range (1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#             print('#',end=' ')
#         else:
#             print(" ",end=" ")
#     print()
# print()

# n=5
# for i in range (1,n+1):
#     for j in range (1, n+1):
#         print((i,j),end=' ')
#     print()
# print()

# n=5
# for i in range (1,n+1):
#     for j in range (1, n+1):
#         if i>=j:
#             print('*',end=' ')
#     print()
# print()

# for i in range(1,6):
#     print(' *'*i)

# a= 'keerthi'
# b= ' kumar'
# print(a+b)

# for i in range (1,6):
#     for j in range (1,6):
#         if i==j or i+j==5+1:
#             print('#',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# print()

# for i in range (1,8):
#     for j in range (1,8):
#         if i==7//2+1 or j==7//2+1:
#             print('@',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# print()

# for i in range (1,8):
#     for j in range (1,8):
#         if i==7//2+1 or j==7//2+1:
#             print('@',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# print()
# n=15
# for i in range (1,n+1):
#     for j in range (1,n+1):
#         if  i==n//2+1 or j==n//2+1 or i==j or i+j==n+1:
#             print('#',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# print()

# a='hello'
# b=['hai','good','evening']
# c={1,2,3,4,5}
# for ele in zip(a,b,c):
#     print(ele)

# cities=['bangalore','mandya','mysore']
# pincode=[454545,4554,69664,641919,696161]
#
# for ele in zip(cities,pincode):
#     print(ele)

# a='python'
# b={'india':'delhi','usa':'washington','srilnka':'columbo'}
# for ele in zip(a,b.items()):
#     print(ele)
# from iterables import zip_longest


from itertools import zip_longest

# a='hello'
# b='hai'
# for ele in zip_longest(a,b,fillvalue=100):
#     print(ele)


# a='hello'
# b=['hai','good','evening']
# c={1,2,3,4,5,6}
# for ele in zip_longest(a,b,c,fillvalue='god'):
#     print(ele)

# a='abracadabra'
# d={}
# for ele in a:
#     # d[ele]=a.count(ele)
#
#     if ele not in d:
#         d[ele]=1
#     else:
#         d[ele]+=1
# print(d)

# d={}
# number_list=[1,2,3,4,5,6,7,8]
# for index,item in enumerate(number_list):
#     # print(item**index)
#     d[item]=item**index
# print(d)

# d={'a':3,'b':5,'c':8,'d':7}
# for num,ele in enumerate (d.items()):
#     print(num,ele)

# s='hello'
# for j,i in enumerate(s):
#     if j%2==0:
#         print(i,end=' ')


# names=['arun','varun','veer','ram']
# print(enumerate(names))

# l=[1,2,3,4,5,6]
# res=reversed(l)
#
# print(list(reversed(l)))
#
# l=[65465,'hello','hai',[5,6,8],8+45j]
# res=reversed(l)
#
# print(list(reversed(l)))

# d={'a':5,'b':8,'c':10,'d':89}
# print(tuple(reversed(d.items())))


# s={'maths','science',54699,669959494919}
# print(tuple(reversed(s)))

# s=[2,4,5,8,6,9]
# res=[i**2 for i in s]
# print(res)


# s=[2,3,5,6,4,6]
# res=[]
# for i in s:
#     if i%2==0:
#         res.append(i**2)
# print(res)

# s=[2,5,6,5,9,5,6]
# res=[i**2 for i in s if i%2!=0]
#
# print(res)


# s=[2,6,5,8,9,7,8,4]
# res=[]
# for i in s:
#     if i%2==0:
#         res.append(i**2)
#     else:
#         res.append(i**3)
# print(res)

# s=[2,3,56,8,4,65,6,5]
# res=[i**2 if i%2==0 else i**3 for i in s]
# print(res)

# ______________________________________________________________

# MULTI-THREADING
# from time import sleep
# from threading import *
#
# class Hi(Thread):
#     def run(self):
#         for i in range(10):
#             print("Hi")
#             sleep(1)
#
# class Hello(Thread):
#     def run(self):
#         for i in range(10):
#             print("Hello")
#             sleep(1)

# t1=Hi()
# t2=Hello()
#
# t1.start()
# sleep(0.2)
# t2.start()
#
# sleep(30)
# print('Bye Bye')

# -----------------------------------------------------------------

# lst=[5,5,4,8,9,5,0,9,0,7,8,0,8,0,9]
#
# for ele in lst:
#     if ele==0:
#         lst.remove(ele)
#         lst.append(ele)
# print(lst)

# _____________________________________________________________________

# x=2
# y='5'
#
# print(x*x)
# print(x*y)

# for x range in (1,11):
#     if x%3==0:
#         break
#     print(x)

# for x in 'geeksforgeeks':
#     if x=='e' or x=='s':
#         continue
#     print('current letter:', x)

# x=1
# while x < 100:
#     x*=2
# print(x)

# n=5
# for i in range (1,n+1):
#     for j in range (1,n+1):
#         print('*',end='  ')
#     print()

# n=5
# for i in range (1,n+1):
#     for j in range (1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#             print('*', end='  ')
#         else:
#             print(' ',end='  ')
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>=j:
#             print('#',end='  ')
#         else:
#             print(' ',end=' ')
#     print()

# n=9
# for i in range (1,n+1):
#     for j in range (1,n+1):
#         if j>=i:
#             print('#',end='   ')
#         else:
#             print('  ',end='')
#     print()


# n=5
# for i in range (1,n+1):
#     for j in range (1,n+1):
#         if i==j or i+j==(n+1):
#             print(' #',end=' ')
#         else:
#             print('  ',end=' ')
#     print()
# ------------------------------------------------------------------------
# from abc import ABC, @abstractmethod

# class student():
#
#     # def __init__(self,name):
#     #     self.name=name
#
#     def uniform(self):
#         print('Boys have unique uniform')
#
#     # @property
#     def study(self):
#         print('yes i am studying')
#
#     def playing(self):
#         print('yash is a boy')

# boy1=student()
# boy1.playing()

# s='hi hello i have started giving interviews'
#
# print(s.find('i'))
# ------------------------------------------------------------------------------------------------
# from copy import deepcopy
#
# x=[5451,4,15,54,51,15,15,1,1,789794,8,464,84,4,945,4249,[84894,84,94,8,468,4,84,984,9,4,15,18,48,18,1]]
# y=[4,1,587,8415,189,165,185,198,478,4181,7,415,168,4,165,185,4189,[898185,484,84,84,894,8,4,5,4547,9794]]
#
# print(id(x))
# print(id(y))
#
# y=deepcopy(x)
#
# print(id(x))
# print(id(y))

# i=1
# while i<=4:
#     print('Mithilesh is confident and cool')
#     i+=1

# s='Hello'
# i=0
# while i<=4:
#     print(s[i])
#     i+=1

# s='google'

# res=''
# i=1
# while i<=len(s):
#     res+=s[-i]
#     i+=1
# print(res)

# lst=['apple','google','microsoft','amazon','flipkart']
#
# res=[]
# i=1
#
# while i<=len(lst):
#     res.append(lst[-i][::-1])
#     i+=1
# print(res)

s = 'Mithilesh Rathod'

# res=''
# i=0
# while i<len(s):
#     res=s[i]+res
#     i+=1
# print(res)
# res=''
# i=1
# while i<=len(s):
#     res+=(s[-i])
#     i+=1
# print(res)

# print(15 & 87)
# print(84|64)
# print(~949)
# print(894^849)
# print(45<<2)
# print(bin(15))
#
# def greet():
#     print("Hi, I am Mithilesh Rathod \n I am learning Programming")
#
# greet()

# ---------------------------------------------------------------------------------

# def mult(a,b):
#     print(a*b)
#
# mult(5,4)


# def mult(*args):
#     result=1
#     for num in args:
#         result *=num
#     return result
#
# result=mult(8,9,6,7,5,6,4)
# print(result)

# ---------------------------------------------------------------------------------

# def square_num(*args):
#     list=[]
#     for ele in args:
#         if type(ele) is int:
#             print(ele**2)
#         else:
#             print(ele)
#
# list=square_num(5,2,3,'jdwehvqre',5,1,12.525,6)
# print(list)

# --------------------------------------------------------------------------------
# def reverse(*args):
#     for ele in args:
#         if ele == ele[::-1]:
#             print('yes, word is palindrome')
#         else:
#             print ('no, word is not palindrome')
#
# reverse('malayalam','mom','dad','kannada','house')

# import random
#
# dice_numbers = ['one', 'two', ' three', 'four', 'five', 'six']
# dice_num = random.randint(0, 5)
# print(dice_numbers[dice_num])
# ---------------------------------------------------------------------------------
from array import *
#
# arr = array('i', [])
#
# n = int(input('enter the length of the array : '))
#
# for i in range(n):
#     x=int(input('enter the value : '))
#     arr.append(x)
#
# print(arr)
#
# val = int(input('enter the value of search : '))
#
# k=0
# for ele in arr:
#     if ele == val:
#         print(k)
#         break
#
#     k+=1
#
# print(arr.index(val))
# -------------------------------------------------------------------------------------

# from numpy import *
#
# arr = array([5, 9, 8, 6, 7.5, 5, 3])
# print(arr.dtype)
# print(arr)

# -----------------------------------------------------------------
# def simple_interest(a, b, c):
#     return ((a*b*c)/100)
#
# print(simple_interest(30000, 2, 5))

# si = lambda p, t, r : (p*t*r)/100
# res= si(30000,2,5)
# print(res)

# --------------------------------------------------------------------------

# p = int(input("Enter the principal amount: "))
# t = int(input("Enter the Time: "))
# r = int(input("enter the rate of interest: "))
#
# def ci(p, t, r):
#     amount = p * ( pow((1+r/100),t))
#     ci = amount - p
#     return ci
#
# # res=ci(4521561, 5, 3.5/100)
#
# print(ci(p, t, r))

# ------------------------------------------------------------------------


# str = input("Enter a string: ")
# # textlength = len(str)
#
# for char in str:
#     ascii = ord(char)
#     print(char, "\t", ascii)

# ------------------------------------------------------------------
# fibonacco_range = int(input("Enter the n"))
#
# c = 0
# while count<nterms:
#     print(n1)
#     nth = n1 + n2
#     n1 = n2
#     n2 = nth
#     count += 1
