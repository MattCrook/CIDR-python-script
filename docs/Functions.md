## Functions

```py
def ip_in_subnetwork(ip_address, subnetwork):
```

* Returns True (or the matching subnetwork if you want it to) if the given IP address belongs to the
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
* Recieves the subnetwork and performs the necessary calculations in order to get the IP upper and lower ranges.
* Returns a tuple (`ip_lower, ip_upper, version`) containing the
integer values of the lower and upper IP addresses respectively
in a subnetwork expressed in CIDR notation (as a string), with
version being the subnetwork IP version (either 4 or 6).

`suffix_mask = (1 << (ip_len - cidr)) - 1`
* The "`<<`" bitwise operator shifts the left hand operand the number of places the right hand operand specifies.
* Binary of 1 is 0001, so as an example, if our `ip_len` in 32, and CIDR is 20;  32 - 20 is 12 so shift 12 places left...*1000000000000* which is 4096 in decimal. Then subtract 1 to give us our decimal number of 4095 which is 111111111111.
* We then covert the text into binary form using `inet_pton`. Then get the hexidecimal of that using `hexlify`.
* To get `ip_lower`, we use the "***&***" bitwise operator to perform a bit by bit AND operation, comparing the two to get the actual binary representation of the IP, and `ip_upper` we simply add the `ip_lower` and `suffix_mask` together.



```py
def check_if_ip_in_subnetwork(host_ip):
```
* Takes in the `host_ip` as and argument and calls `get_list_of_CIDRs()`, which sends an HTTP request the specified [endpoint](https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix) (RIPE network coordination center.). Data returned is a list of CIDRs in which we can loop through to determine if the provided IPv4 address is within the range of any of the returned CIDRs.
