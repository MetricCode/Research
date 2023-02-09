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













