from decouple import config
import requests
from datetime import datetime

GENDER = "Male"
WEIGHT_KG = "70"
HEIGHT_CM = "186"
AGE = "21"

NT_APP_ID = config("NT_APP_ID")
NT_API_KEY = config("NT_API_KEY")
NT_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = config("SHEETY_ENDPOINT")
SHEETY_TOKEN = config("TOKEN")

nt_headers = {"x-app-id": NT_APP_ID, "x-app-key": NT_API_KEY}

exercise_text = input("What workout did you go for today? ")

nt_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

nt_response = requests.post(
    url=NT_ENDPOINT, json=nt_params, headers=nt_headers
)
nt_result = nt_response.json()
# print(nt_result)

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

for exercise in nt_result["exercises"]:
    sheety_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_inputs, headers=sheety_headers)
sheety_result = sheety_response.json()
print(sheety_result)