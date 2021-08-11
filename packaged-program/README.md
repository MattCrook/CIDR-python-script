# pyRIPENCC
Input validated as IP v4 addess; returns Pass if IP address is present or Fail if not present in one of the CIDRs within the json data returned by RIPE NCC.


### make data cache dir
mkdir ripeStatCache

### load data
python pyQryRipencc/ripeStatQuery.py --name country-resource-list --format json --queryParams '{"resource": "US", "v4_format": "prefix"}'

### search IP (Pass)
python pyQryRipencc/ripeStatSearch.py --name country-resource-list --format json --queryParams '{"resource": "US", "v4_format": "prefix"}' --ipAddress 2.56.11.1

### search IP (Fail)
python pyQryRipencc/ripeStatSearch.py --name country-resource-list --format json --queryParams '{"resource": "US", "v4_format": "prefix"}' --ipAddress 123.123.123.1

### Command Line usage (ripeStatSearch)
python pyQryRipencc/ripeStatQuery.py -h 
usage: ripeStatQuery.py [-h] [--name {country-resource-list}] [--format {json,txt}] [--queryParams QUERYPARAMS]

RIPEstat Data Query CLI

optional arguments:
  -h, --help            show this help message and exit
  --name {country-resource-list}
                        One of the data calls found at https://stat.ripe.net/docs/data_api
  --format {json,txt}   Results format.
  --queryParams QUERYPARAMS
                        Query Parameters expressed as key value pairs.
                        {'key1': 'value1', 'key2': 'value2'}
                        Use Keys and values specific to the data call, for example:
                        --name country-resource-list --queryParams \
                            {'resource': 'US', 'v4_format': 'prefix'}

### Command Line usage (ripeStatSearch)
python pyQryRipencc/ripeStatSearch.py -h
usage: ripeStatSearch.py [-h] [--name {country-resource-list}] [--format {json,txt}] [--queryParams QUERYPARAMS] --ipAddress IPADDRESS

RIPEstat Data Cache Search

optional arguments:
  -h, --help            show this help message and exit
  --name {country-resource-list}
                        One of the data calls found at https://stat.ripe.net/docs/data_api
  --format {json,txt}   Results format.
  --queryParams QUERYPARAMS
                        Query Parameters expressed as key value pairs.
                        {'key1': 'value1', 'key2': 'value2'}
                        Use Keys and values specific to the data call, for example:
                        --name country-resource-list --queryParams \
                            {'resource': 'US', 'v4_format': 'prefix'}
  --ipAddress IPADDRESS
                        Results format.