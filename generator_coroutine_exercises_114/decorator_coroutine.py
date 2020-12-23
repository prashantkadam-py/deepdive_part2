import math

def coroutine(gen_fn):
    
    def inner(*args, **kwargs):
        
        gen = gen_fn(*args, **kwargs)
        next(gen)
        return gen
    return inner


@coroutine
def power_up(p):
    result = None
    while True:
        received = yield result
        try:
            result = math.pow(received, p)
        except TypeError:
            result = None


if __name__ == "__main__":
    squares = power_up(2)
    for i in range(1, 11):
        print(f"{i} ** 2 = {squares.send(i)}")
