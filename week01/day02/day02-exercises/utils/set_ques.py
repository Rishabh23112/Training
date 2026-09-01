"""Set Questions"""

from typing import Set


def common_elements(list1: list, list2: list) -> Set:
    """Intersection of two lists."""
    return set(list1) & set(list2)


def unique_chars(s: str) -> Set[str]:
    """Unique characters in a string."""
    return set(s)


def is_subset(set1: set, set2: set) -> bool:
    """checked if set1 is a subset of set2 or not."""
    return set1.issubset(set2)
