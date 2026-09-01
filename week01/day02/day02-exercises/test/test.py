"""Test Cases for the list , dict, set, and string questions"""

from utils.dict_ques import invert_dict, merge_dicts
from utils.list_ques import chunk_list, flatten, merge_sorted
from utils.set_ques import common_elements, is_subset, unique_chars
from utils.string_ques import is_palindrome, reverse_words, title_case

# Dictionary
D1 = {"a": 1, "b": 2}
D2 = {"b": 99, "c": 4}
print(invert_dict(D1))
print(merge_dicts(D1, D2))


# List
L1 = [1, 2, 3]
L2 = [4, 5, 6]
L = [[1, 2], [3, 4]]

print(merge_sorted(L1, L2))
print(chunk_list(L1, 2))
print(flatten(L))


# String
S = "Madam"
S1 = "hello world"
print(is_palindrome(S))
print(reverse_words(S1))
print(title_case(S1))

# Sets
ST1 = [1, 2, 3]
ST2 = [2, 3]
print(common_elements(ST1, ST2))
ST = "aaaabcccc"
print(unique_chars(S))
SET1 = {1, 2, 3}
SET2 = {1, 2, 3, 4}

print(is_subset(SET1, SET2))
