import requests
import json
import sys

try:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json() # data = json.dumps(response.json(), indent=2) (TO READ DATA BETTER)
    rate = data["bpi"]["USD"]["rate_float"]
    value = amount * rate
    print(f"${value:,.4f}")

except requests.RequestException:
    sys.exit()

