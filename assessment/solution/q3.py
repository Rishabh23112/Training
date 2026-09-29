"""Write a small reusable piece of code that measures and prints how long a block of code takes to run, so you don’t have to manually add timing calls every time."""


import time
from contextlib import contextmanager


@contextmanager
def timer():
    start = time.perf_counter()

    yield

    end = time.perf_counter()
    print(f"Time taken: {end - start:.4f} seconds")

if __name__ == "__main__":
    with timer():
        print("running work...")
        time.sleep(0.5)


print(timer())
