import requests
import os
from datetime import datetime as date

NUTRITION_ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/8ab1cbec2ac028194f23883e85f1d81a/exerciseSpreadsheet/sheet1"
APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
headers = {
    "Content-Type":"application/json",
    "x-app-id":APP_ID,
    "x-app-key":APP_KEY
}
user_entry = input("Enter the activity: ")
data = {
    "query":user_entry
}

response = requests.post(url=NUTRITION_ENDPOINT,headers=headers,json=data)
result = response.json()

today = date.now().date()
today = today.strftime("%d/%m/%Y")

time = date.now().time()
time = time.strftime("%H:%M:%S")
sheet_body = {
    "sheet1":{
        "date":today,
        "time":time,
        "exercise":result["exercises"][0]["name"],
        "duration":result["exercises"][0]["duration_min"],
        "calories":result["exercises"][0]["nf_calories"]
    }
}

print("Sending to Sheety:")
print(sheet_body)

response = requests.post(url=SHEET_ENDPOINT,json=sheet_body)
response.raise_for_status()
print(response.text)
response = requests.get(SHEET_ENDPOINT)
print(response.status_code)
print(response.text)