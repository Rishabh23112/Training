"""Dictionary Questions"""

from typing import Dict


def invert_dict(d: Dict[str, str]) -> Dict[str, str]:
    """Swap keys and values"""
    result: Dict[str, str] = {}

    for key, value in d.items():
        result[value] = key

    return result


def merge_dicts(*dicts: dict) -> dict:
    """Merge multiple dicts"""
    merged = {}
    for dictionary in dicts:
        merged.update(dictionary)
    return merged


# def filter_dict(d:dict, predicate)->Dict:
# Flagged - Wrong question
