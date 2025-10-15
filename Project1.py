import csv

def read_file(file):

    infile = open(file)
    csv_reader = csv.reader(infile)

    next(csv_reader)

    penguins = {}

    for row in csv_reader:

        island = row[2]
        # print(island)

        year = row[-1]
        # print(year)

        bill_length = row[3]
        # print(bill_length)

        if not island in penguins:

            d = {}
            penguins[island] = d

        if not year in penguins[island]:

            l = []

            penguins[island][year] = l

        penguins[island][year].append(bill_length)

    return penguins

def calculate_average(bill_lengths):
    sum = 0

    for length in bill_lengths:

        if length != "NA":
            sum += float(length)

    return sum / len(bill_lengths)

        



data = read_file("penguins.csv")

average = calculate_average(data["Torgersen"]["2007"])

print(average)

