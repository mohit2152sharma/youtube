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
