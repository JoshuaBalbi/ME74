import requests
import json


URL = f"https://api.airtable.com/v0/app5ztWLVv5Dycp4W/Table%201?"
token = "patUNH6AJNI4yecWi.828835732f796d192922850f530f40c2cf2e7e3031fd3a413376a107df4001ba"
Headers = {'Authorization':'Bearer '+ token}

def req_info():
    response = requests.get(url = URL, headers = Headers, params = {})
    data = response.json()
    return data["records"][1]["fields"]["Notes"]

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

