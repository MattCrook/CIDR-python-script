import requests
import json
import ipaddress

__author__ = "Matt Crook"
__all__ = ['curl']


def curl(baseUrl, name, format, queryParams):
    queryParams = json.loads(queryParams)
    r = requests.get(baseUrl+'/' + name + '/data.' + format+'?',
                     params=queryParams)
    return json.loads(r.text)


def ipv4Search(ipv4, searchIpAddress):
    for network in ipv4:
        if ipaddress.ip_address(searchIpAddress) \
         in ipaddress.ip_network(network):
            return "Pass"
    return "Fail"
