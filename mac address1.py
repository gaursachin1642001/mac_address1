import subprocess
import optparse
import re

def get_argunment():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="show the interface")
    parser.add_option("-m", "--new_mac", dest="new_mac", help="show the mac address")
    (options, args) = parser.parse_args()
    if not options.interface:
        parser.error("[-] please enter the interface or more info just type --help")
    elif not options.new_mac:
        parser.error("[-] please enter the interface or more info just type --help")
    return options


def change_mac(interface, new_mac):
    print("Changing MAC address to " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    search_mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if search_mac_result:
        return search_mac_result.group(0)
    else:
        print("cannot find MAC ADDRESS")


options = get_argunment()
current_mac = get_current_mac(options.interface)
print("current_mac " + str(current_mac))

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[-] Mac suceessfully get changed to", current_mac)
else:
    print("[-] MAC donot get changed")

change_mac(options.interface, options.new_mac)


