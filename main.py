#!/usr/bin/python3
#coding:utf-8
#author : Djefferson saintilus
#spypro v1.0

print("")

print("choose an option from[1-5]")

print("""
[+]  Pentest steps [+]

1. Information Gahtering
2. Vulnerability analysis
3. Exploitation
4. Post-Exploitation
5. Reporting

""")
choose=int(input("sp1 > "))
try :
	if(choose is not int()):

		print(choose)
		if(choose > 0 and choose < 6):
			print("correct")
		else:
			print("Sorry your numbers should [1-5]")
	else:
		print("fjf")
except:
	print("Sorry you need to enter a number")

