# Finding Given IP Address in Subnetwork

### Subnetting In CIDR Notation
For a description of CIDR notation, and how to find the upper and lower IP range from a given CIDR, see [Subnetting in CIDR Notation](./docs/CIDR.md).

## Set Up Instructions

* `git pull git@github.com:MattCrook/CIDR-python-script.git`
* `cd CIDR-python-script`
* I used a virtual environment to run this program and install dependencies, *this is not needed to run the program*, but if you want to, to do so run:
  * `python -m venv venv`
  * `source ./venv/bin/acitvate`
  * `pip install -r requirements.txt`
* To run program, execute on the CLI:
  * `chmod +x execute.sh` - to make shell command executable.
  * To run:
    * `./execute.sh`


To deactivate virtual env, simply run `deactivate`.

### Sample IPs To Test
You can follow the prompt in the program and try your own IP, or try one of the following:

* 68.52.38.81
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




## Tests

To run the tests, run the following command in the terminal.
```sh
python -m unittest tests/test_ip_in_subnetwork.py -b
```

## Functions
For a more in depth description of the logic used inside the functions, see [here](./docs/Functions.md)
