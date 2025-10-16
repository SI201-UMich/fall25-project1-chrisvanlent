# Name: Christopher van Lent
# Student ID:71095874
# Email: cvanlent@umich.edu
import csv


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



def calculate_highest_conditional(penguins, conditional_categories, conditional_values, data_category):
    max = 0

    for penguin in penguins:

        bool = True

        for i in range(len(conditional_categories)):

            # print(conditional_categories[i])

            if penguins[penguin][conditional_categories[i]] != conditional_values[i]:

                bool = False


        if bool:

            if penguins[penguin][data_category] != "NA":
                    

                    if float(penguins[penguin][data_category]) > max:

                        max = float(penguins[penguin][data_category])

    return max



def write_avg(infile, outfile):

    penguins = read_file(infile)

    outFile = open(outfile, "w")

    csv_writer = csv.writer(outFile)

    csv_writer.writerow(["Year", "Island", "Average"])

    # years = ["2007", "2008", "2009"]
    years = ["2008"]
    islands = ["Torgersen", "Biscoe", "Dream"]

    max_avg = 0
    max_island = ""
    max_year = ""


    for year in years:

        for island in islands:

            avg = calculate_average_conditional(penguins, ["island", "year"], [island, year], "bill_length")

            # outlist = [year, island, avg]

            # csv_writer.writerow(outlist)

            if avg > max_avg:

                max_avg = avg
                max_island = island
                max_year = year

    outlist = [max_year, max_island, max_avg]

    csv_writer.writerow(outlist)


    outFile.close


def write_largest(infile, outfile):

    penguins = read_file(infile)

    outFile = open(outfile, "w")

    csv_writer = csv.writer(outFile)

    csv_writer.writerow(["Species", "Sex", "Largest"])

    species = ["Adelie", "Gentoo"]
    sex = ["male", "female"]

    max_large = 0
    max_species = ""
    max_sex = ""


    for sp in species:

        for se in sex:

            large = calculate_highest_conditional(penguins, ["species", "sex"], [sp, se], "body_mass")

            # outlist = [sp, se, large]

            # csv_writer.writerow(outlist)

            if large > max_large:

                max_large = large
                max_species = sp
                max_sex = se

    outlist = [max_species, max_sex, max_large]

    # print(outlist)

    csv_writer.writerow(outlist)


    outFile.close


def main():



    write_avg("penguins.csv", "avg_output.csv")

    write_largest("penguins.csv", "large_output.csv")



main()
