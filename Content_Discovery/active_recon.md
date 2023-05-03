## Web Broswer
The web browser can be a convenient tool, especially that it is readily available on all systems. There are several ways where you can use a web browser to gather information about a target.

On the transport level, the browser connects to:

-   TCP port 80 by default when the website is accessed over HTTP
-   TCP port 443 by default when the website is accessed over HTTPS

### Developer tools.
We can access this by pressing Ctrl+Shift+I .
### Extensions
We can also use some extensions such as;
- FoxyProxy
- Wappalyzer

## Ping
- Ping can be used to check if you can reach the remote system and that it can reach you back.
-  ping is a command that sends an ICMP Echo packet to a remote system. If the remote system is online, and the ping packet was correctly routed and not blocked by any firewall, the remote system should send back an ICMP Echo Reply.

## Traceroute
The traceroute command _traces the route_ taken by the packets from your system to another host. The purpose of a traceroute is to find the IP addresses of the routers or hops that a packet traverses as it goes from your system to a target host.

- It can be used to reveal the number of routers between 2 systems.
- However, note that the route taken by the packets might change as many routers use dynamic routing protocols that adapt to network changes.

There is no direct way to discover the path from your system to a target system. We rely on ICMP to “trick” the routers into revealing their IP addresses. We can accomplish this by using a small Time To Live (TTL) in the IP header field.

`traceroute` will start by sending UDP datagrams within IP packets of TTL being 1. Thus, it causes the first router to encounter a TTL=0 and send an ICMP Time-to-Live exceeded back. Hence, a TTL of 1 will reveal the IP address of the first router to you. Then it will send another packet with TTL=2; this packet will be dropped at the second router. And so on. Let’s try this on live systems.

## Telnet
telnet command uses the telnet protocok for remote administation. 
It's default port is 23.
The downside of telnet is that the data was being sent without being encrypted.

However, the telnet client, with its simplicity, can be used for other purposes. Knowing that telnet client relies on the TCP protocol, you can use Telnet to connect to any service and grab its banner. Using `telnet MACHINE_IP PORT`, you can connect to any service running on TCP and even exchange a few messages unless it uses encryption.

## Netcat
 Netcat supports both TCP and UDP protocols. 
 
 It can function as a client that connects to a listening port; alternatively, it can act as a server that listens on a port of your choice. 
 
 Hence, it is a convenient tool that you can use as a simple client or server over TCP or UDP.

to collect a server's banner use  `nc MACHINE_IP PORT`
