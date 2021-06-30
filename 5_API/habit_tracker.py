
import requests
from datetime import datetime

#1. setup a new account at Pixela
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "-"
USERNAME = "-"
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_params = {
#     "id": "graph",
#     "name": "graph_python_studying",
#     "unit": "hours",
#     "type": "float",
#     "color": "sora"
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

today = datetime.now()
yday = datetime(year=2021, month=1, day=19)
thedaybefore = datetime(year=2021, month=1, day=18)
graph_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph"

graph_post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you study today?: ")
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_post_endpoint, json=graph_post_params, headers=headers)
print(response.text)

