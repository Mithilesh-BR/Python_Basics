'''PATTERN PRINTING'''

# rows=5
# ascii_value=65
#
# for i in range(rows):
#     for j in range(i+1):
#         a=chr(ascii_value)
#         print(a,end=' ')
#
#     ascii_value +=1
#     print()


'''
*
* *
* * *
* * * *
'''
# for i in range(1, 5):
#     print('* ' * i)

#------------------------------------------
'''
* * * *
* * *
* *
*
'''
# for i in range(4, 0, -1):
#     print('* ' * i)

#--------------------------------------------
''' right justified triangle

   *
  **
 ***
****
'''
# for i in range(1, 5):
#     print(f'{"*" * i:>5}')

# -----------------------------------'

'''
      *
    * *
  * * *
* * * *
'''

# for i in range(1, 5):
#     print(f'{"* " * i:>8}')

#-----------------------------------------
'''
* * * *
  * * *
    * *
      *
'''

# for i in range(4, 0, -1):
#     print(f'{"* " * i:>8}')

#--------------------------------------------------
'''
equilateral
   *
  * *
 * * *
* * * *
'''
# for i in range(1, 5):
#     print(f'{"* " * i:^8}')

#-------------------------------------
'''
* * * *
 * * *
  * *
   *
'''
# for i in range(4, 0, -1):
#     print(f'{"* " * i:^8}')

#-------------------------------
'''
*
* *
* * *
* * * *
* * *
* *
*
'''
# for i in range(1, 5):
#     print('* ' * i)
# for j in range(3, 0, -1):
#     print('* ' * j)

#-----------------------------------
'''
*
*
* *
*
* * *
*
* * * *
*
'''
# for i in range(1, 5):
#     print('* ' * i)
#     print('abc')


#---------------------------------------
'''
1
1 2
1 2 3
1 2 3 4
'''
# res = ''
# for i in range(1, 5):
#     res += str(i) + ' '             #res = res + str(i) + ' '
#     print(res)

'''
      1
    1 2
  1 2 3
1 2 3 4
'''
# res = ''
# for i in range(1, 5):
#     res += str(i) +' '
#     print(f'{res:>8}')

#------------------------------
'''
   1
  1 2
 1 2 3
1 2 3 4
'''
# res = ''
# for i in range(1, 5):
#     res += str(i) +' '
#     print(f'{res:^8}')

#----------------------------------
'''
a 
a b 
a b c
a b c d
'''
# res = ''
# for i in range(ord('a'), ord('e')):
#     res += chr(i) + ' '
#     print(res)

# rows = 6
# b=0
# i
#
# i[[isj26
# /
# for i in range(rows):
#     for j in range(i):
#         print(i, end='')
#     print('')

# def full_pyramid(n):
#     for i in range(1, n+1):
#         for j in range(n-i):
#             print('', end='')
#         for k in range(1, 2*i):
#             print('*', end='')
#         print()
#
# full_pyramid(5)