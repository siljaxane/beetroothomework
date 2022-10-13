def do_twice(function):
    def wrapper_do_twice():
        function()
        function()
    return wrapper_do_twice

    
        
    