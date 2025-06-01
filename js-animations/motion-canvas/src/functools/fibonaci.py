import functools


@functools.lru_cache(maxsize=3)
def fibonacci(n):
    """Fibonacci with limited cache size"""
    print(f"Computing fib({n})")
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Calculate some fibonacci numbers
print(f"fib(10) = {fibonacci(10)}")
print(f"fib(8) = {fibonacci(8)}")  # Some values cached
print(f"fib(12) = {fibonacci(12)}")

# Check cache statistics
print(f"Cache info: {fibonacci.cache_info()}")

# Clear cache
fibonacci.cache_clear()
