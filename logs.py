import functools

def logged(func):
    """Print out the arguments before function call and
    after the call print out the returned value"""
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result

    return wrapper

@logged
def my_function(*args):
    return 3 + len(args)

# Test the decorated function
result = my_function(1, 2, 3)
print("Result:", result)
