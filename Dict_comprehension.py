'''Dict comprehension'''

'''1. create a dict, where'''

# list_ = [10.5, 'True', True, 'python', 'selenium', False]
# d = {}
# for ele in list_:
#     if isinstance(ele,str):
#         d[ele] = len(ele)
# print(d)

# #Using dict comprehension
# d = {ele:len(ele) for ele in list_ if isinstance(ele, str)}
# print(d)

#----------------------------------------
'''2. '''

# data = ['tata', 'siri', 'cricket', 'alexa', 'google', 'chatgpt']
# d = {}
# for ele in data:
#     if len(ele)%2==0:
#         d[ele] = ele
#     else:
#         d[ele] = ele[::-1]
# print(d)

## Using dict comprehension
# res = {ele:ele if len(ele)%2==0 else ele[::-1] for ele in data}
# print(res)

#---------------------------------------------------------

'''3.  wap to build a dict of item and its index from the given string'''
# s = 'python'
# d = {}
# for index,char in enumerate(s):
#     d[char] = index

# print(d)

# d = { char:index for index,char in enumerate(s)}
# print(d)

# ----------------------------------------------------------------------------------------

'''4. wap to check each item of string is alphabet or not, if it is alphabet, consider 
that has a key and its ASCII code as value'''

# s = 'python'
# d = {}
# for char in s:
#     if char.isalpha():
#         d[char] = ord(char)

# print(d)

# d = { char:ord(char) for char in s if char.isalpha()}
# print(d)
# ----------------------------------------------------------------------------------------

'''5. wap to build a dictionary whose prize value > 400 from the given dict'''

# data = {'ibm':1000, 'tata':2000, 'wipro':3000, 'fb':100}
# d = {}
# for key,value in data.items():
#     if value > 400:
#         d[key] = value
# print(d)
#
# d= { key:value for key,value in data.items() if value > 400}
# print(d)

# -----------------------------------------------

'''6. wap to build a dict of dial code and its country name from the given collection'''

# c = [(86,'china'),(91,'india'),(1,'us'),(90,'pakistan')]
# d = {}
# for number,country in c:
#     d[number] = country
# print(d)
#
# a = { number:country for number, country in c}
# print(a)

'''7. '''

# s = 'hey there I am using whatsapp'             ## {h:3, e:3, ,..}
# d = {}
# for ele in s:
#     if s.count(ele) > 1:
#         if ele != ' ':
#             d[ele] = s.count(ele)
# print(d)
#
#
# ## Using Dict comprehension
# res = {ele:s.count(ele) for ele in s if s.count(ele)>1 if ele!=' '}
# print(res)

#---------------------
'''8. Flip the key value pair'''

# d1 = {'one':1, 'two':2, 'three':3}          #{1:'one', 2:'two', 3:'three'}
# d = {}
# for key, value in d1.items():
#     d[value] = key
# print(d)
#
# d = {value:key for key, value in d1.items()}
# print(d)
#-------------------------------------