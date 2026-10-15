
#wether forecast api call link     https://api.openweathermap.org/data/2.5/forecast
#weather data api call link        https://api.openweathermap.org/data/2.5/weather
#ventusky.com shows the exact live weather movements

import smtplib
import requests
from datetime import *
import os

def sendmessage(time):
    MY_MAIL = "yourmail@email"
    MY_pass = os.environ.get("MAIL_PASS")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_MAIL,MY_pass)
        connection.sendmail(
            from_addr=MY_MAIL,
            to_addrs="sendermail@email",
            msg=f"Subject:Rain Alert\n\nGet Your Umbrella while going to outside\n Timing:  {time}."
        )


End_point = "https://api.openweathermap.org/data/2.5/forecast"
api_key =  os.environ.get("FORECAST_API")

weather_params = {
    "lat":18.565531,
    "lon":84.196769,
    "appid":api_key
}
response = requests.get(End_point,params=weather_params)

data = response.json()
now = datetime.now()


for forecast in data["list"]:
    time=datetime.strptime(
                forecast["dt_txt"],"%Y-%m-%d %H:%M:%S"
                )
    if time >= now:
        condition = int(forecast["weather"][0]["id"])
        if condition<700:
            sendmessage(time)
            break

