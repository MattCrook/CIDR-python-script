import os
import requests
from ipaddress import IPv4Address
import subprocess
from cli import find_host_ip, check_if_ip_in_subnetwork, bcolors



def build_main():
    print("-----------------------------------------------")
    print("Input Ip Address To Search If In Provided CIDRs")
    print("-----------------------------------------------")

    print("1. My IP Address")
    print("2. Search For IP Address in CIDRs")
    print("3. Exit")


def main():
    build_main()

    choice = input("> ")

    if choice == "1":
        find_host_ip()

    if choice == "2":
        host_ip = input("> Enter IP Address: ")
        result = check_if_ip_in_subnetwork(host_ip)
        print(f'{bcolors.OKGREEN}PASS{bcolors.ENDC}') if len(result) >= 1 else print(f'{bcolors.FAIL}FAIL{bcolors.ENDC}')

    if choice == "3":
        os.system(f'echo {bcolors.WARNING} Exited{bcolors.ENDC}')


main()
