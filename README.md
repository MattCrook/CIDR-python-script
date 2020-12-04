# Finding Given IP Address in Subnetwork

### Subnetting In CIDR Notation
For a description of CIDR notation, and how to find the upper and lower IP range from a given CIDR, see [Subnetting in CIDR Notation](docs/CIDR.md).

## Set Up Instructions

* `git pull git@github.com:MattCrook/CIDR-python-script.git`
* `cd CIDR-python-script`
* I used a virtual environment to run this program and install dependencies, *this is not needed to run the program*, but if you want to, to do so run:
  * `python -m venv venv`
  * `source ./venv/bin/acitvate`
  * `pip install -r requirements.txt`
* To run program, execute on the CLI:
  * `python main.py`

To deactivate virtual env, simply run `deactivate`.

### Sample IPs To Test
You can follow the prompt in the program and try your own IP, or try one of the following:

* 68.52.38.81 (Mine)
* 50.38.30.81
* I took a random IPv4 from the list at the endpoint [provided](https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix), ***(14.102.172.0/22)*** , and manually backwards engineered it to find out the IP range. Doing this meant that any IP in the range I found should result in a *PASS*.
  * The range I found was:
    * 13.101.172.1
    * 13.101.175.254
  * As examples, a couple failing IPs are:
    * 192.168.1.1
    * 192.168.4.12
    * 192.168.4.0
    * Or you can try just typing any random combination of numbers...(you might get lucky and find one that passes!)
      * I tried 60.80.30.10



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
* Recieves the subnetwork and performs the necessary calculations in order to get the IP upper and lower ranges.
* Returns a tuple (`ip_lower, ip_upper, version`) containing the
integer values of the lower and upper IP addresses respectively
in a subnetwork expressed in CIDR notation (as a string), with
version being the subnetwork IP version (either 4 or 6).

`suffix_mask = (1 << (ip_len - cidr)) - 1`
* The "`<<`" bitwise operator shifts the left hand operand the number of places the right hand operand specifies.
* Binary of 1 is 0001, so as an example, if our `ip_len` in 32, and CIDR is 20;  32 - 20 is 12 so shift 12 places left...*1000000000000* which is 4096 in decimal. Then subtract 1 to give us our  our decimal number of 4095 which is 111111111111.
* We then covert the text into binary form using `inet_pton`. Then get the hexidecimal of that using `hexlify`.
* To get `ip_lower`, we use the "***&***" bitwise operator to perform a bit by bit AND operation, comparing the two to get the actual binary representation of the IP.



```py
def check_if_ip_in_subnetwork(host_ip):
```
* Takes in the host_ip as and argument and calls `get_list_of_CIDRs()`, which sends an HHTP request the specified [endpoint](https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix) (RIPE network coordination center.). Data returned is a list of CIDRs in which we can loop through to determine if the provided IPv4 address is within the range of any of the returned CIDRs.


## Tests

To run the tests, run the following command in the terminal.
```sh
python -m unittest tests/test_ip_in_subnetwork.py -b
```
