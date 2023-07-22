import requests
from password import key,sid,auth_token,frm_num,to_num
from twilio.rest import Client

api_url=f"https://api.openweathermap.org/data/2.5/onecall"
weather_params={
    "lat": 9.318328,
    "lon": 76.611084,
    "exclude": "current,minutely,daily,alerts",
    "appid": key
}
response=requests.get(api_url, params=weather_params)
response.raise_for_status()    
weather_data=response.json()
weather_slice=weather_data["hourly"][:12]
will_rain=False
for hour_data in weather_slice:
    if int(hour_data["weather"][0]["id"])<700:
        will_rain=True
if will_rain:
    client=Client(sid,auth_token)
    message=client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella☔.",
        from_=frm_num,
        to=to_num
    )
    print(message.status)
