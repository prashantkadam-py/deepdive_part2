import math

def factorial_gen(n):

    for num in range(n):
        yield math.factorial(num)


if __name__ == "__main__":
    fact = factorial_gen(10)
    for f in fact:
        print(f)
