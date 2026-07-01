import csv

characters = []

with open("characters.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        characters.append({"name": row["name"], "species": row["species"]})


for character in sorted(characters, key=lambda character: character["name"]):
    print(f"{character['name']} is a {character['species']}.")