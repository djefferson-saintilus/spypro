#!/usr/bin/python3
#coding:utf-8
#author : Djefferson saintilus
#spypro v1.0
import config.func.functions as fc
fc.manual() #help 

# Main
#Banner
#fc.bannerSpyPro()
#end Banner
#Menu
#fc.menu()
#end Menu
while True:
	#Banner
	fc.bannerSpyPro()
#end Banner
#Menu
	fc.menu()
#end Menu
	try:
		choice = int(input("sp1 > "))
		if choice not in range(1, 6):
			print("\033[91mInvalid option. Please enter a number between 1 and 5.\033[0m")
		else:
			if choice==1:
				while True:
					fc.bannerSpyPro()	
				#menu info gathering
					fc.menuInfoGathering()
				# end banner/menu
					try:
						choice1=int(input("sp1 > "))
						if choice1 not in range(0, 7):
							print("\033[91mInvalid option. Please enter a number between 0 and 7.\033[0m")
						elif choice1 == 0:
							break
						else:					
							# OS discovery
							if (choice1==1):
								fc.osDiscovery()
							# Basic nmap scan
							elif (choice1==2):
								fc.basicNmap()
							elif (choice1==3):
								print("Please wait ...")
							elif (choice1==4):
								print("Please wait ...")
							elif (choice1==5):
								print("Please wait ...")
							elif (choice1==6):
								print("Please wait ...")
							else:
								print("\033[91mInvalid option. Please enter a number between 0 and 7.\033[0m\n")
					except ValueError:
						print("\033[91mInvalid option. Please enter a number between 0 and 6.\033[0m")
			elif choice==2:
				print("Please wait")
			elif choice==3:
				print("Please wait")
			elif choice==4:
				print("Please wait")
			elif choice==5:
				print("Please wait")
			elif choice==0:
				print("")
				break
			else:
				print("\033[91mInvalid option. Please enter a number between 1 and 5.\033[0m")

	except ValueError:
		print("\033[91mInvalid option. Please enter a nuMber between 1 and 5.\033[0m")