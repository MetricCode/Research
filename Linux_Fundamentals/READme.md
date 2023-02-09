# Linux Fundamentals!
## @Author : M3tr1c_r00t
### Linux File System
![image](https://user-images.githubusercontent.com/99975622/217579694-4812602e-c98b-4671-89c3-15a0ff7a7f5c.png)
### Linux Architecture
![image](https://user-images.githubusercontent.com/99975622/217583364-3f022e3a-ffe4-41a8-a994-18a4baa18e43.png)

### Linux Components
![image](https://user-images.githubusercontent.com/99975622/217583591-accd5761-c572-4773-9402-8156429ea178.png)

### Linux Philosophy
![image](https://user-images.githubusercontent.com/99975622/217583890-80f8c268-dbad-402c-a803-cb766a6b3bee.png)

To get a definition of a tool, we can use the apropos tool.
```
apropos ssh
```
### System Information Commands
![image](https://user-images.githubusercontent.com/99975622/217589852-b5c2eebb-b5cb-4dcf-a4b9-3814c580ce15.png)

#### Uname options
![image](https://user-images.githubusercontent.com/99975622/217591843-fd9bbe38-3844-4267-a2a9-79a11a14aa84.png)


To view which shell you are in;
```
echo $SHELL
```
### User Management
root files only - 
```
/etc/shadow
```
Commands executable by root user or user's with permission.
![image](https://user-images.githubusercontent.com/99975622/217785180-cddde790-2be9-4c0d-8eb4-67c2ded017e1.png)

### Package Management
Package Management Systems include;
![image](https://user-images.githubusercontent.com/99975622/217790849-34f98f5c-4caf-4b47-b38f-4c856b591890.png)

To view files in which the software repositories are stored in are found in;
```
/etc/apt/sources.list
```
We can the search for a specific tool present in the apt-cache;
```
apt-cache search <TOOL>
```
To view info on a tool;
```
apt-cache show <TOOL>
```
To list installed tools;
```
apt list --installed
```
To install a tool;
```
sudo apt install <TOOL> -y
```
#### DPKG
To install a .deb file, 
```
sudo dpkg -i <TOOL>.deb
```
To check all installed tools in total;
```
dpkg --list | grep "^ii" |wc -l
```
### Service And Process Management
__A daemon__ is a service process that runs in the background and supervises the system or provides functionality to other processes.

There are two services;
- Internal(Are Required during system startup)
- External

All processes have an assigned PID that can be viewed under /proc/ with the corresponding number. Such a process can have a parent process ID (PPID), and if so, it is known as the child process.

Besides systemctl we can also use update-rc.d to manage SysV init script links.

#### Systemctl
To start a service;
```
systemctl start <SERVICE>
```
To view info on a running service;
```
systemctl status <SERVICE>
```

To add a Service to the SysV script to tell the system to run this service after startup, we can link it with the following command:

```
systemctl enable <SERVICE>
```

Once we reboot the system, the server will automatically run.

We can also use systemctl to list all services;
```
systemctl list-units --type=service
```
It is quite possible that the services do not start due to an error. To see the problem, we can use the tool journalctl to view the logs.

```
journalctl -u <SERVICE>.service --no-pager
```
#### Processes
- Running
- Waiting (waiting for an event or system resource)
- Stopped
- Zombie (stopped but still has an entry in the process table).

Processes can be controlled using kill, pkill, pgrep, and killall. To interact with a process, we must send a signal to it. We can view all signals with the following command:
```
kill -l
```

![image](https://user-images.githubusercontent.com/99975622/217797354-03d13f9f-2fee-4c90-8941-02c99994e8d2.png)

For example, if a program were to freeze, we could force to kill it with the following command:
```
kill 9 <PID>
```
#### Backgrounding a job...
```
ctrl + Z
```
The [Ctrl] + Z shortcut suspends the processes, and they will not be executed further. To keep it running in the background, we have to enter the command bg to put the process in the background.

We can also add the & at the end of the command...

Once the process finishes, we will see the results.

To view backgrounded jobs
```
jobs
```
To view listening services;
```
// this excludes 127.0.0
netstat -tunleep4 | grep -v "127\.0\.0"
```
#### Foregrounding a Process
First check the jobs running;
```
jobs
```
Then you can foreground a task using;
```
fg <number>
```
#### Executing Multiple Commands
we can use;
```
;
|
&& (ampersand)
```

### Working With Web Services
#### Apache
installing the apache web server...
```
apt install apache2 -y
```
We can open a http.server;
```
 python3 -m http.server <PORT>
```

##### Curl
cURL is a tool that allows us to transfer files from the shell over protocols like HTTP, HTTPS, FTP, SFTP, FTPS, or SCP. This tool gives us the possibility to control and test websites remotely. Besides the remote servers' content, we can also view individual requests to look at the client's and server's communication.

##### Wget
An alternative to curl is the tool wget. With this tool, we can download files from FTP or HTTP servers directly from the terminal, and it serves as a good download manager. If we use wget in the same way, the difference to curl is that the website content is downloaded and stored locally.

##### npm
We can use npm to open a http.server
```
sudo apt-get install nodejs
sudo apt install npm -y
// installing the http.server package from npm
npm install -g http-server
//starting the web-server
http-server -p 80
```
##### php server
```
php -S 127.0.0.1:8080
```
### Commands
to move into the last directory we were in.
```
cd -
```
To find the index/inode of a file;
```
ls -i <FILE_NAME>
```
inodes stores the file’s metadata, including all the storage blocks on which the file’s data can be found. 

Information found on an inode;
- File size
- Device on which the file is stored 
- User and group IDs associated with the file
- Permissions needed to access the file
- Creation, read, and write timestamps
- Location of the data (though not the filepath)

### Files and Directories
creating new directories
```
mkdir <NAME>
```

creating new directories with parent directories
```
mkdir -p name/name/name
```
we can use treee command to see the directories;
```
tree .
```
### Editing Files
#### Vim
![image](https://user-images.githubusercontent.com/99975622/217897859-7ced871a-1e22-4335-a8b7-08b33643b73f.png)

### Finding Files And Directories
#### which
We can find some binaries and programs using;
```
which <PROGRAM>
```
#### find
is a super useful tool
![image](https://user-images.githubusercontent.com/99975622/217898628-34b55cb0-8ab5-4241-82fd-6d972e12751f.png)

What is the name of the config file that has been created after 2020-03-03 and is smaller than 28k but larger than 25k? 
```
find / -iname "*.conf" -size +25k -size -28k -newermt 2020-03-03 2>/dev/null
```
#### locate
we can use the locate command to find  files and directories.
The locate command works with a local database with the following command.
```
sudo updatedb
```

### File Descriptors and Redirections
A file descriptor (FD) in Unix/Linux operating systems is an indicator of connection maintained by the kernel to perform Input/Output (I/O) operations. In Windows-based operating systems, it is called filehandle. It is the connection (generally to a file) from the Operating system to perform I/O operations (Input/Output of Bytes). By default, the first three file descriptors in Linux are:

1. Data Stream for Input
- STDIN – 0
2. Data Stream for Output
- STDOUT – 1
3. Data Stream for Output that relates to an error occurring.
- STDERR – 2

Review again sources;
```
https://academy.hackthebox.com/module/18/section/79
```

to view contents of proftpd ;
```
locate proftpd.conf
```
Then cat the file to see user and pass details.

### Chmod
u- owner
g- group
o - others
a- all

r-read
w-write
x-execute
```
chmod a+r /bin/shell
```
If we use the octal representation;
![image](https://user-images.githubusercontent.com/99975622/217927740-03f27067-3cc8-4d7e-a4a9-dca9c9c37db2.png)
#### Change owner
we can the chown command;
```
chown <user>:<group> <file/directory>
chown root:root shell
```
#### SUID & GUID
Besides assigning direct user and group permissions, we can also configure special permissions for files by setting the Set User ID (SUID) and Set Group ID (GUID) bits. These SUID/GUID bits allow, for example, users to run programs with the rights of another user. Administrators often use this to give their users special rights for certain applications or files. The letter "s" is used instead of an "x". When executing such a program, the SUID/GUID of the file owner is used.

#### Sticky Bit
Sticky bits are a type of file permission in Linux that can be set on directories. This type of permission provides an extra layer of security when controlling the deletion and renaming of files within a directory. It is typically used on directories that are shared by multiple users to prevent one user from accidentally deleting or renaming files that are important to others.

For example, in a shared home directory, where multiple users have access to the same directory, a system administrator can set the sticky bit on the directory to ensure that only the owner of the file, the owner of the directory, or the root user can delete or rename files within the directory. This means that other users cannot delete or rename files within the directory as they do not have the required permissions. This provides an added layer of security to protect important files, as only those with the necessary access can delete or rename files. Setting the sticky bit on a directory ensures that only the owner, the directory owner, or the root user can change the files within the directory.

When a sticky bit is set on a directory, it is represented by the letter “t" in the execute permission of the directory's permissions. For example, if a directory has permissions “rwxrwxrwt", it means that the sticky bit is set, giving the extra level of security so that no one other than the owner or root user can delete or rename the files or folders in the directory.

If the sticky bit is capitalized (T), then this means that all other users do not have execute (x) permissions and, therefore, cannot see the contents of the folder nor run any programs from it. The lowercase sticky bit (t) is the sticky bit where the execute (x) permissions have been set.

### Linux Terminal Shortcuts
#### Cursor Movement
- [CTRL] + A - Move the cursor to the beginning of the current line.
- [CTRL] + E - Move the cursor to the end of the current line.
- [CTRL] + [←] / [→] - Jump at the beginning of the current/previous word.
- [ALT] + B / F - Jump backward/forward one word.

#### Erase the current Line
- [CTRL] + U - Erase everything from the current position of the cursor to the beginning of the line.
- [Ctrl] + K - Erase everything from the current position of the cursor to the end of the line.
- [Ctrl] + W - Erase the word preceding the cursor position.

#### Paste erased Contents
ctrl + y

#### Reverse Search
Go through previous commands
[CTRL] + R

### Linux Security
Being updated is being better.
Updating the OS and its packages;
```
apt update && apt dist-upgrade
```
If firewall rules are not appropriately set at the network level, we can use the Linux firewall and/or iptables to restrict traffic into/out of the host.

If SSH is open on the server, the configuration should be set up to disallow password login and disallow the root user from logging in via SSH. It is also important to avoid logging into and administering the system as the root user whenever possible and adequately managing access control. Users' access should be determined based on the principle of least privilege. For example, if a user needs to run a command as root, then that command should be specified in the sudoers configuration instead of giving them full sudo rights. Another common protection mechanism that can be used is fail2ban. This tool counts the number of failed login attempts, and if a user has reached the maximum number, the host that tried to connect will be handled as configured.

It is also important to periodically audit the system to ensure that issues do not exist that could facilitate privilege escalation, such as an out-of-date kernel, user permission issues, world-writable files, and misconfigured cron jobs, or misconfigured services. Many administrators forget about the possibility that some kernel versions have to be updated manually.

An option for further locking down Linux systems is Security-Enhanced Linux (SELinux) or AppArmor. This is a kernel security module that can be used for security access control policies. In SELinux, every process, file, directory, and system object is given a label. Policy rules are created to control access between these labeled processes and objects and are enforced by the kernel. This means that access can be set up to control which users and applications can access which resources. SELinux provides very granular access controls, such as specifying who can append to a file or move it.

Besides, there are different applications and services such as Snort, chkrootkit, rkhunter, Lynis, and others that can contribute to Linux's security. In addition, some security settings should be made, such as:

    Removing or disabling all unnecessary services and software
    Removing all services that rely on unencrypted authentication mechanisms
    Ensure NTP is enabled and Syslog is running
    Ensure that each user has its own account
    Enforce the use of strong passwords
    Set up password aging and restrict the use of previous passwords
    Locking user accounts after login failures
    Disable all unwanted SUID/SGID binaries

This list is incomplete, as safety is not a product but a process. This means that specific steps must always be taken to protect the systems better, and it depends on the administrators how well they know their operating systems. The better the administrators are familiar with the system, and the more they are trained, the better and more secure their security precautions and security measures will be.
TCP Wrappers

TCP wrapper is a security mechanism used in Linux systems that allows the system administrator to control which services are allowed access to the system. It works by restricting access to certain services based on the hostname or IP address of the user requesting access. When a client attempts to connect to a service the system will first consult the rules defined in the TCP wrappers configuration files to determine the IP address of the client. If the IP address matches the criteria specified in the configuration files, the system will then grant the client access to the service. However, if the criteria are not met, the connection will be denied, providing an additional layer of security for the service. TCP wrappers use the following configuration files:
- /etc/hosts.allow
- /etc/hosts.deny

In short, the /etc/hosts.allow file specifies which services and hosts are allowed access to the system, whereas the /etc/hosts.deny file specifies which services and hosts are not allowed access. These files can be configured by adding specific rules to the files.

/etc/hosts.allow
```
# Allow access to SSH from the local network
sshd : 10.129.14.0/24

# Allow access to FTP from a specific host
ftpd : 10.129.14.10

# Allow access to Telnet from any host in the inlanefreight.local domain
telnetd : .inlanefreight.local
```

/etc/hosts.deny
```
# Deny access to all services from any host in the inlanefreight.com domain
ALL : .inlanefreight.com

# Deny access to SSH from a specific host
sshd : 10.129.22.22

# Deny access to FTP from hosts with IP addresses in the range of 10.129.22.0 to 10.129.22.255
ftpd : 10.129.22.0/24
```


#### Feel free to checkout my writeups on boxes and challenges!
<a href="https://github.com/MetricCode">My Github Repo </a>
 #### You can also visit the other repos while you're at it! 
## My socials:
<br>@ twitter: https://twitter.com/M3tr1c_root
<br>@ instagram: https://instagram.com/m3tr1c_r00t/
