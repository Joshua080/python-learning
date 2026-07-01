import sys
import csv

characters = []

if len(sys.argv) == 3:

    if sys.argv[1][-4:] == ".csv" and sys.argv[2][-4:] == ".csv":

        try:

            with open(sys.argv[1], "r") as file:

                reader = csv.DictReader(file)
                for row in reader:
                    characters.append({"name": row["name"], "house": row["house"]})

            with open(sys.argv[2], "w") as file:

                writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in characters:

                    last_name, first_name = row["name"].split(", ")
                    house = row["house"]
                    writer.writerow({"first": first_name, "last": last_name, "house": house})

        except FileNotFoundError:
            sys.exit("File was not found")

    else:
        sys.exit("Please make sure both files are .csv")

else:
    sys.exit("Please input the names of an input and output file.")
