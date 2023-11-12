def memoize(func):
    memo = {}
    def wrapper(n):
        if n not in memo:
            memo[n] = func(n)
        return memo[n]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
