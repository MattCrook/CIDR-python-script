import requests
import os


def get_list_of_CIDRs():
    URL = "https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix"
    PARAMS = {}
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    return data


def error_handler(error):
    print("See error output in terminal?")
    choice = input("(y/N) > ")
    print(error) if choice == "y" or choice == "Y" else os.system('clear')
