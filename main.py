import requests
import os
from dotenv import find_dotenv, load_dotenv
from twilio.rest import Client

dotenv_path = find_dotenv('.env')
load_dotenv(dotenv_path)

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")


OWP_API = "https://api.openweathermap.org/data/2.5/forecast"
MY_KEY = os.getenv("API_KEY")
parameters ={
    "lat":"38.826341",
    "lon":"65.801800",
    "appid":MY_KEY
}

response = requests.get(url=OWP_API,params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["list"][0:12]

is_sky_clear = False
for hour_data in weather_slice:
    weather_codes = hour_data["weather"][0]['id']
    if weather_codes >= 800:
        is_sky_clear = True

if is_sky_clear:
    client = Client(account_sid, auth_token) 
    message = client.messages.create(
        body="Sky is clear",
        from_="+19787092481",
        to="+998904289727"
    )
    print(message.body)





