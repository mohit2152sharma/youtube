# Python functools Examples

This document provides easy-to-understand examples for all functions and decorators in Python's `functools` module.

## @functools.cache

Simple unlimited caching for expensive function calls.

```python
import functools
import time

@functools.cache
def expensive_calculation(n):
    """Simulates an expensive calculation"""
    print(f"Computing factorial of {n}...")
    time.sleep(0.1)  # Simulate expensive operation
    return n * expensive_calculation(n-1) if n > 1 else 1

# First call - computes all values
print(expensive_calculation(5))  # Takes ~0.5 seconds

# Subsequent calls - instant (cached)
print(expensive_calculation(3))  # Instant - already computed
print(expensive_calculation(5))  # Instant - cached result
```

## @functools.cached_property

Cache expensive property computations for class instances.

```python
import functools
import statistics

class DataSet:
    def __init__(self, numbers):
        self._data = tuple(numbers)
    
    @functools.cached_property
    def mean(self):
        """Expensive computation - only calculated once"""
        print("Calculating mean...")
        return statistics.mean(self._data)
    
    @functools.cached_property
    def stdev(self):
        """Another expensive computation"""
        print("Calculating standard deviation...")
        return statistics.stdev(self._data)

# Usage
dataset = DataSet([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(dataset.mean)   # Calculates and caches
print(dataset.mean)   # Returns cached value (no calculation)
print(dataset.stdev)  # Calculates and caches
```

## functools.cmp_to_key

Convert old-style comparison functions to key functions for sorting.

```python
import functools
import locale

def compare_strings_ignore_case(a, b):
    """Old-style comparison function"""
    a_lower = a.lower()
    b_lower = b.lower()
    if a_lower < b_lower:
        return -1
    elif a_lower > b_lower:
        return 1
    else:
        return 0

# Convert to key function for modern sorting
words = ['Apple', 'banana', 'Cherry', 'date']

# Using cmp_to_key to convert comparison function
sorted_words = sorted(words, key=functools.cmp_to_key(compare_strings_ignore_case))
print(sorted_words)  # ['Apple', 'banana', 'Cherry', 'date']

# More practical example with locale-aware sorting
names = ['José', 'André', 'François', 'Ångström']
try:
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    sorted_names = sorted(names, key=functools.cmp_to_key(locale.strcoll))
    print(sorted_names)
except locale.Error:
    print("Locale not available, using regular sort")
    print(sorted(names))
```

## @functools.lru_cache

Least Recently Used cache with size limit and statistics.

```python
import functools

@functools.lru_cache(maxsize=3)
def fibonacci(n):
    """Fibonacci with limited cache size"""
    print(f"Computing fib({n})")
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Calculate some fibonacci numbers
print(f"fib(10) = {fibonacci(10)}")
print(f"fib(8) = {fibonacci(8)}")   # Some values cached
print(f"fib(12) = {fibonacci(12)}")

# Check cache statistics
print(f"Cache info: {fibonacci.cache_info()}")

# Clear cache
fibonacci.cache_clear()
print("Cache cleared")
print(f"Cache info: {fibonacci.cache_info()}")

# Example with typed=True
@functools.lru_cache(maxsize=128, typed=True)
def add_numbers(a, b):
    print(f"Computing {a} + {b}")
    return a + b

add_numbers(1, 2)      # int + int
add_numbers(1.0, 2.0)  # float + float (different cache entry due to typed=True)
add_numbers(1, 2)      # Cached result
```

## functools.partial

Create partial function applications with pre-filled arguments.

```python
import functools

def multiply(x, y, z):
    """Simple multiplication function"""
    return x * y * z

# Create partial functions
double = functools.partial(multiply, 2)        # x=2, need y and z
triple_by_2 = functools.partial(multiply, 3, 2) # x=3, y=2, need z

print(double(5, 3))     # multiply(2, 5, 3) = 30
print(triple_by_2(4))   # multiply(3, 2, 4) = 24

# Practical example: pre-configured logging
import logging
functools.partial(logging.log, logging.DEBUG)

debug_log = functools.partial(logging.log, logging.DEBUG)
error_log = functools.partial(logging.log, logging.ERROR)

# More practical example: database operations
def query_database(connection, table, columns, where_clause=None):
    """Simulated database query function"""
    query = f"SELECT {columns} FROM {table}"
    if where_clause:
        query += f" WHERE {where_clause}"
    return f"Executing: {query} on {connection}"

# Create specialized query functions
users_db = functools.partial(query_database, "user_connection", "users")
products_db = functools.partial(query_database, "products_connection", "products")

print(users_db("name, email", "age > 18"))
print(products_db("*", "price < 100"))
```

## @functools.singledispatch

Create function overloads based on the first argument's type.

```python
import functools
from decimal import Decimal

@functools.singledispatch
def format_value(value):
    """Default implementation for unknown types"""
    return f"Unknown type: {type(value).__name__} = {value}"

@format_value.register(int)
def _(value):
    return f"Integer: {value:,}"

@format_value.register(float)
def _(value):
    return f"Float: {value:.2f}"

@format_value.register(str)
def _(value):
    return f"String: '{value}' (length: {len(value)})"

@format_value.register(list)
def _(value):
    return f"List with {len(value)} items: {value}"

@format_value.register(Decimal)
def _(value):
    return f"Decimal: {value}"

# Usage examples
print(format_value(42))           # Integer: 42
print(format_value(3.14159))      # Float: 3.14
print(format_value("hello"))      # String: 'hello' (length: 5)
print(format_value([1, 2, 3]))    # List with 3 items: [1, 2, 3]
print(format_value(Decimal('10.50')))  # Decimal: 10.50
print(format_value({"key": "value"}))  # Unknown type: dict = {'key': 'value'}

# Check which implementation will be used
print(f"Implementation for int: {format_value.dispatch(int)}")
print(f"All registered types: {list(format_value.registry.keys())}")
```

