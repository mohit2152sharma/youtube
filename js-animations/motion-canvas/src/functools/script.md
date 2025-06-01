In this video, I want to talk about functools and the functions this module provides and how they can help you write better functions.

Up first, we have cache. It's a decorator that caches the results of a function. When we use it with a function as a decorator, it automatically caches the function results.
The first call to factorial with 5 will take time because it computes all recursive calls. But subsequent calls return instantly from the cache as they have already been computed.

Next is cached property, it's the same as cache but for class properties.
When we have a class property (or attribute) with expensive property calculation the cached_property decorate ensures the computation happens only once. For example, here we have a Dataset class with an expensive mean property.
The first time I access the mean property, it triggers the calculation but subsequence accesses return the cached value immediately.

Next up we have lru_cache, it's like cache but with size limit. It has a maxsize parameter which prevents unlimited memory growth. Here we set maxsize to 3 for our fibonacci function. The cache keeps track of the 3 most recently used values, and we can inspect cache with cache_info and clear the cache manually when needed

next is partial. functools.partial creates new functions with some arguments pre-filled
Starting with a simple multiply function that takes three arguments
We can create a partial function 'double' with x pre-set to 2
Now double only needs two arguments instead of three
Similarly, triple_by_2 has both x and y pre-filled
This is useful for creating specialized functions from general ones

singledispatch. it creates function overloads based on the first argument's type
We start with a base function decorated with @singledispatch
Then use register decorator to register implementations for specific types
Each registered function handles a different type
When we call format_value, it automatically dispatches to the right implementation
Based on the type of the first argument
This provides type-based polymorphism in Python

like singledispatch, there is singledispatchmethod for class methods
We define a method with @singledispatchmethod
Then register implementations for different types
Each registered method handles a specific type
When we call the method, it dispatches based on the argument type

next up update wrapper, update_wrapper preserves the original function's metadata in wrapper functions
Here we have an original function with its own docstring
And a manual wrapper that calls the original
Without update_wrapper, the wrapper keeps its own metadata
After applying update_wrapper, the wrapper appears to be the original function
This preserves important metadata like function name and documentation

Finally, @functools.wraps is a convenient decorator for applying update_wrapper
Here we create a timer decorator that wraps functions
The @functools.wraps decorator preserves the original function's metadata
Without it, the wrapper would lose the original function's name and docstring
This is the standard way to create well-behaved decorators in Python
It ensures that decorated functions maintain their original identity
