import argparse
import textwrap
import ipaddress
import ripeStat


__author__ = "Matt Crook"


def main(args):
    baseUrl = args.baseUrl
    name = args.name
    format = args.format
    searchIpAddress = args.ipAddress
    queryParams = args.queryParams
    result = ripeStat.curl(baseUrl, name, format, queryParams)
    ipv4 = result['data']['resources']['ipv4']
    print(ripeStat.ipv4Search(ipv4, searchIpAddress))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='RIPEstat Data Cache Search',
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--baseUrl',
                        required=True,
                        help='Base URL, try https://stat.ripe.net/data/')
    parser.add_argument('--name', choices=['country-resource-list'],
                        help=textwrap.dedent('''\
                            One of the data calls found at \
                            https://stat.ripe.net/docs/data_api
                        '''))
    parser.add_argument('--format',
                        choices=['json', 'txt'],
                        help='Results format.')
    parser.add_argument('--queryParams', help=textwrap.dedent('''\
                            Query Parameters expressed as key value pairs.
                            {'key1': 'value1', 'key2': 'value2'}
                            Use Keys and values specific to the data call, \
                                for example:
                            --name country-resource-list --queryParams \\
                                {'resource': 'US', 'v4_format': 'prefix'}
                        '''))
    parser.add_argument('--ipAddress',
                        action="store",
                        type=ipaddress.ip_address,
                        required=True,
                        help='IP Address')
    args = parser.parse_args()
    main(args)
