import requests
MY_LAT = 18.565531
MY_LONG = 84.196769
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
