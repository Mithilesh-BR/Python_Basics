'''Defaultdict in Python

defaultdict is a special type of dictionary from the built-in module:👉 collections
It automatically provides a default value for a key that does not exist.

So it avoids this common error: key error'''

# ----> Why Normal Dictionary Fails
# data = {}
#
# data["a"] += 1   # ❌ KeyError because "a" doesn't exist
#
# ----->  Using defaultdict
from collections import defaultdict

data = defaultdict(int)

data["a"] += 1
print(data)

# ------------------------------------------------------------------------------

from collections import defaultdict

# s="aaeadseadeadea"
# res=defaultdict(int)
# for i in s:
#     res[i]+=1
# print(res)


# l=[54,88,77,45,43,23,22]
# res=defaultdict(list)
# for i in l:
#     res[i%2] += [i]
# print(res)
#
#
# files=["python.py","loops.doc","string.txt","tuple.py","list.doc","programs.txt"]
# res=defaultdict(tuple)
# for i in files:
#     val,key = i.split(".")
#
#     res[key] += (val,)
# print(res)
