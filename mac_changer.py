import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

values, args = parser.parse_args()

interface = values.interface
new_mac = values.new_mac

print(f"[+] Changing current MAC address of {interface} to new address {new_mac}")  

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])


