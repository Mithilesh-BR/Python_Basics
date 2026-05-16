#
# """
# strings_programs.py
# Top 35 String Programs — numbered 1..35
# Run as a script or import functions individually.
# """
#
# # 1. Reverse a string without slicing
# # def reverse_no_slice(s):
# #     return ''.join(reversed(s))
#
# # 2. Count vowels and consonants in a string
# def count_vowels_consonants(s):
#     vowels = set("aeiouAEIOU")
#     v = c = 0
#     for ch in s:
#         if ch.isalpha():
#             if ch in vowels: v += 1
#             else: c += 1
#     return v, c
#
# # 3. Check if a string is palindrome
# def is_palindrome(s):
#     t = ''.join(ch.lower() for ch in s if ch.isalnum())
#     return t == t[::-1]
#
# # 4. Count occurrences of a character in a string
# def char_count(s, ch):
#     return sum(1 for c in s if c == ch)
#
# # 5. Remove all special characters from a string
# def remove_special(s):
#     return ''.join(ch for ch in s if ch.isalnum() or ch.isspace())
#
# # 6. Find frequency of each character
# def freq_chars(s):
#     d = {}
#     for ch in s:
#         d[ch] = d.get(ch, 0) + 1
#     return d
#
# # 7. Replace all spaces with hyphens
# def spaces_to_hyphens(s):
#     return s.replace(' ', '-')
#
# # 8. Find longest word in a string
# def longest_word(s):
#     words = s.split()
#     return max(words, key=len) if words else ''
#
# # 9. Count number of words in a sentence
# def word_count(s):
#     return len(s.split())
#
# # 10. Remove duplicate characters (preserve order)
# def remove_duplicates_preserve(s):
#     seen = set()
#     out = []
#     for ch in s:
#         if ch not in seen:
#             seen.add(ch)
#             out.append(ch)
#     return ''.join(out)
#
# # 11. Print all substrings of a string (returns list)
# def all_substrings(s):
#     return [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
#
# # 12. Check if two strings are anagrams
# def are_anagrams(a, b):
#     return sorted(a.replace(" ", "").lower()) == sorted(b.replace(" ", "").lower())
#
# # 13. Convert string to title case without .title()
# def to_title_case(s):
#     return ' '.join(w[0].upper()+w[1:].lower() if w else '' for w in s.split(' '))
#
# # 14. Remove leading and trailing spaces manually
# def strip_manual(s):
#     start, end = 0, len(s)-1
#     while start <= end and s[start].isspace():
#         start += 1
#     while end >= start and s[end].isspace():
#         end -= 1
#     return s[start:end+1]
#
# # 15. Check if string contains only digits
# def is_numeric(s):
#     return s.isdigit()
#
# # 16. Find ASCII value of each character
# def ascii_values(s):
#     return [ord(ch) for ch in s]
#
# # 17. Swap cases without using .swapcase()
# def swap_cases_manual(s):
#     out = []
#     for ch in s:
#         if ch.islower(): out.append(ch.upper())
#         elif ch.isupper(): out.append(ch.lower())
#         else: out.append(ch)
#     return ''.join(out)
#
# # 18. Find first repeated character
# def first_repeated_char(s):
#     seen = set()
#     for ch in s:
#         if ch in seen: return ch
#         seen.add(ch)
#     return None
#
# # 19. Find first non-repeated character
# def first_non_repeated_char(s):
#     from collections import Counter
#     c = Counter(s)
#     for ch in s:
#         if c[ch] == 1: return ch
#     return None
#
# # 20. Extract numbers from string
# def extract_numbers(s):
#     import re
#     return re.findall(r'\d+', s)
#
# # 21. Remove vowels from a string
# def remove_vowels(s):
#     vowels = set("aeiouAEIOU")
#     return ''.join(ch for ch in s if ch not in vowels)
#
# # 22. Count uppercase and lowercase letters
# def count_case(s):
#     up = sum(1 for ch in s if ch.isupper())
#     low = sum(1 for ch in s if ch.islower())
#     return up, low
#
# # 23. Sort characters in alphabetical order
# def sort_chars(s):
#     return ''.join(sorted(s))
#
# # 24. Check if string starts and ends with same character
# def starts_ends_same(s):
#     if not s: return False
#     return s[0] == s[-1]
#
# # 25. Reverse order of words in a sentence
# def reverse_words(s):
#     return ' '.join(s.split()[::-1])
#
# # 26. Print string in zig-zag format (returns list of rows)
# def zigzag(s, num_rows=3):
#     if num_rows == 1: return [s]
#     rows = [''] * min(num_rows, len(s))
#     cur, down = 0, True
#     for ch in s:
#         rows[cur] += ch
#         if cur == 0: down = True
#         elif cur == num_rows-1: down = False
#         cur += 1 if down else -1
#     return rows
#
# # 27. Find common characters between two strings
# def common_chars(a, b):
#     return set(a) & set(b)
#
# # 28. Find uncommon characters between two strings
# def uncommon_chars(a, b):
#     return set(a) ^ set(b)
#
# # 29. Split string without using .split()
# def split_manual(s, sep=' '):
#     parts = []
#     cur = ''
#     i = 0
#     ln = len(s)
#     while i < ln:
#         if s[i:i+len(sep)] == sep:
#             parts.append(cur)
#             cur = ''
#             i += len(sep)
#             continue
#         cur += s[i]
#         i += 1
#     parts.append(cur)
#     return parts
#
# # 30. Join list of characters into string without .join()
# def join_manual(lst, sep=''):
#     out = ''
#     for i, item in enumerate(lst):
#         out += str(item)
#         if i != len(lst)-1:
#             out += sep
#     return out
#
# # 31. Check if string contains substring (manual)
# def contains_substring(s, sub):
#     n, m = len(s), len(sub)
#     for i in range(n-m+1):
#         if s[i:i+m] == sub:
#             return True
#     return False
#
# # 32. Remove consecutive duplicate characters
# def remove_consecutive_duplicates(s):
#     if not s: return s
#     out = [s[0]]
#     for ch in s[1:]:
#         if ch != out[-1]:
#             out.append(ch)
#     return ''.join(out)
#
# # 33. Maximum occurring character in a string
# def max_occurring_char(s):
#     from collections import Counter
#     c = Counter(s)
#     return max(c, key=c.get)
#
# # 34. Check if string is an isogram (no repeating letters)
# def is_isogram(s):
#     s = s.replace(' ', '').lower()
#     return len(set(s)) == len(s)
#
# # 35. Convert Roman numeral to integer
# def roman_to_int(s):
#     vals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
#     i = 0
#     total = 0
#     while i < len(s):
#         if i+1 < len(s) and vals[s[i]] < vals[s[i+1]]:
#             total += vals[s[i+1]] - vals[s[i]]
#             i += 2
#         else:
#             total += vals[s[i]]
#             i += 1
#     return total
#
# # If run as script, simple demos
# if __name__ == "__main__":
#     print("Reverse 'python' ->", reverse_no_slice("python"))
#     print("Is 'Madam' palindrome?", is_palindrome("Madam"))
#     print("Extract numbers from 'a1b2c33' ->", extract_numbers("a1b2c33"))
