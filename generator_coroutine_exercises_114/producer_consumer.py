from collections import deque


def produce_elements(dq, n):
    for i in range(1, n):
        dq.appendleft(i)
        print(f"produced - {i}")
        if len(dq) == dq.maxlen:
            print("queue full - yielding control")
            yield

def consume_elements(dq):
    while True:
        #if len(dq) > 0:
        #    print("consuming", dq.pop())
        #else:
        #    yield
        while len(dq) > 0:
            print("consuming", dq.pop()) 
        print("queue empty - yielding control")
        yield

def coordinator(n):

    dq = deque(maxlen=10)
    producer = produce_elements(dq, n)
    consumer = consume_elements(dq)
    while True:
        try:
            print("producing....")
            next(producer)
        except StopIteration:
            break
        finally:
            print("consuming....")
            next(consumer)

if __name__ == "__main__":
    coordinator(30)



