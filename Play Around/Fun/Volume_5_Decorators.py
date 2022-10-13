

# A simple decorator:
def name_of_function(original_function):
    def name_of_wrapper_function():
        return original_function()
    return name_of_wrapper_function

# Continuing on above function
def show_this_function():
    print('This function ran')

show_function = name_of_function(show_this_function)

show_function()

# A simple decorator (V2):
def my_decorator(function):
    def wrapper():
        print("Something is happening before the function is called.")
        function()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee) # This is the 'decoration'
# So, what is happening above is that you take the original function
# called, my_decorator, and apply another function as its argument. 
# Then you assign this to a variable

# Essentially, you need to create these two functions well enough so 
# they can be applied in decorators. 

# The name, say_whee, exists / is connected to the 'wrapper()' function.

###

# You can also make the decorators easier - by using the 
# pie syntax. Shown as '@', where instead of saying/coding:

# say_whee = my_decorator(say_whee)

# You can do the below:

@my_decorator
def say_whee():
    print('Whee!')

from Volume_6_Decoratorfile import do_twice

@do_twice
def say_whee():
    print("Whee!")