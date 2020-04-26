import subprocess
import optparse
	
parser = optparse.OptionParser()

parser.addOption("-i", "--interface", dest = interface, help="interface name to change MAC")
parser
def main():
	
	interface = input("interfae> ")
	new_mac = input("new mac address> ")

	print("[+] Changing mac address for {} to {}".format(interface, new_mac))
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw",  "ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])

if __name__ == "__main__":
	main()