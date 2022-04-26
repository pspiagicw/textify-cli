import requests
from textify import database
import time
import json

SERVER_URL = "http://localhost:5000"

def Pull():
    ID = database.Get_ID()
    r = requests.get(SERVER_URL + '/pull/' + ID)
    if r.status_code == 200:
        data = r.json()
        database.SetDatabase(data)
    else:
        print("Failed!!!")

def Push(payload):
    ID = database.Get_ID()
    final_data = dict(id = ID , **payload )
    r = requests.post(SERVER_URL + '/push/' + ID ,  json = final_data )
    if r.status_code == 200:
        print("Push Sucessfull!")
    else:
        print("Push Unsucessfull!")

def Login(id):
    database.clearData()
    if id:
        config = dict(uid = id , timestamp = time.time())
        database.SetID(config)
    else:
        r = requests.get(SERVER_URL + '/login' )
        if r.status_code == 200:
            database.SetID(r.json())
    


