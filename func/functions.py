import time,subprocess,os,argparse
# list all functions
def bannerSpyPro():
	# banner 
	print("\n")
	f = open("bannerOfficial.txt", "r")
	print(f.read())
	print("version : 1.0 \n")
	# end banner

def menu():
	# Menu
	print("""
[+]  Pentest steps [+]

choose an option from[1-5]:

1. Information Gahtering
2. Vulnerability analysis
3. Exploitation
4. Post-Exploitation
5. Reporting

""")

def menuInfo():
	print("""
[+] Information Gahtering [+]

choose an option from [1-2]:

1. ping host to detect the OS
2. basic nmap scan
""")

#os Discovery
def osDiscovery():
	os.system("clear")
	bannerSpyPro()
	print("[+] OS Discovery [+] \n")
	print("Enter ip/domain")
	ip=str(input("sp1 > "))
	time.sleep(1)
	discoverPingOS=subprocess.run(f'ping -c 1 {ip} | grep "ttl=" | awk -F "ttl=" \'{{print $2}}\' | cut -d " " -f1', shell=True, capture_output=True, text=True)
	result1 = discoverPingOS.stdout.strip()
	result1=int(result1)
	if(result1==64 or result1==63):
		print("\n === Operating system ====")
		print('OS : Linux/Unix \n')
	elif(result1==123 or result1==124):
		print("\n === Operating system ====")
		print("\n OS : Windows")
# end 

# basic Nmap
def basicNmap():
	os.system("clear")
	bannerSpyPro()
	print("[+] Basic Nmap Scan [+] \n")
	print("Enter ip/domain")
	ip=str(input("sp1 > "))
	time.sleep(1)
	print("\n === Port Scan ====")
	os.system(f"nmap {ip} -sV -p1-1000 | grep 'open' | sed -E 's/(open)/\\x1b[31m\\1\\x1b[0m/g'")
#end

def manual():
	parser = argparse.ArgumentParser(description='My program')
	parser.add_argument('--h', action='help', help='Show this help message and exit')
	args = parser.parse_args()
