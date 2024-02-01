"""Write a decorator which wraps functions to log function
arguments and the return value on each call.
Provide sypport for both positional and named 
arguments(your wrapper function should take both 
*args and **kwargs and print them both)
"""

# As a class

class logged:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):


        print('you called {.__name__}({}{}{})'.format(
            self.func,
            str(list(args))[1:-1],
            ',' if kwargs else '',
            ',' .join('{}={}'.format(*pair) for pair in kwargs.items()),
        ))
        val = self.func(*args, **kwargs)
        print('it returned', val)
        return val
    
#As a function:
    
# def logged(func):
#     """Print out the arguments before function call 
#     and after the call print out the returned value"""
#     def wrapper(*args,**kwargs):
#         print('you called {.__name__}({}{}{})'.format(
#             func,
#             str(list(args))[1:-1],
#             ',' if kwargs else '',
#             ',' .join('{}={}'.format(*pair) for pair in kwargs.items()),
#         ))
#         val = func(*args, **kwargs)
#         print('it returned' ,val)
#         return val
#     return wrapper


@logged
def func(*args):
    return 3+len(args)
func(7,8,9)


"""Long version with doctests and improved introspection"""

import functools


def logged(func):
   """Print out the arguments before function call and
   after the call print out the returned value"""


   def wrapper(*args, **kwargs):
        print('you called {.__name__}({}{}{})'.format(
        func,
        str(list(args))[1:-1], # cast to list because tuple
        # of length one has an extra comma
        ', ' if kwargs else '',
        ', '.join('{}={}'.format(*pair) for pair in kwargs.items()),
        ))

        val = func(*args, **kwargs)
        print('This function returned', val)
        return val
   
   return functools.update_wrapper(wrapper, func)


@logged
def func(*args):
    return 3 + len(args)

func(4, 4, 4)

@logged
def func2(a=None, b=None):
    return None

func2()

func2(3, b=2)

@logged
def func3():
    "this function is documented"
    pass

print(func3.__doc__)