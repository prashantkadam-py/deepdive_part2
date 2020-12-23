def coro():
    
    data = None
    while True:
        received = yield data
        data = f"received data : {received}"
       


def gen3():
    yield from coro()


def gen2():
    yield from gen3()


def gen1():
    yield from gen2()


if __name__ == "__main__":

    player = gen1()
    next(player)
    for i in range(1, 10):
        print(player.send(i))
