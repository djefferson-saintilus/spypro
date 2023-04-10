import time
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
