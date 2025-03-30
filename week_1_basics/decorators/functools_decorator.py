from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Call started!')
        r = func(*args, **kwargs)
        print('Call Finished!')
        return r
    return wrapper

@decorator
def call(a: int) -> str:
    return str(a)

decorated = call

assert decorated(1) == '1'