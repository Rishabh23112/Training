"""List Quesitons"""

from typing import List


def merge_sorted(list1: List[int], list2: List[int]) -> List[int]:
    """Merge sorted list"""

    i = 0
    j = 0
    merged: List[int] = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    return merged + list1[i:] + list2[j:]


def chunk_list(items: List, size: int) -> List[list]:
    """Split the list into chunks of the given size"""
    result: List[list] = []

    for i in range(0, len(items), size):
        result.append(items[i : i + size])

    return result


def flatten(nested: List[list]) -> List:
    """Flatten one level"""
    result: List[list] = []

    for i in nested:
        result.extend(i)
    return result
