import smtplib
import requests
import time
from datetime import datetime
from password import email, passkey,to_email

MY_LAT = 9.318328 
MY_LONG = 76.611084  

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters={
    "lat":9.318328,
    "lon":76.611084,
    "formatted":0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
real_time = time_now.hour

def is_iss_overhead():
    if MY_LAT-5<=iss_latitude<=MY_LAT+5 and MY_LONG-5<=iss_longitude<=MY_LONG+5:
        return True

def is_night():
    if real_time<=sunset or real_time>=sunrise:
        return True

while True:
    time.sleep(120)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(email, passkey)
            connection.sendmail(from_addr=email,
                                to_addrs=to_email,
                                msg="Subject:Look UP the ISS is above you!\n\n The ISS is above you in the sky. Look up!")
            print("Email sent Successfully!")
        

