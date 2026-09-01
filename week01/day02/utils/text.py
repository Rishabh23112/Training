"""Clean Text, Tokenize, Count Chars"""

from typing import Dict, List


def clean_text(s: str) -> str:
    """Normalized lowercase string with single spaces and trimmed ends"""

    return "".join(s.strip().lower().split())


def tokenize(s: str, delimiter: str = " ") -> List[str]:
    """List of word tokens split on delimiter"""

    return s.split(delimiter)


def count_chars(s: str) -> Dict[str, int]:
    """Count the frequencies of the characters"""

    count: Dict[str, int] = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    return count



