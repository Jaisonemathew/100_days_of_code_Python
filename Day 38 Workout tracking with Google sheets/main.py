from config import API_KEY, APP_ID,sheety_api_key,TOKEN
from datetime import datetime
import requests
GENDER="Male"
WEIGHT_KG=60
HEIGHT_CM=140
AGE=22

query = input("Tell me which exercise you did: ")
excersise_api=f"https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "x-app-id": APP_ID,
    'x-app-key': API_KEY
}
params={
 "query":query,
 "gender":GENDER,
 "weight_kg":WEIGHT_KG,
 "height_cm":HEIGHT_CM,
 "age":AGE
}
response = requests.post(url=excersise_api,json=params,headers=header)
result = response.json()
print(result)
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


sheet_endpoint=f"https://api.sheety.co/{sheety_api_key}/copyOfMyWorkouts/workouts"
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
header = {"Authorization": f"Bearer {TOKEN}"}

sheet_response = requests.post(sheet_endpoint, json=sheet_inputs,headers=header)

print(sheet_response.text)