#!/usr/bin/python3
#coding:utf-8
#author : Djefferson saintilus
#spypro v1.0
import time,subprocess,os
import func.functions as fc

#Banner
fc.bannerSpyPro()
#end Banner

#Menu
fc.menu()
#end Menu

# Main
try:
	i=0
	while (i < 1):
		choose=int(input("sp1 > "))
		if(choose is not int() and choose !=0):
			if(choose > 0 and choose < 6):
				os.system("clear")
				fc.bannerSpyPro()
				print("""
	\n [+] Information Gahtering [+]

choose an option from [1-2]:

1. ping host to detect the OS
2. basic nmap scan
""")
				choose1=int(input("sp1 > "))
				# OS discovery
				if (choose1==1):
					os.system("clear")
					fc.bannerSpyPro()
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
				# Basic nmap scan
				elif (choose1==2):
					os.system("clear")
					fc.bannerSpyPro()
					print("[+] Basic Nmap Scan [+] \n")
					print("Enter ip/domain")
					ip=str(input("sp1 > "))
					time.sleep(1)
					print("\n === Port Scan ====")
					os.system(f"nmap {ip} -sV -p1-1000 | grep 'open' | sed -E 's/(open)/\\x1b[31m\\1\\x1b[0m/g'")
				else:
					print("")

				break
			else:
				print("Sorry you should choose a number from 1-5")
		else:
			print("Sorry you should choose a number from 1-5")
	i += 1
except ValueError as err1:
	print("Sorry you should enter a NUMBER from 1-5")