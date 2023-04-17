import subprocess

ip = "110.0.0.159"
command = f"nmap {ip} -n -T5 -p1-65535 --open -oN /tmp/nmap.txt | grep 'open' | sed -E 's/(open)/\\x1b[31m\\1\\x1b[0m/g'"
try:
    result = subprocess.check_output(command, shell=True, text=True)
    if 'open' not in result:
        print("No open ports found or Host is unreacheable.")
    else:
        print(result)
except subprocess.CalledProcessError as e:
    print("Error running command:", e)
