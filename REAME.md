## Finding Given IP Address in Subnetwork

### Subnetting In CIDR Notation
For a description of CIDR notation, and how to find the upper and lower IP range from a given CIDR, see [Subnetting in CIDR Notation](docs/CIDR.md).



### Functions

```py
def ip_in_subnetwork(ip_address, subnetwork):
```

* Returns True if the given IP address belongs to the
subnetwork expressed in CIDR notation, otherwise False.
Both parameters are strings.

* We compute a "suffix mask", which is a mask whose bits are equal to one if they are in the host part of an IP address and zero if they are part of the network prefix. This mask is the same as the netmask for the given subnetwork with all bits inverted. Since the lowest IP address in a given subnetwork has all bits in the host part equal to zero, it is identical to the network prefix. By summing the network prefix and the suffix mask, we get the largest IP address in the subnetwork.


```py
def ip_to_integer(ip_address):
```
* Converts an IP address expressed as a string to its
representation as an integer value and returns a tuple
(ip_integer, version), with version being the IP version
(either 4 or 6).

* Both IPv4 addresses (e.g. "192.168.1.1") and IPv6 addresses
(e.g. "2a02:a448:ddb0::") are accepted.


```py
def subnetwork_to_ip_range(subnetwork):
```
* Returns a tuple (ip_lower, ip_upper, version) containing the
integer values of the lower and upper IP addresses respectively
in a subnetwork expressed in CIDR notation (as a string), with
version being the subnetwork IP version (either 4 or 6).

* Both IPv4 subnetworks (e.g. "192.168.1.0/24") and IPv6
subnetworks (e.g. "2a02:a448:ddb0::/44") are accepted.

```py
def check_if_ip_in_subnetwork(host_ip):
```
* Takes in the host_ip as and argument and calls `get_list_of_CIDRs()`, which sends an HHTP request the specified [endpoint](https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix) (RIPE network coordination center.). Data returned is a list of CIDRs in which we can loop through to determine if the provided IPv4 address is within the range of any of the returned CIDRs.


### Tests

To run the tests, run the following command in the terminal.
```
python -m unittest tests/test_ip_in_subnetwork_methods.py
```
