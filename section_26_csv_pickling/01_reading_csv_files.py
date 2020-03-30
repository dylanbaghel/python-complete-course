"""
Reading CSV Files:
    --> CSV files are a common file format for tabular data.
    --> We can read CSV files just like other text files.
    --> Python has a built-in CSV module to read/write CSVs more easily.
"""

"""
CSV Module:
    --> 'reader' - lets you iterate over rows of the CSV as lists.
    --> DictReader - lets you iterate over rows of the CSV as OrderedDicts.
    --> CSV Reader object is iterator. on which we can call 'next'.
    --> CSV DictReader object is iterator, on which we can call 'next'. 
    --> Readers accept a delimiter kwarg in case your data isn't separated by commas.
"""

# Reader
from csv import reader, DictReader
with open('users.csv') as file:
    csv_reader = reader(file)
    print(csv_reader)
    next(csv_reader)
    for row in csv_reader:
        print(row)

# Reader
with open('users.csv') as file:
    csv_reader = reader(file)
    csv_reader_list = list(csv_reader)
    print(csv_reader_list)

# Dict Reader
with open('users.csv') as file:
    csv_reader = DictReader(file)
    print(csv_reader)
    for row in csv_reader:
        # print(row)
        print(f"{row['Name']} is {row['age']} and lives in {row['address']}")

# Using Delimiter
with open('users2.csv') as file:
    csv_reader = reader(file, delimiter="|")
    csv_reader_list = list(csv_reader)
    print(csv_reader_list)

with open('users2.csv') as file:
    csv_reader = DictReader(file, delimiter="|")
    for row in csv_reader:
        # print(row)
        print(f"{row['Name']} is {row['age']} and lives in {row['address']}")
