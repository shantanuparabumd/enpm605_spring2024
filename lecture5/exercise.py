

# Exercise 1

def strong(original):
    """Decorator to wrap a string in <strong> tags.

    Args:
        original (function): function to be decorated
    """
    def wrap_strong():
        return '<strong>' + original() + '</strong>'
    return wrap_strong

def emphasis(original):
    """Decorator to wrap a string in <em> tags.

    Args:
        original (function): funtion to be decorated
    """
    def wrap_emphasis():
        return '<em>' + original() + '</em>'
    return wrap_emphasis

@strong
@emphasis
def greet():
    return 'Hello'

print(greet())  


# Exercise 2

def count_calls(original):
    calls = 0
    def wrap_count_calls():
        nonlocal calls
        calls += 1
        print("Function call made",calls,"times.")
        return original()
    
    return wrap_count_calls

@count_calls
def greet2():
    return 'Hello'

greet2()
greet2()
greet2()


# Exercise 3

# Import the partial function from the functools module
from functools import partial



def subtract(x,y):
    """Subtract y from x.

    Args:
        x (int): value to be subtracted from
        y (int): value to subtract

    Returns:
        int: subtracted value
    """
    return x - y


# Fix the value to be subtracted(y) to 3 and create a new function
less = partial(subtract, y=3)

print(less(7))
print(less(12))
print(less(20))
