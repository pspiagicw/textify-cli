import json
import os
import pathlib
import sys


def get_database_location():
    home = str(pathlib.Path.home())
    datapath = os.path.join(home , '.textify')
    return datapath

def get_User_config_path():
    home = get_database_location()
    config_path = os.path.join(home, "user.json")
    return config_path

def get_database_path():
    home = get_database_location()
    database_path = os.path.join(home, "database.json")
    return database_path

def Get_ID():
    Checkfolder()
    CheckConfigFile()
    with open(get_User_config_path()) as f:
        data = json.load(f)
        return data['id']

def SetID(config):
    Checkfolder()
    with open(get_User_config_path(), 'w') as json_file:
        json.dump(config, json_file)

def GetDatabase():
    Checkfolder()
    CheckDatabaseFile()
    with open(get_database_path()) as f:
        data = json.load(f)
        return data

def SetDatabase(User_data):
    Checkfolder()
    with open(get_database_path(), 'w') as json_file:
        json.dump(User_data, json_file)

    
def Checkfolder():
    check = os.path.isdir(get_database_location())
    if check == False:
        os.mkdir(get_database_location())

def CheckConfigFile():
    datafile = os.path.join(get_database_location() , 'user.json')
    check = os.path.isfile(datafile)
    if check == False:
        print("No user file found! Login first!")
        sys.exit(1)
def CheckDatabaseFile():
    databasefile = os.path.join(get_database_location() ,'database.json')
    check = os.path.isfile(databasefile)
    if check == False:
        print("No database file found! Pull first!")
        sys.exit(1)
        
        
