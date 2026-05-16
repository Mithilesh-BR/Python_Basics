'''FILE HANDLING'''
import csv

'''
1. open the file
2. read/write
3. close the file
'''

#-----------------------------------------------------------------------------------------------
'''opening the file
1. without context manager
2. with context manager
'''

#------------------
'''without context manager : '''


# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\python_class\sample.txt'
# file = open(path)
# # print(file)
# # print(next(file))
# print(file.closed)
# file.close()
# print(file.closed)

## Here in without context manager, we have to close the file manually
## To open the file, we will be using open() func
## To close the file, we use close() func

'''
file path should be given in the string format.
'''
#----------------------------------------------------------------------------
'''with context manager'''
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\python_class\sample.txt'
# with open(path) as file:
#     print(file)
#     print(next(file))
#     print(next(file))
#     print(file.closed)

# print(file.closed)

#---------------------------------------------------------------------------------------------------------
'''
modes
1. read = r (default mode)
2. write = w
3. append = a
4. create = x
'''

#----------------------------------------------------------------------------
'''read mode = r
To open the file in the read mode. Read mode is the default mode
Modes also should be given in the string format
'''
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\python_class\sample.txt'
# with open(path, 'r') as file:
#     print(file)     #file objecct
#     print(next(file))

# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\python_class\sample1.txt'
# with open(path, 'r') as file:
#     print(file)     #FileNotFoundError
'''If we try to open the file which is not present, read mode will give FileNotFoundError'''

#--------------------------------------------------------------------------
'''write mode : w'''
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\python_class\sample.txt'
# with open(path, 'w') as file:
#     print(file)     #file object

'''Whenever we open the file in write mode, whatever the data we had
## in the file will be completely lost.'''


# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\python_class\sample1.txt'
# with open(path, 'w') as file:
#     print(file)

'''If we open the file which is not present, write mode will not give
any error instead it will create a new file'''

#--------------------------------------------------------------------------------
'''append mode : a
Will add the data to the existing data
'''
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\python_class\sample.txt'
# with open(path, 'a') as file:
#     print(file)     #file object

# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\python_class\sample2.txt'
# with open(path, 'a') as file:
#     print(file)

'''If we try to open the file which is not present, append mode will
## create a new file'''

#-----------------------------------------------------------------------------------
'''create mode = x '''
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\python_class\spam.txt'
#
# with open(path, 'x') as file:
#     print(file)

# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\python_class\sample.txt'
# with open(path, 'x') as file:
#     print(file)     #FileExistsError

#-------------------------------------------------------------------------------------------------------
'''reading the file
1. read()
2. readline()
3. readlines()
'''

'''read() : Reads the data from starting to end of the file'''
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\python_class\sample.txt'
# with open(path) as file:
#     res = file.read()
#     print(type(res))        #<class 'str'>
#     print(res)

'''## read() func will read the data in the form of strings'''
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\python_class\sample.txt'
# with open(path) as file:
#     res = file.read(12)
#     print(res)

'''## when we pass the parameters to the read() func, it will read till that number'''

#----------------------------------------------
'''readline() : It will read one line at a time and the line will be stored in 
the form of strings'''
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\python_class\sample.txt'
# with open(path) as file:
#    print(file.readline())
#    print(file.readline())
#    print(file.readline())

# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\python_class\sample.txt'
# with open(path) as file:
#    print(file.readline(30))

#-----------------------------------------------
# f_path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\python_class\sample.txt'
# with open(f_path) as file:
#    # print(file)
#    # res = file.read()
#    # print(type(res))
#
#    print(file.read())
#    print('***************************************')
#    print(file.read())

'''files are iterator objects. once the file is read, the control will
be in the last position, so if we perform read() operation again, it 
will not print anything. To read the file again, we have to initialize 
the file again'''

#---------------------------------
'''readlines():'''
# f_path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\python_class\sample.txt'
# with open(f_path) as file:
#    print(file.readlines())

# f_path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\python_class\sample.txt'
# with open(f_path) as file:
#    # print(file.readlines())    #['hello world\n', 'python\n', 'selenium']
#    print(file.readlines(14))

