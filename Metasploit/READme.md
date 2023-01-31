# Metaploit!
## Modules

The Modules detailed above are split into separate categories in this folder. We will go into detail about these in the next sections. They are contained in the following folders:
### Modules
```
MetricCode@htb[/htb]$ ls /usr/share/metasploit-framework/modules
```
auxiliary  encoders  evasion  exploits  nops  payloads  post

### Plugins

Plugins offer the pentester more flexibility when using the msfconsole since they can easily be manually or automatically loaded as needed to provide extra functionality and automation during our assessment.
### Plugins
```
MetricCode@htb[/htb]$ ls /usr/share/metasploit-framework/plugins/

aggregator.rb      ips_filter.rb  openvas.rb           sounds.rb
alias.rb           komand.rb      pcap_log.rb          sqlmap.rb
auto_add_route.rb  lab.rb         request.rb           thread.rb
beholder.rb        libnotify.rb   rssfeed.rb           token_adduser.rb
db_credcollect.rb  msfd.rb        sample.rb            token_hunter.rb
db_tracker.rb      msgrpc.rb      session_notifier.rb  wiki.rb
event_tester.rb    nessus.rb      session_tagger.rb    wmap.rb
ffautoregen.rb     nexpose.rb     socket_logger.rb
```
### Scripts

Meterpreter functionality and other useful scripts.
Scripts
```
MetricCode@htb[/htb]$ ls /usr/share/metasploit-framework/scripts/

meterpreter  ps  resource  shell
```
### Tools

Command-line utilities that can be called directly from the msfconsole menu.
Tools
```
MetricCode@htb[/htb]$ ls /usr/share/metasploit-framework/tools/

context  docs     hardware  modules   payloads
dev      exploit  memdump   password  recon
```

### Commands
```
msfconsole -q
```
opens msfconsole in silence mode.

### MSF Engagement Structure

The MSF engagement structure can be divided into five main categories.

- Enumeration
- Preparation
- Exploitation
- Privilege Escalation
- Post-Exploitation

This division makes it easier for us to find and select the appropriate MSF features in a more structured way and to work with them accordingly. Each of these categories has different subcategories that are intended for specific purposes. These include, for example, Service Validation and Vulnerability Research.

### Syntax
Syntax
```
<No.> <type>/<os>/<service>/<name>
794   exploit/windows/ftp/scriptftp_list
```
![image](https://user-images.githubusercontent.com/99975622/215698139-90fbd5e6-d288-43ae-b8a7-b01eca8134ec.png)

#### Commands
```
info // shows information on an exploit
target // you can get to specify the type of target you want to run your exploit on... 
grep meterpreter show payloads //you can filter for payloads...
meterpreter commands...
getuid //whoami...
type ? to see the available commands...
```
### Payloads


A Payload in Metasploit refers to a module that aids the exploit module in (typically) returning a shell to the attacker. The payloads are sent together with the exploit itself to bypass standard functioning procedures of the vulnerable service (exploits job) and then run on the target OS to typically return a reverse connection to the attacker and establish a foothold (payload's job).

There are three different types of payload modules in the Metasploit Framework: Singles, Stagers, and Stages. Using three typologies of payload interaction will prove beneficial to the pentester. It can offer the flexibility we need to perform certain types of tasks. Whether or not a payload is staged is represented by / in the payload name.

For example, windows/shell_bind_tcp is a single payload with no stage, whereas windows/shell/bind_tcp consists of a stager (bind_tcp) and a stage (shell).
#### Singles

A Single payload contains the exploit and the entire shellcode for the selected task. Inline payloads are by design more stable than their counterparts because they contain everything all-in-one. However, some exploits will not support the resulting size of these payloads as they can get quite large. Singles are self-contained payloads. They are the sole object sent and executed on the target system, getting us a result immediately after running. A Single payload can be as simple as adding a user to the target system or booting up a process.

#### Stagers
Stager payloads work with Stage payloads to perform a specific task. A Stager is waiting on the attacker machine, ready to establish a connection to the victim host once the stage completes its run on the remote host. Stagers are typically used to set up a network connection between the attacker and victim and are designed to be small and reliable. Metasploit will use the best one and fall back to a less-preferred one when necessary.

Windows NX vs. NO-NX Stagers

    Reliability issue for NX CPUs and DEP
    NX stagers are bigger (VirtualAlloc memory)
    Default is now NX + Win7 compatible

#### Stages
Stages are payload components that are downloaded by stager's modules. The various payload Stages provide advanced features with no size limits, such as Meterpreter, VNC Injection, and others. Payload stages automatically use middle stagers:

    A single recv() fails with large payloads
    The Stager receives the middle stager
    The middle Stager then performs a full download
    Also better for RWX

#### Staged Payloads
A staged payload is, simply put, an exploitation process that is modularized and functionally separated to help segregate the different functions it accomplishes into different code blocks, each completing its objective individually but working on chaining the attack together. This will ultimately grant an attacker remote access to the target machine if all the stages work correctly.

The scope of this payload, as with any others, besides granting shell access to the target system, is to be as compact and inconspicuous as possible to aid with the Antivirus (AV) / Intrusion Prevention System (IPS) evasion as much as possible.

Stage0 of a staged payload represents the initial shellcode sent over the network to the target machine's vulnerable service, which has the sole purpose of initializing a connection back to the attacker machine. This is what is known as a reverse connection. As a Metasploit user, we will meet these under the common names reverse_tcp, reverse_https, and bind_tcp.
