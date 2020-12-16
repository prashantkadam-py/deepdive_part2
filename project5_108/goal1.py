import csv
from collections import namedtuple

def get_dialect(fname): 
    with open(fname, "r") as f:
        return csv.Sniffer().sniff(f.read(1000))



class FileParser:

    def __init__(self, fname):
        self._fname = fname


    def __enter__(self):
        self._f = open(self._fname, "r")
        self._reader = csv.reader(self._f, get_dialect(self._fname))
        headers = map(lambda column: column.lower(),  next(self._reader))
        self._nt = namedtuple("Data", headers)
        return self



    def __exit__(self, exc_type, exc_value, exc_tb):
        self._f.close()
        return False


    def __iter__(self):
        return self

    def __next__(self):
        if self._f.closed:
            raise StopIteration
        else:
            return self._nt(*next(self._reader))

if __name__ == "__main__":
    with FileParser("data/personal_info.csv") as data:
        for row in data:
            print(row)
            

