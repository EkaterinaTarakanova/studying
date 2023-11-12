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
