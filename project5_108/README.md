# Project5

## Goal 1

- For this goal, you are given a number of CSV files, each of which have their first row with the field name.

- You goal is to create a context manager that you can use to produce the data from each file in a named tuple with field names corresponding to the header row field names.

- You should use the csv module's reader function to help with parsing the data.

- Your context manager should be generic in the sense that it should just need the file name, no other configuration or hardcoded functionality is required. You do not need to worry about data types for this goal - just return every field as a string.

- In addition, your context manager should produce lazy iterators.

- Implement this using a class that implements the context manager protocol

## Goal 2
- The goal is to reproduce the work you did in Goal 1, but using a generator function and the contextlib contextmanager decorator.

### Notes
- The files included with this project are:

    cars.csv
    personal_info.csv


