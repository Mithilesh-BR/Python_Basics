
# The while Loop

# With the while loop we can execute a set of statements as long as a condition is true.

# Note: remember to increment i, or else the loop will continue forever.

# ""The while loop requires relevant variables to be ready,
# in this example we need to define an indexing variable, i, which we set to 1.""



# _______________________________________________


# Print i as long as i is less than 6:

# i = 1
# while i < 6:
#   print(i)
#   i += 1
# ___________________________________________________________________________________________________________

# The break Statement:

# With the break statement we can stop the loop even if the while condition is true:
#
# Example
# Exit the loop when i is 3:
#
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1
# ______________________________________________________________________________________________________

# The continue Statement:

# With the continue statement we can stop the current iteration, and continue with the next:
# Example
# Continue to the next iteration if i is 3:
#
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)



# _____________________________________________________________________________________________________
# The else Statement:

# With the else statement we can run a block of code once when the condition no longer is true:
#
# Example
# Print a message once the condition is false:
#
# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")
# ______________________________________________________________________________________________




# ________________________________________________________________________________________________________________
# 1.

# count = 0
#
# while (count <10):
#
#     # count += 1
#     print(count)
#     count += 1
# -----------------------------------------------------
# 2.
# countdown = 5
# while countdown>0:
#     print(countdown)
#     countdown -=1
# print("Blast off !")

# -------------------------------------------------------

# age=int(input('Enter your age:'))
#
# while age >18:
#     print('You are eligible to VOTE')
#     break
# else:
#     print("you are not eligible to vote")
# ------------------------------------------------------




# practice


# i=1
# while i<5:
#     print('MITHILESH',end=" ")
#     i+=1
#     J=1
#     while J<5:
#         print('INDIAN',end=" ")
#         J+=1
#     print()
# ___________________________________________
# s='Hello this is python world'
#
# i=0
# while i<len(s):
#     print(s[i],end='')
#     i+=1
# ___________________________________________
# i=1
# while i<=20:
#     if i%2==0:
#         print(i, end='   ')
#     i+=1

# ___________________________________________
# s='Hello this is python world'
#
# res=''
# i=0
# while i<len(s):
#     if s[i] in 'aeiouAEIOU':
#         res+=s[i]
#     i+=1
# print(f'"{res}" are the vowel letters present in the string')

# ___________________________________________

# lst=['apple', 'google','microsoft','amazon','flipkart']
# res=[]
# i=0
# while i<len(lst):
#     res.append(lst[i].upper())
#     i+=1
# print(res)

# 1️⃣ Print numbers from 1 to 10
#
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
i=1
while i<=10:
    print(i)
#
# 2️⃣ Print numbers from 10 to 1
# i = 10
# while i >= 1:
#     print(i)
#     i -= 1
#
# 3️⃣ Print even numbers from 1 to 20
# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1
#
# 4️⃣ Print odd numbers from 1 to 20
# i = 1
# while i <= 20:
#     if i % 2 != 0:
#         print(i)
#     i += 1
#
# 5️⃣ Sum of numbers from 1 to n
# n = 10
# i = 1
# total = 0
#
# while i <= n:
#     total += i
#     i += 1
#
# print(total)
#
# 6️⃣ Factorial of a number
# n = 5
# i = 1
# fact = 1
#
# while i <= n:
#     fact *= i
#     i += 1
#
# print(fact)
#
# 7️⃣ Reverse a number
# num = 1234
# rev = 0
#
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10
#
# print(rev)
#
# 8️⃣ Check palindrome number
# num = 121
# temp = num
# rev = 0
#
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10
#
# if temp == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
#
# 9️⃣ Multiplication table
# n = 5
# i = 1
#
# while i <= 10:
#     print(n, "*", i, "=", n*i)
#     i += 1
#
# 🔟 Count digits in a number
# num = 56789
# count = 0
#
# while num > 0:
#     count += 1
#     num //= 10
#
# print(count)
#
# 1️⃣1️⃣ Sum of digits
# num = 1234
# total = 0
#
# while num > 0:
#     digit = num % 10
#     total += digit
#     num //= 10
#
# print(total)
#
# 1️⃣2️⃣ Largest digit in number
# num = 52964
# largest = 0
#
# while num > 0:
#     digit = num % 10
#     if digit > largest:
#         largest = digit
#     num //= 10
#
# print(largest)
#
# 1️⃣3️⃣ Fibonacci series
# n = 10
# a, b = 0, 1
# i = 1
#
# while i <= n:
#     print(a)
#     a, b = b, a + b
#     i += 1
#
# 1️⃣4️⃣ Check prime number
# num = 7
# i = 2
# flag = True
#
# while i < num:
#     if num % i == 0:
#         flag = False
#         break
#     i += 1
#
# if flag:
#     print("Prime")
# else:
#     print("Not Prime")
#
# 1️⃣5️⃣ Print numbers divisible by 5
# i = 1
#
# while i <= 50:
#     if i % 5 == 0:
#         print(i)
#     i += 1
#
# 1️⃣6️⃣ Guess number game
# secret = 7
# guess = 0
#
# while guess != secret:
#     guess = int(input("Enter number: "))
#     if guess == secret:
#         print("Correct!")
#
# 1️⃣7️⃣ Print square numbers
# i = 1
#
# while i <= 10:
#     print(i*i)
#     i += 1
#
# 1️⃣8️⃣ Count vowels in string
# s = "pythonprogramming"
# i = 0
# count = 0
#
# while i < len(s):
#     if s[i] in "aeiou":
#         count += 1
#     i += 1
#
# print(count)
#
# 1️⃣9️⃣ Print list elements
# lst = [10, 20, 30, 40]
# i = 0
#
# while i < len(lst):
#     print(lst[i])
#     i += 1
#
# 2️⃣0️⃣ Find maximum number in list
# lst = [10, 4, 67, 32, 99]
# i = 0
# max_val = lst[0]
#
# while i < len(lst):
#     if lst[i] > max_val:
#         max_val = lst[i]
#     i += 1
#
# print(max_val)