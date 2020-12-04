import socket
import binascii
import os
import sys
from .helpers import get_list_of_CIDRs, error_handler
from .Colors import bcolors
import unittest


def check_if_ip_in_subnetwork(host_ip):

    print(f'{bcolors.OKBLUE}Searching...This may take a couple seconds.{bcolors.ENDC}')

    data = get_list_of_CIDRs()

    IPv4s = data['data']['resources']['ipv4']
    matched_subnetwork = []

    for subnetwork in IPv4s:
        is_subnetwork = ip_in_subnetwork(host_ip, subnetwork)
        if is_subnetwork:
            matched_subnetwork.append(is_subnetwork)

    return matched_subnetwork


def ip_in_subnetwork(ip_address, subnetwork):

    (ip_integer, version1) = ip_to_integer(ip_address)
    (ip_lower, ip_upper, version2) = subnetwork_to_ip_range(subnetwork)

    if version1 != version2:
        raise ValueError("incompatible IP versions")

    """to return the matching subnetwork"""
    if ip_lower <= ip_integer <= ip_upper:
        return subnetwork

    """to return True/False"""
    # return ip_lower <= ip_integer <= ip_upper


def ip_to_integer(ip_address):
    # try parsing the IP address first as IPv4, then as IPv6
    try:
        for version in (socket.AF_INET, socket.AF_INET6):
            ip_hex = socket.inet_pton(version, ip_address)
            ip_integer = int(binascii.hexlify(ip_hex), 16)
            return (ip_integer, 4 if version == socket.AF_INET else 6)

    except Exception as val:
        print(f'{bcolors.FAIL}FAIL{bcolors.ENDC}')
        error_handler(val)


def subnetwork_to_ip_range(subnetwork):

    # array with subnet mask and cidr (subnet mask)
    fragments = subnetwork.split('/')
    subnet_mask = fragments[0]
    cidr = int(fragments[1])

    # try parsing the subnetwork first as IPv4, then as IPv6
    for version in (socket.AF_INET, socket.AF_INET6):
        ip_len = 32 if version == socket.AF_INET else 128

        # shifts the left hand operand the number of places the right hand operand specifies.
        # Here, shifting 32 - the cidr - 1
        # subtracting 1 to get final value of upper and lower ranges as those will be our NetworkId and BroadcastID + or -1.
        suffix_mask = (1 << (ip_len - cidr)) - 1
        netmask = ((1 << ip_len) - 1) - suffix_mask
        ip_hex = socket.inet_pton(version, subnet_mask)
        ip_lower = int(binascii.hexlify(ip_hex), 16) & netmask
        ip_upper = ip_lower + suffix_mask

        return (ip_lower,
                ip_upper,
                4 if version == socket.AF_INET else 6)


def find_host_ip():
    print(" ")
    os.system('curl ifconfig.me')
    print('\n')
    print("-----------------------------------------------")
    print("1. Search For IP Address in CIDRs")
    print("2. Exit")

    choice = input("> ")

    if choice == "1":
        host_ip = input('> Enter IP Address: ')
        find_ip_in_cidr = check_if_ip_in_subnetwork(host_ip)
        print(f'{bcolors.OKGREEN}PASS{bcolors.ENDC}') if len(
            find_ip_in_cidr) >= 1 else print(f'{bcolors.FAIL}FAIL{bcolors.ENDC}')

    if choice == "2":
        sys.exit()