## functools.singledispatchmethod

Single dispatch for class methods.

```python
import functools

class Formatter:
    @functools.singledispatchmethod
    def format(self, value):
        """Default formatter"""
        return f"Default: {value}"
    
    @format.register
    def _(self, value: int):
        return f"Integer: {value:,}"
    
    @format.register
    def _(self, value: float):
        return f"Float: {value:.3f}"
    
    @format.register
    def _(self, value: str):
        return f"String: '{value.upper()}'"

# Usage
formatter = Formatter()
print(formatter.format(1000))      # Integer: 1,000
print(formatter.format(3.14159))   # Float: 3.142
print(formatter.format("hello"))   # String: 'HELLO'

# Example with classmethod
class Calculator:
    @functools.singledispatchmethod
    @classmethod
    def add(cls, x, y):
        return x + y
    
    @add.register
    @classmethod
    def _(cls, x: int, y: int):
        print(f"Adding integers: {x} + {y}")
        return x + y
    
    @add.register
    @classmethod
    def _(cls, x: str, y: str):
        print(f"Concatenating strings: '{x}' + '{y}'")
        return x + y

# Usage
print(Calculator.add(5, 3))        # Adding integers: 5 + 3 → 8
print(Calculator.add("hello", " world"))  # Concatenating strings: 'hello' + ' world' → hello world
```

## functools.update_wrapper

Update wrapper functions to look like the original function.

```python
import functools

def original_function():
    """This is the original function's docstring"""
    return "original result"

def manual_wrapper(*args, **kwargs):
    """Manual wrapper function"""
    print("Before calling original")
    result = original_function(*args, **kwargs)
    print("After calling original")
    return result

# Without update_wrapper
print(f"Wrapper name: {manual_wrapper.__name__}")
print(f"Wrapper doc: {manual_wrapper.__doc__}")

# Using update_wrapper
functools.update_wrapper(manual_wrapper, original_function)
print(f"After update_wrapper name: {manual_wrapper.__name__}")
print(f"After update_wrapper doc: {manual_wrapper.__doc__}")

# More practical example
def timing_decorator(func):
    """A decorator that times function execution"""
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    
    # Update wrapper to preserve original function metadata
    functools.update_wrapper(wrapper, func)
    return wrapper

@timing_decorator
def slow_function():
    """A function that takes some time"""
    import time
    time.sleep(0.1)
    return "done"

print(f"Function name: {slow_function.__name__}")
print(f"Function doc: {slow_function.__doc__}")
```

## @functools.wraps

Convenient decorator for applying update_wrapper.

```python
import functools
import time

def retry_decorator(max_attempts=3):
    """Decorator that retries a function on failure"""
    def decorator(func):
        @functools.wraps(func)  # Preserves original function metadata
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt + 1} failed: {e}")
                    if attempt < max_attempts - 1:
                        time.sleep(0.1 * (attempt + 1))  # Exponential backoff
            
            print(f"All {max_attempts} attempts failed")
            raise last_exception
        
        return wrapper
    return decorator

@retry_decorator(max_attempts=3)
def unreliable_function(should_fail=True):
    """A function that might fail"""
    import random
    if should_fail and random.random() < 0.7:
        raise ValueError("Random failure!")
    return "Success!"

# The wrapped function preserves original metadata
print(f"Function name: {unreliable_function.__name__}")
print(f"Function doc: {unreliable_function.__doc__}")
print(f"Original function: {unreliable_function.__wrapped__}")

# Test the retry behavior
try:
    result = unreliable_function(should_fail=True)
    print(f"Result: {result}")
except ValueError as e:
    print(f"Final failure: {e}")

# Example of logging decorator
def log_calls(func):
    """Decorator that logs function calls"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_calls
def calculate_area(length, width):
    """Calculate the area of a rectangle"""
    return length * width

calculate_area(5, 3)
print(f"Function metadata preserved: {calculate_area.__name__}, {calculate_area.__doc__}")
```

## Real-world Combined Example

Here's a more complex example showing multiple functools features working together:

```python
import functools
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self._session = None
    
    @functools.cached_property
    def session(self):
        """Expensive session creation - cached"""
        print("Creating HTTP session...")
        # Simulate expensive session creation
        time.sleep(0.1)
        return f"Session for {self.base_url}"
    
    @functools.lru_cache(maxsize=100)
    def _cached_request(self, endpoint, method="GET"):
        """Cache GET requests"""
        print(f"Making {method} request to {endpoint}")
        time.sleep(0.05)  # Simulate network delay
        return f"Response from {endpoint}"
    
    @functools.singledispatchmethod
    def process_response(self, data):
        """Default response processor"""
        return f"Processed: {data}"
    
    @process_response.register
    def _(self, data: dict):
        return f"JSON data with {len(data)} keys"
    
    @process_response.register
    def _(self, data: str):
        return f"Text data: {data[:50]}..."

# Usage
client = APIClient("https://api.example.com")

# Cached property in action
print(client.session)  # Creates session
print(client.session)  # Returns cached session

# Cached requests
response1 = client._cached_request("/users")
response2 = client._cached_request("/users")  # Cached

# Single dispatch processing
print(client.process_response({"users": [1, 2, 3]}))
print(client.process_response("Long text response..."))

print(f"Request cache info: {client._cached_request.cache_info()}")
```

This demonstrates how functools can be used together to create efficient, well-structured code with caching, method dispatch, and proper function metadata preservation.
