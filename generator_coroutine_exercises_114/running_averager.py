def running_averager():
    total = 0
    count = 0
    average = None

    while True:
        print("calculate avg...")
        number = yield average
        total += number
        count += 1
        average = total / count


def running_averages(iterable):

    averager = running_averager()
    next(averager)
    for num in iterable:
        print(f"sending..{num}")
        average = averager.send(num)
        print(f"Average : {average}")


if __name__ == "__main__":
    running_averages([10, 20, 30, 40, 50])

