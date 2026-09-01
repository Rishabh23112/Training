"""Frequencies, dedupe, group_by"""

from typing import Dict, List, Set


def frequencies(items: List[str]) -> Dict[str, int]:
    """Count the frequencies of the characters"""
    count: Dict[str, int] = {}
    for item in items:
        count[item] = count.get(item, 0) + 1
    return count


def dedupe(items: List[str]) -> List[str]:
    """Removed the duplicates"""

    unique: Set[str] = set()
    result: List[str] = []
    for item in items:
        if item not in unique:

            unique.add(item)
            result.append(item)
    return result


def group_by(items: List[Dict], key: str) -> Dict[str, List[Dict]]:
    """Mapping key values to the lists of items"""

    result: Dict[str, int] = {}
    for item in items:
        value = item[key]
        if value not in result:
            result[value] = []

        result[value].append(item)
    return result
