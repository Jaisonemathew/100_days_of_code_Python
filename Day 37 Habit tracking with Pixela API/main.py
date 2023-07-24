import requests
from password import TOKEN,USERNAME
from datetime import datetime

GRAPH_ID="onepiece"
headers={"X-USER-TOKEN":TOKEN}

pixela_endpoint = "https://pixe.la/v1/users"
params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
} 
# response = requests.post(url=pixela_endpoint,json=params)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    "id":GRAPH_ID,
    "name":"One Piece Watched",
    "unit":"episodes",
    "type":"int",
    "color":"sora",
}


# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

today=datetime.now()
pixel_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":"2",
}

response=requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4"
}


# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)


