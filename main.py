#!/usr/bin/python3
#coding:utf-8
#author : Djefferson saintilus
#spypro v1.0
import time,subprocess

# banner 
print("\n")
f = open("bannerOfficial.txt", "r")
print(f.read())
print("[+] version : 1.0 [+] \n")
# end banner

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

# Main
try:
	i=0
	while (i < 1):
		choose=int(input("sp1 > "))
		if(choose is not int() and choose !=0):
			if(choose > 0 and choose < 6):
				print("\n [+] Information Gahtering [+]")
				print("""
choose an option [1-2]:

1. ping host to detect the OS
2. basic nmap scan
					""")
				choose1=int(input("sp1 > "))
				if (choose1==1):
					print("Enter ip/domain")
					ip=str(input("sp1 > "))
					print("Please wait ...")
					time.sleep(0.1)
					discoverPingOS=subprocess.run(f'ping -c 1 {ip} | grep "ttl=" | awk -F "ttl=" \'{{print $2}}\' | cut -d " " -f1', shell=True, capture_output=True, text=True)
					result1 = discoverPingOS.stdout.strip()
					result1=int(result1)
					if(result1==64 or result1==63):
						print("")
						print("[+] OS discovery [+]")
						print('OS : Linux/Unix \n')
						print("would you want to discover the version? Y/n")
						discoverNmapOS=str(input("sp1 > "))
					elif(result1==123 or result1==124):
						print("\n OS : Windows")					
				break
			else:
				print("Sorry you should choose a number from 1-5")
		else:
			print("Sorry you should choose a number from 1-5")
	i += 1
except ValueError as err1:
	print("Sorry you should enter a NUMBER from 1-5")