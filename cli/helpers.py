import requests
import os
import sys
from .Colors import bcolors


def get_list_of_CIDRs():
    URL = "https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix"
    PARAMS = {}
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    return data


def error_handler(error):
    print(f'{bcolors.WARNING}See error output in terminal?{bcolors.ENDC}')
    choice = input("(y/N) > ")
    if choice == "n" or choice == "N":
        sys.exit()
    elif choice == "y" or choice == "Y":
        print(error)
