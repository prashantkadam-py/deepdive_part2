import csv

def parse_data(fname):

    with open(fname, "r") as f:
        dialect = csv.Sniffer().sniff(f.read(2000))
        f.seek(0)
        next(f)
        yield from csv.reader(f, dialect=dialect)


def filter_data(rows, contains):

    for row in rows:
        if contains in row[0]:
            yield row


def output(fname, *filter_words):
    data = parse_data(fname)
    for filter_word in filter_words:
        data = filter_data(data, filter_word)
    yield from data 


if __name__ == "__main__":
    results = output("data/cars.csv", "Chevrolet", "Carlo", "Landau")
    for row in results:
        print(row)
