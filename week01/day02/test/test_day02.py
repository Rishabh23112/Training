import unittest

from utils.collection_utils import dedupe, frequencies, group_by
from utils.text import clean_text, count_chars, tokenize


class TestTextUtils(unittest.TestCase):
    def test_clean_text(self):
        self.assertEqual(clean_text("  HELLO  "), "hello")

    def test_tokenize(self):
        self.assertEqual(tokenize("Hello World"), ["Hello", "World"])

    def test_count_chars(self):
        self.assertEqual(count_chars("Hello"), {"H": 1, "e": 1, "l": 2, "o": 1})


class TestCollections(unittest.TestCase):
    def test_frequencies(self):
        self.assertEqual(frequencies(["a", "b", "a"]), {"a": 2, "b": 1})


if __name__ == "__main__":
    unittest.main()
