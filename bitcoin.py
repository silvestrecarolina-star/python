import sys
import requests

# Check that exactly one command-line argument was given besides the file name
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

# Try to convert the argument to a float, error message if it fails
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    # Query the CoinCap API
    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=38bd219b9038f426bb0302b23ed3aff8aee705eb8177a171e8b55f71927a2036"
    )
    # Raise an exception if the request failed (e.g. invalid key, server error)
    response.raise_for_status()
except requests.RequestException:
    # Covers connection problems, timeouts, bad HTTP status codes, etc.
    sys.exit("Could not retrieve the Bitcoin price")

# Convert the response to a Python dictionary
data = response.json()

# The price is under "data" -> "priceUsd" and comes as a string,
# so convert it to a float
price = float(data["data"]["priceUsd"])

# Total cost of n Bitcoins
amount = price * n

# Print in USD with 4 decimal places and a comma as thousands separator
print(f"${amount:,.4f}")
