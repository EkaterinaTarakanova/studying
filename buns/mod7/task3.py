import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.6f} seconds to run.")
        return result
    return wrapper

def validate_args(func):
    def wrapper(*args):
        if len(args) < 1:
            return 'Not enough arguments'
        elif len(args) > 1:
            return 'Too many arguments'
        elif not isinstance(args[0], int):
            return 'Wrong argument type'
        elif args[0] < 0:
            return 'Negative argument'
        return func(*args)
    return wrapper

def memoize(func):
    memo = {}
    def wrapper(n):
        if n not in memo:
            memo[n] = func(n)
        return memo[n]
    return wrapper

@timer
@validate_args
@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


