from time import perf_counter, sleep
from contextlib import contextmanager

class GenContextManager:

    def __init__(self, gen):
        self.gen = gen


    def __enter__(self):
        print("calling next to get the yielded value from generator...")
        return next(self.gen)

    
    def __exit__(self, exc_type, exc_value, exc_tb):
        try:
            next(self.gen)
        except StopIteration:
            pass
        return False


def context_manager_dec(gen_fn):
    def helper(*args, **kwargs):
        gen = gen_fn(*args, **kwargs)
        ctx = GenContextManager(gen)
        return ctx
    return helper

@context_manager_dec
def open_file(fname, mode='r'):
    print("opening file...")
    f = open(fname, mode)
    try:
        yield f
    finally:
        print("closing file")
        f.close()

@contextmanager
def timer():
    stats = dict()
    start = perf_counter()
    stats["start"] = start
    try:
        yield stats
    finally:
        end = perf_counter()
        stats["end"] = end
        stats["elapsed"] = end - start



if __name__ == "__main__":
    with open_file("test.txt", "r") as f:
        print(f.readlines())
    
    with timer() as stats:
        sleep(2)
    print(stats)
