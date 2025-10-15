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

def compare_islands(penguins, year):

    max = 0
    max_island = ""

    for island in penguins:

        avg = calculate_average(penguins[island][year])
        print(island + ": " + str(avg))

        if avg > max:

            max = avg
            max_island = island

    return max_island









penguins = read_file("penguins.csv")

# average = calculate_average(data["Torgersen"]["2007"])



print(compare_islands(penguins, "2007"))

