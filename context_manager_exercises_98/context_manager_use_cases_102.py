import decimal
from time import perf_counter, sleep
import sys

decimal.getcontext().prec = 14


class Precision:

    def __init__(self, prec):
        self.prec = prec
        self.global_prec = decimal.getcontext().prec 

    def __enter__(self):
        decimal.getcontext().prec = self.prec
        
    def __exit__(self, exc_type, exc_value, exc_tb):
        decimal.getcontext().prec = self.global_prec
        return False



class Timer:

    def __init__(self):
        self.elapsed = 0


    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.stop = perf_counter()
        self.elapsed = self.stop - self.start
        return False


class OutToFile:

    def __init__(self, fname):
        self.fname = fname
        self._current_stdout = sys.stdout

    def __enter__(self):
        self._file = open(self.fname, "w")
        sys.stdout = self._file

    def __exit__(self, exc_type, exc_error, exc_tb):
        sys.stdout = self._current_stdout
        self._file.close()
        return False



if __name__ == "__main__":
    print(decimal.Decimal(1) / decimal.Decimal(3))
    with Precision(3):
        print(decimal.Decimal(1) / decimal.Decimal(3))
    print(decimal.Decimal(1) / decimal.Decimal(3))

    with Timer() as timer:
        sleep(5)
        print(timer.elapsed)
    print(timer.elapsed)


    with OutToFile("test.txt"):
        print("Hello")
        print("World")





