import requests
End_point = "https://api.openweathermap.org/data/2.5/weather"
api_key =  "88acf73f46ec347f130943deb27d93d3"

weather_params = {
    "lat":18.565531,
    "lon":84.196769,
    "appid":api_key
}
response = requests.get(End_point,params=weather_params);
data = response.json()
print(f"wind speed is:{data["wind"]["speed"]}")