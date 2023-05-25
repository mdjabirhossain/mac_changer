import subprocess
import optparse

def change_mac(interface, new_mac):
    print(f"[+] Changing current MAC address of {interface} to new address {new_mac}")  

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    return parser.parse_args()


def main():
    values, args = get_args()
    change_mac(values.interface, values.new_mac)


if __name__ == "__main__":
    main()


