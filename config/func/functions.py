#coding:utf-8

import time,subprocess,os,argparse,re,sys,threading,asyncio,aiohttp

# list all functions
def bannerSpyPro():
	# banner 
	print("\n")
	f = open("./config/bannerOfficial.txt", "r")
	print(f.read())
	print("version : 1.1 \n")
	# end banner

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
	subprocess.call("clear", shell=True)
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
        print("Scanning in progress... |", end="\r")
        time.sleep(0.5)
        print("Scanning in progress... /", end="\r")
        time.sleep(0.5)
        print("Scanning in progress... -", end="\r")
        time.sleep(0.5)
        print("Scanning in progress... \\", end="\r")
        time.sleep(0.5)
    print(" " * 30, end="\r")  # Clear progress animation line

# basic Nmap
def basicNmap():
	subprocess.call("clear", shell=True)
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

def dirListing():
    subprocess.call("clear", shell=True)
    bannerSpyPro()
    ####################
    print("[+] Directory Listing [+]\n")
    ip = get_valid_ip()
    print("Enter the wordlist file (default press ENTER):")
    wordlist = input()
    
    if wordlist == "":
        wordlist = "/usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt"
    
    command = f"gobuster dir -u {ip} -w {wordlist} -q -t 40"
    stop_event = threading.Event()
    progress_thread = threading.Thread(target=animate_progress, args=(stop_event,))
    progress_thread.start()
    output = subprocess.check_output(command, shell=True, universal_newlines=True)
    stop_event.set()
    progress_thread.join()
    print("Scanning completed.\n")
    
    # Filter and display the directories found
    print("[+] Directories Found:\n")
    lines = (line for line in output.splitlines())
    directories = set()
    for line in lines:
        if "(Status: 301)" in line or "(Status: 302)" in line:
            directory = line.split()[0]
            directories.add(directory)
    
    if directories:
        for directory in directories:
            print(directory)
    else:
        print("No directories found.")
    
    time.sleep(5)

#check robots.txt
def fetch_robots_txt(urlCheck):
    robots_url = f"http://{urlCheck}/robots.txt"
    async def fetch():
        async with aiohttp.ClientSession() as session:
            async with session.get(robots_url, allow_redirects=True) as response:
                if response.status == 200:
                    print("\n[+] Robots.txt Found: \n")
                    robots_content = await response.text()
                    print(robots_content)
                else:
                    print("\n[-] Robots.txt Not Found.")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch())

def get_valid_ip_dns():
    while True:
        print("Enter an IP address or DNS: ")
        ip_dns = input("sp1 > ")

        # Check if the input matches the IP address format
        ip_regex = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
        dns_regex = r'^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])' \
                    r'(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9]))*$'

        if re.match(ip_regex, ip_dns) or re.match(dns_regex, ip_dns):
            # Verify if the host is online
            if is_host_online(ip_dns):
                return ip_dns
            else:
                print("Host is not online. Please try again.")
        else:
            print("Invalid input. Please try again.")

def is_host_online(ip_dns):
    # Use ping command to check if the host is online
    try:
        subprocess.check_output(['ping', '-c', '1', ip_dns])
        return True
    except subprocess.CalledProcessError:
        return False

def check_robots_txt():
    subprocess.call("clear", shell=True)
    bannerSpyPro()
    print("[+] Check robots.txt [+]")
    urlCheck = get_valid_ip_dns()
    time.sleep(1)
    stop_event = threading.Event()
    progress_thread = threading.Thread(target=animate_progress, args=(stop_event,))
    progress_thread.start()

    # Function check start
    fetch_robots_txt(urlCheck)
    # Function check end

    stop_event.set()
    progress_thread.join()
    print("Scanning completed.\n")

    time.sleep(5)

def manual():
	parser = argparse.ArgumentParser(description='My program')
	parser.add_argument('--h', action='help', help='Show this help message and exit')
	args = parser.parse_args()
