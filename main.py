import requests
import json
from datetime import datetime

NUTRONIX_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRONIX_API_ID = "ed78f121"
NUTRONIX_APP_KEY = "64e1266a99428c08415bd961e2e547ef"

nutronix_headers = {
    "x-app-id": NUTRONIX_API_ID, 
    "x-app-key": NUTRONIX_APP_KEY, 
    "x-remote-user-id": "0",
}

user_params_nutri = {
    "query": input("Tell me which exercise you did: "),
    "gender": "male",
    "weight_kg": 43.5,
    "height_cm": 171.64,
    "age": 17
}

response = requests.post(url=NUTRONIX_API_ENDPOINT, json=user_params_nutri, headers=nutronix_headers)
workout_data = json.loads(response.text)

username = "aidren"
password = "aidrendjfnusamaamimnineue"
token = "YWlkcmVuOmFpZHJlbmRqZm51c2FtYWFtaW1uaW5ldWU="

SHEETY_ENDPOINT = "https://api.sheety.co/7392ef5a891ac8017761137caf3c54a7/workoutTracking/workouts"

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

for exercise in workout_data['exercises']:
    workout_details = {    
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise['name'].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(url=SHEETY_ENDPOINT, params=workout_details)

    shetty_headers = {
        "Authorization" : f"Basic {token}"
    }

    sheety_response = requests.post(
        SHEETY_ENDPOINT, 
        json=workout_details,     
        headers=shetty_headers,
        auth=(
            username, 
            password
        )
    )

    print(sheety_response.text)

