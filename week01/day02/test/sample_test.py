from utils.collection_utils import frequencies,dedupe,group_by
from utils.text import clean_text,count_chars,tokenize

# Collection_utils.py test

S = ["a", "b", "a"]

items_Test = [{"status": "todo", "id": 1}, {"status": "done", "id": 2}]

print(frequencies(S))
print(dedupe(S))
print(group_by(items_Test, "status"))

# Text.py test

text_test = " Hello, WORLD!"

print(clean_text(text_test))
print(tokenize(text_test))
print(count_chars(text_test))