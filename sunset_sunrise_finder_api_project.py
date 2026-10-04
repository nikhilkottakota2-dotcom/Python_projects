import requests
MY_LAT = 18.617958
MY_LONG = 18.617958
parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG
}

response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data  = response.json()
sunrise  = data['results']['sunrise']
sunset = data['results']['sunset']
print(f"Sunrise : {sunrise}")
print(f"Sunset : {sunset}")
