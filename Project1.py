# Name: Christopher van Lent
# Student ID:71095874
# Email: cvanlent@umich.edu
import csv

# Takes in a csv file
# Returns a dictionary of dictonaries with outer-keys of ID, inner keys of data categories, and values of data points
def read_file(file):

    infile = open(file)
    csv_reader = csv.reader(infile)

    next(csv_reader)

    penguins = {}

    for row in csv_reader:

        "island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex","year"

        ID = row[0]
        species = row[1]
        island = row[2]
        bill_length = row[3]
        bill_depth = row[4]
        flipper_length = row[5]
        body_mass = row[6]
        sex = row[7]
        year = row[8]

        d = {

            "species": species,
            "island": island,
            "bill_length": bill_length,
            "bill_depth": bill_depth,
            "flipper_length": flipper_length,
            "body_mass": body_mass,
            "sex": sex,
            "year": year
        }

        penguins[ID] = d

    return penguins


# Takes in a list of string values (as well as a few NA strings)
# Returns average value in the list
def calculate_average_conditional(penguins, conditional_categories, conditional_values, data_category):
    sum = 0
    count = 0

    for penguin in penguins:

        bool = True

        for i in range(len(conditional_categories)):

            # print(conditional_categories[i])

            if penguins[penguin][conditional_categories[i]] != conditional_values[i]:

                bool = False


        if bool:

            if penguins[penguin][data_category] != "NA":

                    sum += float(penguins[penguin][data_category])
                    count += 1

    return sum/count



# Takes in a csv file and dictionary of dictonaries with outer-keys of islands, inner keys as years, and values as a list of bill_lengths
# writes table of Year, Island (with highest average), and Average value into csv file for years 2007, 2008, 2009
def write_file(penguins, file):

    outFile = open(file, "w")

    csv_writer = csv.writer(outFile)

    csv_writer.writerow(["Year", "Island", "Average"])

    years = ["2007", "2008", "2009"]
    islands = ["Torgersen", "Biscoe", "Dream"]

    for year in years:

        for island in islands:

            avg = calculate_average_conditional(penguins, ["island", "year"], [island, year], "bill_length")

            outlist = [year, island, avg]

            csv_writer.writerow(outlist)

    outFile.close

    









penguins = read_file("penguins.csv")

# print(penguins)

# average = calculate_average_conditional(penguins,["island", "year"],["Torgersen", "2009"],"bill_length")

# print(average)

# print(highest_average(penguins,"island",["Torgersen", "Biscoe", "Dream"], "bill_length"))



# print(compare_islands(penguins, "2007"))

write_file(penguins, "output.csv")

