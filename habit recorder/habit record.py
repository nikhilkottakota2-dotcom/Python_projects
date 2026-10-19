import requests
import os
import datetime
USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
pixela_endpoint = "https://pixe.la/v1/users"
ID = "habitgraph"

# user_params = {
#     "token":"28r07a20m09y3a",
#     "username":"nikhil28",
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes"
# }

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_params = {
#     "id":ID,
#     "name":"code",
#     "unit":"number",
#     "type":"int",
#     "color":"shibafu"
# }

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(response.text)

graph_value_endpoint = f"{graph_endpoint}/{ID}"

today = datetime.datetime.now().date()
date = today.strftime("%Y%m%d")
date = str(date)
value_params = {
    "date": date,
    "quantity":"5"
    }

response = requests.post(url=graph_value_endpoint,json=value_params,headers=headers)
print(response.text)

# https://pixe.la/v1/users/nikhil28/graphs/habitgraph.html --> to access the graph