from collections import namedtuple
from functools import partial
from datetime import datetime

filename = "nyc_parking_tickets_extract.csv"

def parse_column_names():
    with open(filename, "r") as rows:
        row = next(rows)
    column_names = [ column_name.strip().replace(" ", "_").lower() for column_name in row.strip("\n").split(",") ] 
    return column_names

def parse_int(value, default = None):
    try:
        return int(value)
    except ValueError:
        return default


def parse_date(value, default = None): 
    try:
        return datetime.strptime(value, "%m/%d/%Y").date()
    except ValueError:
        return default

def parse_string(value, default=None):
    try:
        normalized_value = value.strip()
        value = normalized_value if normalized_value else default
        return value
    except:
        return default



column_names = parse_column_names()
Ticket = namedtuple("Ticket", column_names)
column_parsers = (
                   parse_int,
                   parse_string,
                   lambda x : parse_string(x, default = ""),
                   partial(parse_string, default= ""),
                   parse_date,
                   parse_int,
                   partial(parse_string, default=""),
                   parse_string,
                   lambda x : parse_string(x, default="")
                )

def read_data():
    with open(filename, "r") as rows:
        next(rows)
        yield from rows


def parse_row(row, *, default=None):
    fields = row.strip("\n").split(",")
    parsed_data = [func(field) for func, field in zip(column_parsers, fields)]

    if all(item is not None for item in parsed_data):
        return Ticket(*parsed_data)
    return default

def parse_data():
    for i, row in enumerate(read_data()):
        parsed_data = parse_row(row)
        if parsed_data is None:
            #print(i, list(zip(column_names, row.strip("\n").split(","))))
            pass
        else:
            yield parsed_data 

if __name__ == "__main__":
    parse_data()

    
