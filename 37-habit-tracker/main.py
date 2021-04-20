import requests
from datetime import datetime
from decouple import config

USERNAME = config("USERNAME")
TOKEN = config("TOKEN")
GRAPH_ID = config("GRAPH_ID")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Ka",
    "type": "float",
    "color": "ajisai",
}

headers = {"X-USER-TOKEN": TOKEN}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

new_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now().strftime("%Y%m%d")

new_pixel_config = {
    "date": today,
    "quantity": "12.5",
}
# response = requests.post(url=new_pixel_endpoint, json=new_pixel_config, headers=headers)
# print(response.text)

# yesterday = today - timedelta(days=1)
# print(yesterday)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

update_pixel_config = {"quantity": "7.4"}

# response = requests.put(
#     url=update_pixel_endpoint, json=update_pixel_config, headers=headers
# )
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)