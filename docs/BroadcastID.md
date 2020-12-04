### Finding the Broadcast ID

#### BroadcastID or Broadcast Address
* The address in a subnet not assigned to single host, it is broadcasted or sent to all hosts and devices on the network.


Since we know the network portion of the ID based on the subnet, we now take what is called the *wildcard* bits which will indicate the portion of the octet bits that are not a part of the network. We logically assign a value of 1 to all those bits, and in this example our wildcard is:
* **0.0.0.255**

In simple terms, you can think of the broadcast ID as an inversion or opposite of the bits set in the subnet ID.

Now using our example from the previous page, since the subnet is 192.168.40.0, the last octet consists of the wildcard bits. Since all bits are set a value of 1, it will be: ***192.168.63.255***.
