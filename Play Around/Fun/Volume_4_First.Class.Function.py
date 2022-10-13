

def say_hello(name):
    return f"Hello {name}"

say_hello("Chris")

def be_awesome(name):
    return f"Yo {name}, together we are awesome!"

say_hello

be_awesome
my_list = [say_hello, be_awesome]
my_list [0]

my_list[1]('Thomas')

def greet_bob(greeter_func):
    return greeter_func('Bob')


greet_bob

print(greet_bob(say_hello))
print(greet_bob(be_awesome))

# the two print statements above have a function 
# embedded in another function

