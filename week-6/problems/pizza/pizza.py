import sys
from tabulate import tabulate
import csv

if len(sys.argv) == 2:

    if sys.argv[1][-4:] == ".csv":

        try:

            with open(sys.argv[1], "r") as file:
                reader = csv.reader(file)
                lines = list(reader)
            print(tabulate(lines, headers="firstrow", tablefmt="grid"))

        except FileNotFoundError:
            sys.exit("File name was not found in database")

    else:
        sys.exit("Please make sure its a .csv file")

else:
    sys.exit("Please make sure you have entered just the file name")
