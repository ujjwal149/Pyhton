import requests


#GET INTERNATIONAL SPACE STATION LOCATION.

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json() ["iss_position"]
# print(data)


#GET SUN RISE AND SUN SET TIME OF ANY PARTICULAR LATITUDE AND LONGITUDE.
parameters = {
    "lat":30.744600,
    "lng":76.652496,
    "formatted":0
}

response = requests.get("https://api.sunrise-sunset.org/json",parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(f"Sun rise at: {sunrise}")
print(f"Sun set at: {sunset}")
