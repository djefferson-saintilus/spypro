#coding:utf-8

import time,subprocess,os,argparse,re,sys
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

Enter an option (1-5):

1. Information Gahtering
2. Vulnerability analysis
3. Exploitation
4. Post-Exploitation
5. Reporting

""")

def menuInfoGathering():
	print("""
[+] Information Gahtering [+]

Enter an option (0-6):

1. check OS signature
2. check open ports 1-65535, and targeted
3. check firewall
4. check robots.txt
5. check subdomains
6. check zone-transfer
0. back

""")
#filter ip
def get_valid_ip():
	while True:
		print("Enter an IP address")
		ip = input("sp1 > ")
		ip_regex = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
		if re.match(ip_regex, ip):
			return ip
		else:
			print("\033[91mInvalid IP address. Please try again.\033[0m\n")
#end filter ip

#os Discovery
def osDiscovery():
	os.system("clear")
	bannerSpyPro()
	print("[+] OS Discovery [+] \n")
	ip = get_valid_ip()
	time.sleep(1)
	discoverPingOS=subprocess.run(f'ping -c 1 -W 1 {ip} | grep "ttl=" | awk -F "ttl=" \'{{print $2}}\' | cut -d " " -f1', shell=True, capture_output=True, text=True)
	result1 = str(discoverPingOS.stdout.strip())
	# check os ttl
	if(result1=="64" or result1=="63"):
		print("\n === Operating system ====")
		print('OS : Linux/Unix \n')
		time.sleep(5)
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
	ip = get_valid_ip()
	time.sleep(1)
	print("\n === Port Scan ====")
	command = f"nmap {ip} -n -T5 -p1-65535 --open -oN /tmp/nmap.txt | grep 'open' | sed -E 's/(open)/\\x1b[31m\\1\\x1b[0m/g'"
	try:
		result = subprocess.check_output(command, shell=True, text=True)
		if 'open' not in result:
			print("No open ports found or Host is unreacheable.")
		else:
			print(result)
			# nmap targeted
			print("Do you want to have more info about this/these port(s)? Y/n")
			while True:
				moreInfo=str(input("sp1 > "))
				if(moreInfo=="y" or moreInfo=="yes" or moreInfo=="Y"):
					os.system("clear")
					bannerSpyPro()
					os.system("grep -oP '\\d+(?=/tcp)' /tmp/nmap.txt | tr '\n' ',' | sed 's/,$//' > /tmp/port_numbers.txt")
					with open("/tmp/port_numbers.txt", "r") as f:
						portValues = f.readline().strip()
						print("[+] Port",portValues,"targeted ... [+]")
					print("")
					os.system(f"nmap {ip} -sV -p{portValues} -T5 -n | grep 'open' | sed -E 's/(open)/\\x1b[31m\\1\\x1b[0m/g'")
					break
				elif (moreInfo=="n" or moreInfo=="no" or moreInfo=="N"):
					print("")
					break
				else:
					print("\033[91mSorry you have to enter Y or n, try again.\033[0m")
			#end nmap targeted
	except subprocess.CalledProcessError as e:
		print("Error running command:", e)

	# end basic nmap
	##################
	print("")
	#######################
#end

def manual():
	parser = argparse.ArgumentParser(description='My program')
	parser.add_argument('--h', action='help', help='Show this help message and exit')
	args = parser.parse_args()
