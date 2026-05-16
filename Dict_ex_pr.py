#
# """
# dicts_programs.py
# Top 30 Dictionary Programs — numbered 71..100
# Run as a script or import functions individually.
# """
#
# # 71. Count frequency of characters in string using dictionary
# def freq_chars_dict(s):
#     d = {}
#     for ch in s:
#         d[ch] = d.get(ch, 0) + 1
#     return d
#
# # 72. Count frequency of words in sentence
# def freq_words(s):
#     d = {}
#     for w in s.split():
#         d[w] = d.get(w, 0) + 1
#     return d
#
# # 73. Sort dictionary by keys (returns list of tuples)
# def sort_dict_by_keys(d):
#     return sorted(d.items(), key=lambda x: x[0])
#
# # 74. Sort dictionary by values
# def sort_dict_by_values(d):
#     return sorted(d.items(), key=lambda x: x[1])
#
# # 75. Merge two dictionaries (Python 3.5+ style)
# def merge_dicts(a, b):
#     res = a.copy()
#     res.update(b)
#     return res
#
# # 76. Invert dictionary {key: value -> value: key}
# def invert_dict(d):
#     return {v:k for k,v in d.items()}
#
# # 77. Check if key exists in dictionary
# def key_exists(d, key):
#     return key in d
#
# # 78. Get value safely without using get()
# def get_safe(d, key, default=None):
#     try:
#         return d[key]
#     except KeyError:
#         return default
#
# # 79. Remove key from dictionary without using pop()
# def remove_key(d, key):
#     if key in d:
#         new = d.copy()
#         del new[key]
#         return new
#     return d.copy()
#
# # 80. Convert two lists into dictionary
# def lists_to_dict(keys, values):
#     return dict(zip(keys, values))
#
# # 81. Convert dictionary to list of tuples
# def dict_to_tuples(d):
#     return list(d.items())
#
# # 82. Find key with max value
# def key_with_max_value(d):
#     return max(d, key=d.get) if d else None
#
# # 83. Find key with min value
# def key_with_min_value(d):
#     return min(d, key=d.get) if d else None
#
# # 84. Sum all dictionary values
# def sum_dict_values(d):
#     return sum(d.values())
#
# # 85. Filter dictionary by condition (values > threshold)
# def filter_dict_by_value(d, threshold):
#     return {k:v for k,v in d.items() if v > threshold}
#
# # 86. Create dictionary of word lengths
# def word_lengths(s):
#     return {w: len(w) for w in s.split()}
#
# # 87. Create nested dictionary dynamically from list of keys
# def nested_from_keys(keys, value):
#     out = current = {}
#     for k in keys[:-1]:
#         current[k] = {}
#         current = current[k]
#     current[keys[-1]] = value
#     return out
#
# # 88. Update multiple keys at once
# def update_multiple(d, updates):
#     res = d.copy()
#     res.update(updates)
#     return res
#
# # 89. Create dictionary from string (character: count)
# def char_count_dict(s):
#     return freq_chars_dict(s)
#
# # 90. Delete key-value pair if value is even
# def delete_if_value_even(d):
#     return {k:v for k,v in d.items() if v % 2 != 0}
#
# # 91. Check if two dictionaries are equal
# def dicts_equal(a, b):
#     return a == b
#
# # 92. Convert flat dictionary to nested (a.b.c : 10 -> {a:{b:{c:10}}})
# def flat_to_nested(d):
#     res = {}
#     for k, v in d.items():
#         parts = k.split('.')
#         cur = res
#         for p in parts[:-1]:
#             cur = cur.setdefault(p, {})
#         cur[parts[-1]] = v
#     return res
#
# # 93. Convert nested dictionary to flat (reverse of above)
# def nested_to_flat(d, parent_key=''):
#     items = {}
#     for k, v in d.items():
#         new_key = parent_key + '.' + k if parent_key else k
#         if isinstance(v, dict):
#             items.update(nested_to_flat(v, new_key))
#         else:
#             items[new_key] = v
#     return items
#
# # 94. Reverse dictionary maintaining list for duplicate values
# def reverse_dict_multivalue(d):
#     res = {}
#     for k, v in d.items():
#         res.setdefault(v, []).append(k)
#     return res
#
# # 95. Iterate dictionary without using .items() (yield key, value)
# def iterate_without_items(d):
#     for k in d:
#         yield k, d[k]
#
# # 96. Swap keys and values for specific keys (given a list)
# def swap_selected_keys(d, keys_to_swap):
#     res = d.copy()
#     for k in keys_to_swap:
#         if k in res:
#             val = res[k]
#             del res[k]
#             res[val] = k
#     return res
#
# # 97. Find all keys having the same value
# def keys_with_value(d, value):
#     return [k for k, v in d.items() if v == value]
#
# # 98. Remove items with None values
# def remove_none_values(d):
#     return {k:v for k,v in d.items() if v is not None}
#
# # 99. Create dictionary of number squares (1 to N)
# def squares_dict(n):
#     return {i: i*i for i in range(1, n+1)}
#
# # 100. Convert JSON-like string to dictionary manually (simple parser for flat JSON)
# def simple_json_to_dict(s):
#     import ast
#     try:
#         return ast.literal_eval(s)
#     except Exception:
#         # fallback: very simple parser for flat {"a":1,"b":"x"}
#         s = s.strip()
#         if s.startswith('{') and s.endswith('}'):
#             s = s[1:-1].strip()
#             if not s:
#                 return {}
#             parts = []
#             cur = ''
#             depth = 0
#             for ch in s:
#                 if ch == ',' and depth == 0:
#                     parts.append(cur)
#                     cur = ''
#                 else:
#                     cur += ch
#                     if ch in '"\'':
#                         pass
#                     elif ch == '{':
#                         depth += 1
#                     elif ch == '}':
#                         depth -= 1
#             if cur:
#                 parts.append(cur)
#             res = {}
#             for part in parts:
#                 k, v = part.split(':', 1)
#                 k = k.strip().strip('\'"')
#                 v = v.strip()
#                 try:
#                     val = ast.literal_eval(v)
#                 except Exception:
#                     val = v.strip('\'"')
#                 res[k] = val
#             return res
#         raise ValueError("Unsupported format")
#
# # Demo when run as script
# if __name__ == "__main__":
#     print("Freq chars 'banana' ->", freq_chars_dict("banana"))
#     print("Merge {'a':1} and {'b':2} ->", merge_dicts({'a':1}, {'b':2}))
#     print("Flat to nested {'a.b': 1} ->", flat_to_nested({'a.b':1}))
