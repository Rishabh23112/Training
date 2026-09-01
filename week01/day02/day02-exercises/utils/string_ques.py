"""String Questions"""

from typing import List


def is_palindrome(s: str) -> bool:
    """Removed spaces and ignored cases and checked palindrome."""
    original = s.replace(" ", "").lower()
    return original == original[::-1]


def reverse_words(s: str) -> str:
    """Reversed the word order."""
    words = s.split()
    return " ".join(words[::-1])


def title_case(s: str) -> str:
    """Title case without using title."""
    words = s.split()
    result: List[str] = []

    for word in words:
        result.append(word[0].upper() + word[1:].lower())

    return " ".join(result)
