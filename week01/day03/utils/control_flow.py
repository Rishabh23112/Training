# Condition if/else/elif
def is_even(num: int) -> str:
    """Check if a number is even."""
    if num % 2 == 0:
        return "Even"
    elif num == 0:
        return "Zero"
    else:
        return "Odd"


# Ternary operator
def is_even_ternary(num: int) -> str:
    """Check if a number is even or odd."""
    return "Even" if num % 2 == 0 else "Odd"


# Truthy/falsy
def truthy_or_falsy(value: any) -> str:
    """Check if a value is truthy or falsy."""
    return "Truthy" if value else "Falsy"


# for Loop
def print_numbers(num: list[int]) -> None:
    """Print numbers using a for loop."""
    for i in num:
        print(i)


# break and else on a for loop
def find_number(num: list[int], target: int) -> None:
    """Demonstrate the else clause on a for loop."""
    for number in num:
        if number == target:
            print(f"Found {target}")
            break
    else:
        print(f"{target} not found.")


# continue
def print_odd_numbers(num: list[int]) -> None:
    """Print only odd numbers using continue."""
    for number in num:
        if number % 2 == 0:
            continue

        print(number)


# Comprehensions

# List comprehension: squares of even numbers from 1-20

squares = [x**2 for x in range(0, 20, 2)]

# Dict comprehension: character → ASCII code for "hello
char_codes = {char: ord(char) for char in "hello"}

# Set comprehension: unique word lengths in a sentence
SENTENCE = "the quick brown fox jumps"
lengths = {len(word) for word in SENTENCE.split()}

#    Nested comprehension: multiplication table (1-5
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]


# Exception Handling
def exception_handling(num: int) -> int:
    """Demonstrate exception handling."""
    try:
        result = 10 / num
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None
    else:
        print("Division successful.")
        return result
    finally:
        print("Execution completed.")


# Context Manager

# python automatically calls __enter__() and __exit__() methods when used with.
with open("/data/energy/hourly_prices.csv", "r") as f:
    data = f.read()
    print(data[:10])

f = open("/data/energy/hourly_prices.csv", "r")
f.__enter__()
try:
    data = f.read()
    print(data[:10])
finally:
    f.__exit__(exec_type=None, exc_value=None, traceback=None)


# early return: returning from the function as soon as we know the result.
def early_return(num: int) -> int:
    """Early return."""
    if num < 0:
        return 0
    return num
