def decorator(call):
    def wrapper(*args, **kwargs):
        print('Call started!')
        r = call(*args, **kwargs)
        print('Call Finished!')
        return r

    return wrapper


def call(a: int) -> str:
    return str(a)


@decorator
def call2(a: int) -> str:
    return str(a)


decorated = decorated_call = decorator(call)
decorated2 = call2

assert decorated(1) == '1'
assert decorated2(1) == '1'
