import sys
import requests

try:
    n = float(sys.argv[1])
except (ValueError, IndexError):
    sys.exit("Usage: python bitcoin.py <number>")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=a72c77e3a5dab15b014d0a577edfb825d98b8a21457f65f7766efb25ba6603f3")
    data = response.json()
    rate = float(data["data"]["priceUsd"])
except (requests.RequestException, KeyError, ValueError):
    sys.exit("Error fetching Bitcoin price")

total = n * rate
print(f"${total:,.4f}")