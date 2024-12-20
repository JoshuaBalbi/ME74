import requests
import json


URL = f"https://api.airtable.com/v0/app5ztWLVv5Dycp4W/Table%201?"
token = "patUNH6AJNI4yecWi.828835732f796d192922850f530f40c2cf2e7e3031fd3a413376a107df4001ba"
Headers = {'Authorization':'Bearer '+ token}

def req_info():
    response = requests.get(url = URL, headers = Headers, params = {})
    data = response.json()
    return data["records"][1]["fields"]["Notes"]

def req_weather_info():
    response = requests.get(url = URL, headers = Headers, params = {})
    data = response.json()
    return [int(data["records"][2]["fields"]["Notes"]),
            int(data["records"][4]["fields"]["Notes"]),
            int(data["records"][0]["fields"]["Notes"]),
            int(data["records"][5]["fields"]["Notes"]),
            int(data["records"][3]["fields"]["Notes"])]

def post_info(status):
    resp = {
        "records": [
            {
            "id": "recDCjZW4rrIItwXJ",
            "fields": {
                "Notes": status,
                "Name": "status"
            }
        }
        ]
        }
    response = requests.patch(URL, json = resp, headers = Headers)
    if response.status_code == 200:
        print("Record created successfully:", response.json())
    else:
        print("Failed to create record:", response.json())

def post_weather_info(numbers):
    ids = ['recFQuCz9o7jghGKx', 'recYSrf2Of6396Nmd', 'recCVPulvWLI2Iq80','recimLyC6LAos8XaH','recSYZJIsOFyj9AAt']
    names = ['Temperature','Humidity','UV_Index','Percipitation','Wind_speed']
    for i in range(5):
        resp = {
            "records": [
                {
                "id": ids[i],
                "fields": {
                    "Notes": str(numbers[i]),
                    "Name": names[i]
                }
            }
            ]
            }
        response = requests.patch(URL, json = resp, headers = Headers)
        if response.status_code == 200:
            print("Record created successfully:", response.json())
        else:
            print("Failed to create record:", response.json())


# [{'id': 'recCVPulvWLI2Iq80', 'createdTime': '2024-11-22T18:28:49.000Z', 'fields': {'Name': 'UV_Index', 'Notes': '0'}}, 
#  {'id': 'recDCjZW4rrIItwXJ', 'createdTime': '2024-10-29T18:01:37.000Z', 'fields': {'Name': 'status', 'Notes': 'Closed'}}, 
#  {'id': 'recFQuCz9o7jghGKx', 'createdTime': '2024-10-29T18:01:37.000Z', 'fields': {'Name': 'Temperature', 'Notes': '65'}}, 
#  {'id': 'recSYZJIsOFyj9AAt', 'createdTime': '2024-10-29T18:01:37.000Z', 'fields': {'Name': 'Wind_speed', 'Notes': '7.5'}}, 
#  {'id': 'recYSrf2Of6396Nmd', 'createdTime': '2024-11-22T18:29:00.000Z', 'fields': {'Name': 'Humidity', 'Notes': '30'}}, 
#  {'id': 'recimLyC6LAos8XaH', 'createdTime': '2024-11-22T18:28:42.000Z', 'fields': {'Name': 'Percipitation', 'Notes': '0'}}]

