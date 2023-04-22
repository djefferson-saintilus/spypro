#coding:utf-8

import time,subprocess,os,argparse,re,sys,threading
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
3. lorem
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
	
	# animateProgress start
	stop_event = threading.Event()
	progress_thread = threading.Thread(target=animate_progress, args=(stop_event,))
	progress_thread.start()
	result1 = str(discoverPingOS.stdout.strip())
	stop_event.set()
	progress_thread.join()
	print("Scanning completed.")
	# end progress

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
		print("\033[91mOperating system not found, or Host unreachable.\033[0m")
		time.sleep(5)
# end

def animate_progress(stop_event):
    while not stop_event.is_set():
        for symbol in "|/-\\":
            print("\rScanning in progress... " + symbol, end="", flush=True)
            time.sleep(0.1)
# basic Nmap
def basicNmap():
	os.system("clear")
	bannerSpyPro()
	####################
	print("[+] Basic Nmap Scan [+] \n")
	ip = get_valid_ip()
	time.sleep(1)
	print("\n === Port Scan ====")
	command = f"nmap {ip} -Pn -n -T5 -p1-65535 --open --min-rate 5000 -oN ./tmp/nmap.txt | grep 'open' | sed -E 's/(open)/\\x1b[31m\\1\\x1b[0m/g'"
	stop_event = threading.Event()
	try:
		# animateProgress start
		progress_thread = threading.Thread(target=animate_progress, args=(stop_event,))
		progress_thread.start()
		result = subprocess.check_output(command, shell=True, text=True)
		stop_event.set()
		progress_thread.join()
		print("Scanning completed.")
		# end progress

		if 'open' not in result:
			print("\033[91mNo open ports found or Host is unreacheable.\033[0m")
		else:
			print("")
			print(result)
			# nmap targeted
			print("Do you want to have more info about this/these port(s)? Y/n")
			while True:
				moreInfo=str(input("sp1 > "))
				if(moreInfo=="y" or moreInfo=="yes" or moreInfo=="Y"):
					os.system("clear")
					bannerSpyPro()
					os.system("grep -oP '\\d+(?=/tcp)' ./tmp/nmap.txt | tr '\n' ',' | sed 's/,$//' > ./tmp/port_numbers.txt")
					with open("./tmp/port_numbers.txt", "r") as f:
						portValues = f.readline().strip()
						print("[+] Port",portValues,"targeted ... [+]")
					print("")
					command = f"nmap {ip} -sV -p{portValues} -T5 -n  --min-rate 5000 -Pn | grep 'open' | sed -E 's/(open)/\\x1b[31m\\1\\x1b[0m/g'"
					# animateProgress start
					stop_event = threading.Event()
					progress_thread = threading.Thread(target=animate_progress, args=(stop_event,))
					progress_thread.start()
					result = subprocess.run(command, shell=True, capture_output=True, text=True)
					stop_event.set()
					progress_thread.join()
					print("Scanning completed.")
					# end progress
					if 'open' not in result.stdout:
						print("\033[91mNo open ports found or Host is unreachable.\033[0m")
					else:
						print("")
						port_info = result.stdout.strip()
						print(port_info)
					sys.exit()
				elif (moreInfo=="n" or moreInfo=="no" or moreInfo=="N"):
					print("")
					break
				else:
					print("\033[91mInvalid choice. Please enter Y or n..\033[0m")
			#end nmap targeted
	except subprocess.CalledProcessError as e:
		print("\033[91mError occurred while scanning.\033[0m")


	# end basic nmap
	##################
	print("")
	#######################
#end

def manual():
	parser = argparse.ArgumentParser(description='My program')
	parser.add_argument('--h', action='help', help='Show this help message and exit')
	args = parser.parse_args()
