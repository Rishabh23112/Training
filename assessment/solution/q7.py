"""Implement the function below. It should rotate items to the right by k positions.

def rotate_list(items: list, k: int) -> list:
    ...
Example: rotate_list([1, 2, 3, 4, 5], 2) returns [4, 5, 1, 2, 3]."""


def rotate_list(items: list, k: int) -> list:
    """
    Return a new list with its elements rotated right by k positions.
    """
    if not items:
        return []

    k %= len(items)

    if k == 0:
        return items.copy()

    return items[-k:] + items[:-k]

items=[1,2,3,4,5]
k=1

print(rotate_list(items, k))