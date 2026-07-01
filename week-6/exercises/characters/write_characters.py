import csv

name = input("Enter a character name: ")
species = input("Enter the character's species: ")

with open("characters.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "species"])
    writer.writerow({"name": name, "species": species})