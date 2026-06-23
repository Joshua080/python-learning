import requests
import sys
import json

if len(sys.argv) != 3:
    sys.exit("Usage: python itunes.py <search_term> <number_of_results>")

search_term = sys.argv[1]
number_of_results = int(sys.argv[2])

response = requests.get("https://itunes.apple.com/search?entity=song&limit=" + str(number_of_results) + "&term=" + search_term)
o = response.json()
for result in o["results"]:
    print(result["trackName"])