import requests
import json
import uuid

SERVER_URL = "http://localhost:5000/process_prompt"
INPUT_FILE = "input.txt"
OUTPUT_FILE = "client_output.json"

CLIENT_ID = str(uuid.uuid4())


def send_prompt_to_server(prompt, client_id):
    params = {"prompt": prompt, "clientID": client_id}

    response = requests.get(SERVER_URL, params=params)
    # response = dict(response)
    # if(client_id != response["Client ID"]):
    #     response["Source"] = "user"

    return response.json()

while(True):
    prompt = input("Enter Prompt\n")
    response = send_prompt_to_server(prompt,CLIENT_ID)
    print(response)