# with open(file.txt) as file:
#     print(file.readlines())



#----------------------------------------------------------------------------------------------------------------
'''1. wap to count the number of lines in the file'''
# file_path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample1.txt'
# with open(file_path) as file:
    # line_count = 0
    # for line in file:
    #     line_count += 1
    # print(line_count)


    # print(len(file))    #TypeError: object of type '_io.TextIOWrapper' has no len()

'''whenever we traverse on the files, for each iteration, it will
consider one line at a time, and each line will be considered as strings

Since files are iterator objects, we cannot find the length of a file 
using len() inbuilt function
'''

#----------------------------------------
'''2. wap to count the number of characters present in each line'''
# file_path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample1.txt'
# with open(file_path) as file:
#     res = file.readlines()
#     # print(res)
#     for line in res:
#         print(line, '=', len(line))

## Alternate solution
# file_path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample1.txt'
# with open(file_path) as file:
#     for line in file:
#         count = 0
#         for ele in line:
#             count += 1
#         print(f'{line} = {count}')

#----------------------------------
'''3. wap to print the line along with its line num'''
# file_path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample1.txt'
# with open(file_path) as file:
#     count = 0
#     for line in file:
#         count += 1
#         print(f'{count} . {line}')

## Alternate solution
# file_path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample1.txt'
# with open(file_path) as file:
#     for line_no, line in enumerate(file, start=1):
#         print(f'{line_no}. {line}')

#----------------------------------------------
'''wap to find number of words present in each line'''
# file_path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample1.txt'
# with open(file_path) as file:
#     for line in file:
#         res = line.split()
#         print(len(res))
#

#------------------------------------------------
'''wap to reverse the lines in sample.txt file'''
# f_path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample1.txt'
# with open(f_path) as file:
#     for line in file:
#         print(line[::-1])

## Alternate solution
# f_path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample1.txt'
# with open(f_path) as file:
#     for line in file:
#         rev_line = ''
#         for ele in line:
#             rev_line = ele + rev_line
#         print(rev_line)

## Alternate solution
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample1.txt'
# with open(path) as file:
#     for line in file:
#         for ele in reversed(line):
#             print(ele, end='')

#---------------------------------------------------------------------------------
'''wap to read a file in reversed order'''
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample1.txt'
# with open(path) as file:
#     for line in reversed(list(file)):
#         print(line)

#---------------------------------------------------------------------------------
'''wap to read a file in reversed order also reverse the lines'''
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample1.txt'
# with open(path) as file:
#     for line in reversed(list(file)):
#         print(line[::-1])

#------------------------------------
'''wap to read 10 characters at a time'''
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample1.txt'
# with open(path) as file:
#     print(file.read(10))
#
# print('*******************************************')
#
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample1.txt'
# with open(path) as file:
#     print(file.readline(10))

#---------------------------
# '''
# DO IT YOURRSELF
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample1.txt'
# with open(path) as file:
#     print(file.read(50))
#
# print('*******************************************')
#
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample1.txt'
# with open(path) as file:
#     print(file.readline(50))
# '''

#--------------------------------------------------------------
'''wap to read 10 characters from 3 line'''
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample1.txt'
# with open(path) as file:
#     first_line = next(file)
#     second_line = next(file)
#     print(file.read(10))

#-----------------------------------------
'''wap to extract IP addresses from access-log.txt file'''
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\access-log.txt'
# with open(path) as file:
#     for line in file:
#         if line.strip():
#             res = line.split()
#             print(res[0])

#------------------------------------
'''wap to count number of occurances of the IP address'''
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\access-log.txt'
# with open(path) as file:
#     ip_addresses = []
#     for line in file:
#         if line.strip():
#             res = line.split()
#             ip_addresses.append(res[0])
#
#     for ip_address in set(ip_addresses):
#         print(ip_address, '-', ip_addresses.count(ip_address))

