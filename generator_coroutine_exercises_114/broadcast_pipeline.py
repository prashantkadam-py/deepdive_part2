import csv
from contextlib import contextmanager

input_file = "data/cars.csv"
converters = (str, str, int, str, str)
headers = ("make", "model", "year", "yin", "color")
idx_make, idx_model, idx_year, idx_vin, idx_color = 0, 1, 2, 3, 4

def data_reader(fname):
    
    with open(fname, "r") as f:
        dialect = csv.Sniffer().sniff(f.read(2000))
        f.seek(0)
        yield from csv.reader(f, dialect = dialect)


def data_parser():

    data = data_reader(input_file)
    next(data)
    for row in data:
        parsed_row = [
                        converter(item) 
                        for converter, item in zip(converters, row)
                        ]
        yield parsed_row



def coroutine(gen_fn):
    
    def inner(*args, **kwargs):
        g = gen_fn(*args, **kwargs)
        next(g)
        return g
    return inner

@coroutine
def save_data(fname, headers):
    
    with open(fname, "w", newline="") as f:
        writer = csv.writer(f) 
        writer.writerow(headers)
        while True:
            data_row = yield
            writer.writerow(data_row)

@coroutine
def filter_data(filter_predicate, target):
    while True:
        data_row = yield
        if filter_predicate(data_row):
            target.send(data_row)

@coroutine
def broadcast(targets):
    while True:
        data_row = yield
        for target in targets:
            target.send(data_row)


@coroutine
def pipeline_coro():
    out_pink_cars = save_data("data/pink_cars.csv", headers)
    out_ford_green = save_data("data/ford_green.csv", headers)
    out_older = save_data("data/older.csv", headers)

    filter_pink_cars = filter_data(lambda d: d[idx_color].lower() == "pink", 
                                out_pink_cars)

    def pred_ford_green(d):
        return (d[idx_make].lower() == "ford" 
                and d[idx_color].lower() == "green")

    filter_ford_green = filter_data(pred_ford_green, out_ford_green)
    filter_old = filter_data(lambda d: d[idx_year] <= 2010, out_older)
    filters = (filter_pink_cars, filter_ford_green, filter_old)

    broadcaster = broadcast(filters)
    while True:
        row = yield
        broadcaster.send(row)

@contextmanager
def pipeline():
    p = pipeline_coro()
    try:
        yield p
    finally:
        p.close()
       

if __name__ == "__main__":
    with pipeline() as pipe:
        data = data_parser()
        for row in data:
            pipe.send(row)
