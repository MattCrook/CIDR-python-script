import os
import requests
from ipaddress import IPv4Address
# URL = "https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix"
# location given here
# location = "delhi technological university"
# defining a params dict for the parameters to be sent to the API
# PARAMS = {'address': location}
# PARAMS = {}
# sending get request and saving the response as response object
# r = requests.get(url=URL, params=PARAMS)
# extracting data in json format
# data = r.json()
# host_ip = os.system('curl -sS ifconfig.me/ip')
# print(host_ip)
def build_main():
    # os.system('cls' if os.name == 'nt' else 'clear')
    # host_ip = os.system('curl -sS ifconfig.me/ip')
    # message = (f'Your Current IP Addres: {host_ip}')
    print("-----")
    print("Input Ip Address To Search If In Provided CIDRs")
    print("1. My IP Address")
    print("2. Search For IP Address in CIDRs")
    print("3. Exit")
def main():
    build_main()
    choice= input(">>")
    if choice == "1":
        pass
    if choice == "2":
        pass
    if choice == "3":
        os.system('clear')
main()
