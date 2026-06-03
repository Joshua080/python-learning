characters = [
    {"name": "Clarke", "clan": "Sky People", "age": 18},
    {"name": "Lincoln", "clan": "Grounders", "age": 20},
    {"name": "Russell", "clan": "Primes", "age": 22},
    {"name": "Bellamy", "clan": "Sky People", "age": 19},
    {"name": "Octavia", "clan": "Sky People", "age": 17},
    {"name": "Indra", "clan": "Grounders", "age": 21},
    {"name": "Alie", "clan": None, "age": 98},
]

for character in characters:
    print(character["name"], character["clan"], character["age"], sep=", ")
    