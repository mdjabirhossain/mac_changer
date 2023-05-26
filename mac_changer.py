import subprocess
import optparse
import re


# changes the MAC address of interface to new_mac
def change_mac(interface, new_mac):
    print(f"[+] Changing current MAC address of {interface} to new MAC address {new_mac} ...")

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


# parses the command line arguments that include interface and name and new MAC address
def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    values, args = parser.parse_args()
    if not values.interface:
        parser.error("[-] Please enter an interface, use --help for more info.")
    elif not values.new_mac:
       parser.error("[-] Please enter a new MAC address, use --help for more info.") 
    return values


# returns the current MAC address of interface
def get_mac_address(interface):
    ifconfig_output = subprocess.check_output(["ifconfig", interface])
    mac_add_search_output = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_output.decode("utf-8"))
    if mac_add_search_output:
        return mac_add_search_output.group(0)
    else:
        print("[-] Could not find MAC address.")


def main():
    values = get_args()
    current_mac = str(get_mac_address(values.interface))
    print(f"Current MAC address = {current_mac}")
    change_mac(values.interface, values.new_mac)
    current_mac = str(get_mac_address(values.interface))
    if current_mac == values.new_mac:
        print(f"[+] Successfully changed the current MAC address to {current_mac}.")
    else:
        print("[-] Failed to change the MAC address.")


if __name__ == "__main__":
    main()


