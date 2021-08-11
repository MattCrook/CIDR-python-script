import pytest
import os
import subprocess
from unittest import mock
import ipaddress
import json
import pyQryRipencc.ripeStat as ripeStat


@pytest.fixture(autouse=True)
def mock_settings_env_vars():
    env = {
        "CONFIG": "conf/ripeStatQuery.ini",
        "NAME": "country-resource-list",
        "FORMAT": "json",
        "QUERYPARAMS": '{\"resource\": \"US\", \"v4_format\": \"prefix\"}',
        "BASEURL": 'https://stat.ripe.net/data/'
    }
    with mock.patch.dict(os.environ, env):
        yield


def test_ripeStat_curl_valid():
    # config = configparser.ConfigParser()
    # config.read(os.getenv('CONFIG', default=None))
    baseUrl = os.getenv('BASEURL', default=None)
    name = os.getenv('NAME', default=None)
    format = os.getenv('FORMAT', default=None)
    queryParams = os.getenv('QUERYPARAMS', default=None)
    result = ripeStat.curl(baseUrl, name, format, queryParams)
    ip = ipaddress.ip_network(result['data']['resources']['ipv4'][0])
    assert type(ip) is ipaddress.IPv4Network


def test_ripeStat_ipv4Search_pass():
    baseUrl = os.getenv('BASEURL', default=None)
    name = os.getenv('NAME', default=None)
    format = os.getenv('FORMAT', default=None)
    queryParams = os.getenv('QUERYPARAMS', default=None)
    queryResult = ripeStat.curl(baseUrl, name, format, queryParams)
    ipv4 = queryResult['data']['resources']['ipv4']
    searchIpAddress = '216.163.196.1'
    searchResult = ripeStat.ipv4Search(ipv4, searchIpAddress)
    assert searchResult == "Pass"


def test_ripeStat_ipv4Search_fail():
    baseUrl = os.getenv('BASEURL', default=None)
    name = os.getenv('NAME', default=None)
    format = os.getenv('FORMAT', default=None)
    queryParams = os.getenv('QUERYPARAMS', default=None)
    queryResult = ripeStat.curl(baseUrl, name, format, queryParams)
    ipv4 = queryResult['data']['resources']['ipv4']
    searchIpAddress = '192.168.1.1'
    searchResult = ripeStat.ipv4Search(ipv4, searchIpAddress)
    assert searchResult == "Fail"


def test_ripeStatSearch_main():
    baseUrl = os.getenv('BASEURL', default=None)
    name = os.getenv('NAME', default=None)
    format = os.getenv('FORMAT', default=None)
    queryParams = json.loads(os.getenv('QUERYPARAMS', default=None))
    ipAddress = '216.163.196.1'
    cmd = ['python',
           'pyQryRipencc/ripeStatSearch.py',
           '--baseUrl', baseUrl,
           '--name', name,
           '--format', format,
           '--queryParams', json.dumps(queryParams),
           '--ipAddress', ipAddress]
    result = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    result.wait()
    assert result.returncode == 0
