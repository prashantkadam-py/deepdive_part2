import math

def coroutine(gen_fn):

    def inner(*args, **kwargs):
        gen = gen_fn(*args, **kwargs)
        next(gen)
        return gen
    return inner


@coroutine
def handle_data():
    while True:
        received = yield
        print(received)

@coroutine
def power_up(n, gen_fn):
    while True:
        received = yield 
        result = math.pow(received, n)
        gen_fn.send(result)

@coroutine
def filter_even(gen_fn):
    while True:
        received = yield
        if received % 2 == 0:
            gen_fn.send(received)


def caller():
    print_data = handle_data()
    filtered_data = filter_even(print_data)
    gen2 = power_up(3, filtered_data)
    gen1 = power_up(2, gen2)
    
    for i in range(1, 6):
        #print(i)
        gen1.send(i)

if __name__ == "__main__":
    caller()

