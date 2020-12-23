def subgen():
    try:
        received = yield
        print(received)
    finally:
        print("subgen closing.....")
        return "returned"


def delegator():
    s = subgen()
    yield from s
    yield "delegator subgen closed"
    print("delegator closing")



if __name__ == "__main__":
    d = delegator()
    next(d)

    d.send(100)

    d.close()

    d = delegator()
    next(d)
    try:
        d.send(200)
        d.throw(GeneratorExit, "exit")
    except StopIteration as ex:
        print("returned value : ", ex.value)
