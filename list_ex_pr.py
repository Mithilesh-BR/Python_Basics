#
# """
# lists_programs.py
# Top 35 List Programs — numbered 36..70
# Run as a script or import functions individually.
# """
#
# # 36. Sum of all elements in a list (manual loop)
# def sum_list(lst):
#     total = 0
#     for x in lst:
#         total += x
#     return total
#
# # 37. Find largest number in list
# def largest_in_list(lst):
#     if not lst: return None
#     maxv = lst[0]
#     for x in lst:
#         if x > maxv: maxv = x
#     return maxv
#
# # 38. Find smallest number in list
# def smallest_in_list(lst):
#     if not lst: return None
#     minv = lst[0]
#     for x in lst:
#         if x < minv: minv = x
#     return minv
#
# # 39. Remove duplicates from list (preserve order)
# def remove_duplicates(lst):
#     seen = set()
#     out = []
#     for x in lst:
#         if x not in seen:
#             seen.add(x)
#             out.append(x)
#     return out
#
# # 40. Count frequency of elements in list
# def freq_list(lst):
#     d = {}
#     for x in lst:
#         d[x] = d.get(x, 0) + 1
#     return d
#
# # 41. Reverse list without using reverse() or slicing
# def reverse_list_manual(lst):
#     out = []
#     i = len(lst)-1
#     while i >= 0:
#         out.append(lst[i])
#         i -= 1
#     return out
#
# # 42. Sort list without using sort() (bubble sort)
# def bubble_sort(lst):
#     a = lst[:]
#     n = len(a)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#     return a
#
# # 43. Merge two lists
# def merge_lists(a, b):
#     return a + b
#
# # 44. Find common elements between two lists
# def common_elements(a, b):
#     return list(set(a) & set(b))
#
# # 45. Find difference of two lists (a - b)
# def difference_lists(a, b):
#     return [x for x in a if x not in b]
#
# # 46. Separate even and odd numbers from list
# def separate_even_odd(lst):
#     ev = [x for x in lst if isinstance(x, int) and x%2==0]
#     od = [x for x in lst if isinstance(x, int) and x%2!=0]
#     return ev, od
#
# # 47. Create list of squares of numbers
# def squares(n):
#     return [i*i for i in range(1, n+1)]
#
# # 48. Check if list is sorted (ascending)
# def is_sorted(lst):
#     return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
#
# # 49. Rotate list by K positions (left rotate)
# def rotate_list(lst, k):
#     if not lst: return lst
#     k = k % len(lst)
#     return lst[k:] + lst[:k]
#
# # 50. Find second largest element
# def second_largest(lst):
#     s = sorted(set(lst))
#     return s[-2] if len(s) >= 2 else None
#
# # 51. Find N largest elements
# def n_largest(lst, n):
#     return sorted(lst, reverse=True)[:n]
#
# # 52. Split list into chunks of N elements
# def chunks(lst, n):
#     return [lst[i:i+n] for i in range(0, len(lst), n)]
#
# # 53. Flatten nested list (one level)
# def flatten_once(lst):
#     out = []
#     for item in lst:
#         if isinstance(item, list):
#             out.extend(item)
#         else:
#             out.append(item)
#     return out
#
# # 54. Remove empty lists from nested list
# def remove_empty_sublists(lst):
#     return [x for x in lst if not (isinstance(x, list) and len(x)==0)]
#
# # 55. Find duplicates in list
# def find_duplicates(lst):
#     from collections import Counter
#     return [k for k, v in Counter(lst).items() if v > 1]
#
# # 56. Print elements at even index & odd index
# def split_by_index_parity(lst):
#     even_idx = [lst[i] for i in range(0, len(lst), 2)]
#     odd_idx = [lst[i] for i in range(1, len(lst), 2)]
#     return even_idx, odd_idx
#
# # 57. Count positive & negative numbers
# def count_pos_neg(lst):
#     pos = sum(1 for x in lst if isinstance(x, (int, float)) and x > 0)
#     neg = sum(1 for x in lst if isinstance(x, (int, float)) and x < 0)
#     return pos, neg
#
# # 58. Pair each element of two lists (like zip) — returns list of tuples
# def pair_elements(a, b):
#     return list(zip(a, b))
#
# # 59. Convert list of strings to integers
# def list_str_to_int(lst):
#     return [int(x) for x in lst]
#
# # 60. Compute dot product of two lists
# def dot_product(a, b):
#     return sum(x*y for x, y in zip(a, b))
#
# # 61. Replace an element at specific index
# def replace_at_index(lst, idx, val):
#     a = lst[:]
#     if -len(a) <= idx < len(a):
#         a[idx] = val
#     return a
#
# # 62. Insert element without using insert() (at index)
# def insert_manual(lst, idx, val):
#     return lst[:idx] + [val] + lst[idx:]
#
# # 63. Delete element without using del (by value)
# def delete_by_value(lst, val):
#     return [x for x in lst if x != val]
#
# # 64. Create list from user input (split manually)
# def list_from_input(s, sep=','):
#     return [item.strip() for item in s.split(sep)]
#
# # 65. Find all pairs in list whose sum equals K
# def pairs_with_sum(lst, k):
#     seen = set()
#     pairs = []
#     for x in lst:
#         if k-x in seen:
#             pairs.append((k-x, x))
#         seen.add(x)
#     return pairs
#
# # 66. Remove None values from list
# def remove_none(lst):
#     return [x for x in lst if x is not None]
#
# # 67. Find the product of all list elements
# def product_of_list(lst):
#     prod = 1
#     for x in lst:
#         prod *= x
#     return prod
#
# # 68. Check if two lists are permutations of each other
# def are_permutations(a, b):
#     from collections import Counter
#     return Counter(a) == Counter(b)
#
# # 69. Get unique elements in same order
# def unique_in_order(lst):
#     seen = set()
#     out = []
#     for x in lst:
#         if x not in seen:
#             seen.add(x)
#             out.append(x)
#     return out
#
# # 70. Reverse every sublist inside a nested list
# def reverse_sublists(lst):
#     return [sub[::-1] if isinstance(sub, list) else sub for sub in lst]
#
# # If run as script, demo some functions
# if __name__ == "__main__":
#     print("Sum [1,2,3] ->", sum_list([1,2,3]))
#     print("Second largest [1,4,2,4] ->", second_largest([1,4,2,4]))
#     print("Pairs with sum 5 in [1,2,3,4] ->", pairs_with_sum([1,2,3,4], 5))
