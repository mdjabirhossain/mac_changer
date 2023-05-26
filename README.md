# mac_changer
A python program that takes two command line arguments: an interface and a MAC address, and changes the current MAC address of the interface to the new MAC address given.

# Usage
After cloning the repository, navigate to the directory and run
`python3 mac_changer.py -i [interface] -m [MAC address]`
For example, `python3 mac_changer.py -i etho -m 00:11:22:33:44:55`.
MAC address option must be 12 characters long and each two characters must be seperated by a colon. 

# Options
-h, --help    show this help message and exit
-i INTERFACE, --interface=INTERFACE
              Interface to change its MAC address
-m NEW_MAC, --mac=NEW_MAC
              New MAC address
