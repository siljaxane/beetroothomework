# Write a decorator that prints a function with arguments passed to it.

# NOTE! It should print the function, not the result of its execution!

# For example:
# "add called with 4, 5"

def main_decorator(function):
    def wrap(*args, **kwargs):
        function(*args, **kwargs)
        return function(*args, **kwargs)
    return wrap

def green_decorator(colour='green'):
    print(f'The leaf is {colour}')

green_decorator = main_decorator(green_decorator)

print(green_decorator)
    





























