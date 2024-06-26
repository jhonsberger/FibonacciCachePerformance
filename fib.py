import time
from functools import lru_cache

def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

@lru_cache()
def fib1(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib1(n-1) + fib1(n-2)

# Timing fib without cache
start_time = time.time()
for i in range(25):
    fib(i)
noCacheTime = time.time() - start_time

# Timing fib with cache
start_time = time.time()
for i in range(25):
    fib1(i)
cacheTime = time.time() - start_time

print('Printing the Fibonacci sequence up to the 25th term: ')
print('Without lru_cache: ', noCacheTime)
print('With lru_cache: ', cacheTime)