from contextlib import contextmanager
import csv
from collections import namedtuple


def get_dialect(fname):
    with open(fname, "r") as f:
        return csv.Sniffer().sniff(f.read(1000))


def parsed_data_iter(data_iter, nt):
    for row in data_iter:
        yield nt(*row)

@contextmanager
def parsed_data(fname):
    f = open(fname, "r")
    try:
        reader = csv.reader(f, get_dialect(fname))
        headers = map(lambda column: column.lower(), next(reader))
        nt = namedtuple("Data", headers)
        yield parsed_data_iter(reader, nt)
    finally:
        f.close()

if __name__ == "__main__":
    with parsed_data("data/personal_info.csv") as data:
        for row in data:
            print(row)