#------------------------------------------------
'''IP address and its count pair'''
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\access-log.txt'
# with open(path) as file:
#     ip_addresses = {}
#     for line in file:
#         if line.strip():
#             res = line.split()
#             if res[0] not in ip_addresses:
#                 ip_addresses[res[0]] = 1
#             else:
#                 ip_addresses[res[0]] += 1
#     print(ip_addresses)



## Using default dict
# from collections import defaultdict
#
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\access-log.txt'
# with open(path) as file:
#     ip_addresses = defaultdict(int)
#     for line in file:
#         if line.strip():
#             res = line.split()
#             ip_addresses[res[0]] += 1
#
#     print(ip_addresses)

#-----------------------------------------------------
'''wap to extract the msgs from sample.log file'''
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample.log'
# with open(path) as file:
#     for line in file:
#         if line.strip():
#             res = line.split()
#             print(res[2])

'''msg and its count pair'''
## Using count method
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample.log'
# with open(path) as file:
#     msgs = []
#     for line in file:
#         if line.strip():
#             res = line.split()
#             msgs.append(res[2])
#
#     for ele in set(msgs):
#         print(ele, '-', msgs.count(ele))

## Normal dictionary
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample.log'
# with open(path) as file:
#     msgs = {}
#     for line in file:
#         if line.strip():
#             res = line.split()
#             if res[2] not in msgs:
#                 msgs[res[2]] = 1
#             else:
#                 msgs[res[2]] += 1
#
#     print(msgs)

## Default dictionary
# from collections import defaultdict
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample.log'
# with open(path) as file:
#     msgs = defaultdict(int)
#     for line in file:
#         if line.strip():
#             res = line.split()
#             msgs[res[2]] += 1
#
#     print(msgs)

#------------------------------------------------------
'''wap to get country names from football.txt file'''
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\football.txt'
# with open(path, encoding='UTF-8') as file:
#     for line in file:
#         if line.strip():
#             res = line.split('\t')
#             print(res[1])

'''country and its count pair'''
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\football.txt'
# with open(path, encoding='UTF-8') as file:
#     country_count_pair = {}
#     for line in file:
#         if line.strip():
#             res = line.split('\t')
#             if res[1] not in country_count_pair:
#                 country_count_pair[res[1]] = 1
#             else:
#                 country_count_pair[res[1]] += 1
#
#     print(country_count_pair)

## Using default dict
# from collections import defaultdict
#
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\football.txt'
# with open(path, encoding='UTF-8') as file:
#     country_count_pair = defaultdict(int)
#     for line in file:
#         if line.strip():
#             res = line.split('\t')
#             country_count_pair[res[1]] += 1
#
#     print(country_count_pair)

#---------------------------------------------
'''wap  to print most occuring country name along with counts'''
# from collections import Counter
#
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\football.txt'
# with open(path, encoding='UTF-8') as file:
#     country_names = []
#     for line in file:
#         if line.strip():
#             res = line.split('\t')
#             country_names.append(res[1])
#             country_count_pair = Counter(country_names)
#     print(country_count_pair)       #dict
#     res = Counter.most_common(country_count_pair)  #list of tuples of country and number of times it is repeated
#     print(res[0])

#---------------------------------------------
'''create a dict, key as group and value as list of countries belongs 
to that group'''
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\football.txt'
# with open(path, encoding='UTF-8') as file:
#     header = next(file)
#     group_country = {}
#     for line in file:
#         if line.strip():
#             res = line.split('\t')
#             group_name = res[0]
#             country_name = res[1]
#             if group_name not in group_country:
#                 group_country[group_name] = [country_name]
#             elif country_name not in group_country[group_name]:
#                 group_country[group_name] += [country_name]
#
#     print(group_country)


#--------------------------------------------------------
'''
WRITING INTO A FILE
1. write()
2. writelines()
'''

#-------------------------------------------------------
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\file1.txt'
# with open(path, 'w') as file:
#     print(file.write('version control'))

'''write mode will override the existing data
write() will give the length od str as an output'''
#-------------------------------------
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\file1.txt'
# with open(path, 'w') as file:
#     print(file.write(['version control', 'python packages']))       #TypeError

