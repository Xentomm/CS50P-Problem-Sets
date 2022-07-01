import sys
import requests
import json

if len(sys.argv) == 2:
    try:
        mnożnik = float(sys.argv[1])
    except ValueError:
        print("Error occured!(ValueError)")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response_json = response.json()

    #print(json.dumps(response_json['bpi']['USD']['rate_float'], indent = 2))
    wartość = response_json['bpi']['USD']['rate_float']
    print(f"Current value of {mnożnik} Bitcoins is ${mnożnik * wartość:,.4f}")
except requests.RequestException:
    print("Request exeption")
    sys.exit(1)

