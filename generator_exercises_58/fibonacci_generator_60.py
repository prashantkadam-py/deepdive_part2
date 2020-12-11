def fib(n):
    fib_0 = 1
    yield fib_0
    fib_1 = 1
    yield fib_1
    for i in range(n-1):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
        yield fib_1


if __name__ == "__main__":
    fib_gen = fib(7)
    for num in fib_gen:
        print(num)
