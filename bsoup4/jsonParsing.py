import json
from urllib.error import HTTPError
from urllib.request import urlopen


def getCountry(ipAddress):
    try:
        response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode("utf-8")
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get("country_code")

print(getCountry("50.78.253.58"))