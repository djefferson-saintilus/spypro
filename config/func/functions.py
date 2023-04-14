import time,subprocess,os,argparse
# list all functions
def bannerSpyPro():
	# banner 
	print("\n")
	f = open("./config/bannerOfficial.txt", "r")
	print(f.read())
	print("version : 1.1 \n")
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

1. check OS signature
2. check open ports 1-65535, and targeted
3. check firewall
4. check robots.txt
5. check subdomains
6. check zone-transfer

""")

#os Discovery
def osDiscovery():
	os.system("clear")
	bannerSpyPro()
	print("[+] OS Discovery [+] \n")
	print("Enter ip/domain")
	ip=str(input("sp1 > "))
	time.sleep(1)
	discoverPingOS=subprocess.run(f'ping -c 1 -W 1 {ip} | grep "ttl=" | awk -F "ttl=" \'{{print $2}}\' | cut -d " " -f1', shell=True, capture_output=True, text=True)
	result1 = str(discoverPingOS.stdout.strip())
	if(result1=="64" or result1=="63"):
		print("\n === Operating system ====")
		print('OS : Linux/Unix \n')
	elif(result1=="127" or result1=="128"):
		print("\n === Operating system ====")
		print("\n OS : Windows")
	elif(result1=="" or result1=="0"):
		print("\n === Operating system ====")
		print("Not found, maybe some firewall blocking us, try with nmap -Pn")
# end 

# basic Nmap
def basicNmap():
	os.system("clear")
	bannerSpyPro()
	####################
	# basic nmap scan
	print("[+] Basic Nmap Scan [+] \n")
	print("Enter ip/domain")
	ip=str(input("sp1 > "))
	time.sleep(1)
	print("\n === Port Scan ====")
	os.system(f"nmap {ip} -n -T5 -p1-65535 --open -oN /tmp/nmap.txt | grep 'open' | sed -E 's/(open)/\\x1b[31m\\1\\x1b[0m/g'")
	# end basic nmap
	##################
	print("")
	##################
	# nmap targeted
	print("Do you want to have more info about this/these port(s)? Y/n")
	moreInfo=str(input("sp1 > "))
	if(moreInfo=="yes" or moreInfo=="Y" or moreInfo=="YES" or moreInfo=="y"):
		os.system("clear")
		bannerSpyPro()
		os.system("grep -oP '\\d+(?=/tcp)' /tmp/nmap.txt | tr '\n' ',' | sed 's/,$//' > /tmp/port_numbers.txt")
		with open("/tmp/port_numbers.txt", "r") as f:
			portValues = f.readline().strip()
			print("[+] Port targeted",portValues,"scanning ... [+]")
		print("")
		os.system(f"nmap {ip} -sV -p{portValues} -T5 -n | grep 'open' | sed -E 's/(open)/\\x1b[31m\\1\\x1b[0m/g'")
	else:
		print("Sorry you have to enter Y or n, try again")
	#end nmap targeted
	#######################
#end


def manual():
	parser = argparse.ArgumentParser(description='My program')
	parser.add_argument('--h', action='help', help='Show this help message and exit')
	args = parser.parse_args()
