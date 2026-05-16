
# '''Normal copy'''
#
# A=[1,2,3,4]
# B=[5,6,7,8]
#
# print(id(A))
# print(id(B))
#
#
# A=B
#
# print(A)
# print(B)
#
# print(id(A))
# print(id(B))
# ----------------------------------------------------------
'''shallow copy'''
#
# A = [1, 2, 3, [4, 5]]
# B=A.copy()
# #
# print(id(A))
# print(id(B))
#
# print(A)
# print(B)
#
# print(id(A))
# print(id(B))
#
# A.append(50)
# print(A)
# print(B)
#
# print(id(A))
# print(id(B))

'''deepcopy'''

# from copy import deepcopy
#
# a = [1, 2, 3, [4, 5]]
# b = deepcopy(a)
#
# print(id(a))
# print(id(b))
#
# a[3][0] = 100
# print(a)        #[1, 2, 3, [100, 5]]
# print(b)        #[1, 2, 3, [4, 5]]
#
# print(id(a))
# print(id(b))

# A=[1,2,3,4]
# B=deepcopy(A)
#
# print(id(A))
# print(id(B))

# A=copy.deepcopy(B)

# -------------------------------------------

# a = [1, 2, 3, 4, 5]
# b = a[:]
# print(id(a))
# print(id(b))
#
# a[0] = 100
# print(a)
# print(b)
#
# print(id(a))
# print(id(b))
#
# a = [1, 2, 3, [4, 5]]
# b = a[:]
# print(b)        #[1, 2, 3, [4, 5]]
#
# print(id(a))
# print(id(b))
#
# print(id(a[3]))
# print(id(b[3]))
#
# a[3][0] = 400
# print(a)
# print(b)
#
# print(id(a))
# print(id(b))
#
# print(id(a[3]))
# print(id(b[3]))