from functools import wraps

def decorator_wrapper(arg1, arg2):
    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Call started! Arg1 = ' + str(arg1))
            r = func(*args, **kwargs) 
            print('Call finished! Arg2 = ' + str(arg2))
            return r
        return wrapper

    return real_decorator

@decorator_wrapper(1,2)
def call(a: int) -> str:
    return str(a)

decorated = call

assert decorated(1) == '1'