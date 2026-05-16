
''("regular expression : special sequence of characters that uses a search pattern "
   "to find a string or set of string")""




# special sequences

#            \A      \z     \d   \D   \s    \S      \w    \W     \b      \B

# ------------------------------------------------------------------------------------------------------

# Meta_characters

#           \      []      ^        $        .       |      ?      *      +       {}       ()

# import re
# a='my name is mithilesh, my age is 35 years and i have learnt python 20 times'
# b=re.findall('[a-z]',a)
# print(b)

# import re
# a='my name is mithilesh, my age is 35 years and i have learnt python 20 times'
# b=re.findall('[^a-z]',a)
# print(b)
# o/p:[' ', ' ', ' ', ',', ' ', ' ', ' ', ' ', '3', '5', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '2', '0', ' ']

# import re
# a='my name is mithilesh, my age is 35 years and i have learnt python 20 times'
# b=re.findall('times$',a)
# print(b)
# o/p: ['times']

# b=re.findall('$times',a)
# print(b)
# o/p; []

# a='my name is mithilesh, my age is 35 years and i have learnt python 20 times'
# b=re.findall('my|have',a)
# print(b)

# ---------------functions--------------------------------------------------------------------------

# match()      -   check whether pattern starts with string
# fullmatch()  -   matches the entire string
# search()     -   finds first occurrence of pattern
# findall()    -   find all occurrence
# finditer()   -   find all matches with details
# sub()        -   replace matches with new string
# subn()       -   replace and count occurrence
# split()      -   split string based on pattern

# ------------------------------------------------------------------------------------------------------

# Quantifiers----------
# a                       exactly one a
# a+                      atleast one a
# a*                      any number of a,  including zero
# a?                      either zero or one
# a{m}                    exactly m number of a
# a{m,n}                  minimum number of a and maximum number of a

#---------------------------------------------------------------------------------------------------------

# import re

# a='my name is mithilesh, my age is 35 years and i have learnt python 20 times'
# b=re.match('my',a)
# print(b)

# a='my name is mithilesh, my age is 35 years and i have learnt python 20 times'
# b=re.search('my',a)
# print(b)

# a='my name is mithilesh, my age is 35 years and i have learnt python 20 times'
# b=re.findall('35',a)
# print(b)
#
# a='my name is mithilesh, my age is 35 years and i have learnt python 20 times'
# b=re.split(' ',a)
# print(b)

# a='my name is mithilesh, my age is 35 years and i have learnt python 20 times'
# b=re.sub("python","java", a)
# print(b)
