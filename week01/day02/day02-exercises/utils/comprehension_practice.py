"""List comprehension: squares of even numbers from 1-20"""

squares = [x**2 for x in range(0, 20, 2)]

"""Dict comprehension: character → ASCII code for "hello"""
char_codes = {char: ord(char) for char in "hello"}

"""Set comprehension: unique word lengths in a sentence"""
SENTENCE = "the quick brown fox jumps"
lengths = {len(word) for word in SENTENCE.split()}

"""Nested comprehension: multiplication table (1-5)"""
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
