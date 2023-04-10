#!/usr/bin/python3
#coding:utf-8
#author : Djefferson saintilus
#spypro v1.0
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
				fc.bannerSpyPro()

				# banner gathering info
				fc.menuInfo()
				# end banner
				
				choose1=int(input("sp1 > "))
				# OS discovery
				if (choose1==1):
					fc.osDiscovery()

				# Basic nmap scan
				elif (choose1==2):
					fc.basicNmap()
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