'''Because write() takes only strings as arguments'''

#------------------------------------------
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\file1.txt'
# with open(path, 'a') as file:
#     print(file.write('version control', 'python packages'))     #TypeError
#
'''write() takes only one argument.
# ## To be more precise, write() takes only one string as argument'''

#------------------------------------------
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\file1.txt'
# with open(path, 'a') as file:
#     file.write('hello world\n')
#     file.write('hello universe\n')
#     file.write('welcome to India')

#-----------------------
'''writelines()'''
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\file1.txt'
# with open(path, 'w') as file:
#     file.writelines(['python', 'selenium', 'robot framework', 'django', 'datastructures'])      #pythonseleniumrobot frameworkdjangodatastructures
#     file.writelines(['python\n', 'selenium\n', 'robot framework\n', 'django\n', 'datastructures\n'])

'''writelines takes list of strings as argument'''
#------------------------
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\file1.txt'
# with open(path, 'w') as file:
#     file.writelines(['python\n', 'selenium'], ['hello', 'world'])       #TypeError
#
'''because writelines() takes only one argument'''
#----------------------------
'''CSV FILE HANDLING
csv = comma seperated value
'''
# path = r"C:\Users\Ramya\OneDrive\Desktop\logincredentials.xlsx"
# with open(path) as file:
#     print(file)
#     print(file.read())

'''To deal with the excel files, we use CSV file handling

## import csv'''

#--------------------------------------------------
'''
CSV
To read a csv file
csv.reader
csv.DictReader

To write into a csv file
csv.writer
csv.DictWriter
'''

'''csv.reader()'''
# import csv
# path = r"C:\Users\Ramya\OneDrive\Desktop\example.csv"
# with open(path) as file:
#     file_data = csv.reader(file)     #<_csv.reader object at 0x00000266F26E8AC0>
#     for data in file_data:
#         print(data)

## csv.reader() will give a list

#------------------------------
'''csv.DictReader()'''
# import csv
# path = r"C:\Users\Ramya\OneDrive\Desktop\example.csv"
# with open(path) as file:
#     file_data = csv.DictReader(file)     #<csv.DictReader object at 0x000002A0FF796A50>
#     for data in file_data:
#         print(data)

## DictReader will give a dictionary, headers as the keys and the elements from 2nd row will be the value

#---------------------------------------------------
# path = r"C:\Users\Ramya\OneDrive\Desktop\logindata.xlsx"
# with open(path) as file:
#     print(file)
#     print(csv.reader(file))

#----------------------------------------------------
'''wap to extract total vaccinations of all the countries'''
# Using reader
# import csv

# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\vaccine.csv'
# with open(path) as file:
#     vaccine_data = csv.reader(file)
#     header = next(vaccine_data)
#     for data in vaccine_data:
#         print(data[5])

## Using DictReader()
# import csv
#
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\vaccine.csv'
# with open(path) as file:
#     vaccine_data = csv.DictReader(file)
#     for data in vaccine_data:
#         print(data['TOTAL_VACCINATIONS'])

#-----------------------------------------------------------
'''wap to add the total vaccinations of all countries'''
# import csv
#
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\vaccine.csv'
# with open(path) as file:
#     total_vaccines = 0
#     vaccine_data = csv.reader(file)
#     header = next(vaccine_data)
#     for data in vaccine_data:
#         if data[5].strip():
#             total_vaccines += int(data[5])
#     print(total_vaccines)

# ------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------



import csv

'''
1. open the file
2. read/write
3. close the file
'''

'''opening the file
1. without context manager : file path should be given in the string format.
2. with context manager
'''


'''
modes:

1. read = r (default mode)  : To open the file in the read mode. Read mode is the default mode
Modes also should be given in the string format. 
If we try to open the file which is not present, read mode will give FileNotFoundError

2. write = w : Whenever we open the file in write mode, whatever the data we had
in the file will be completely lost.

3. append = a

4. create = x
'''

