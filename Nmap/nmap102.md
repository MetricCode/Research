- TCP/UDP ports specify the type of service running on the network.
- Ports are in 2 simple states; open and closed.
- However, nmap configured the following states;
	- open- a service is listening
	- Closed - Indicates no service are listening.
	- Filtered - nmap cannot determine whether a service is open or not.
	- Unfiltered - nmap cannot determine the port if open or closed though the port is accessible.(is usually encountered when using -sA) 
	- Open | Filtered - nmap cannot determine whether the port is open or filtered
	- Closed | Filtered - nmap cannot determine whether the port is closed or filtered.

#### TCP scans
-  The TCP header is the first 24 bytes of a TCP segment.
- The following figure shows the TCP header as defined in [RFC 793](https://datatracker.ietf.org/doc/html/rfc793.html). This figure looks sophisticated at first; however, it is pretty simple to understand. In the first row, we have the source TCP port number and the destination port number. We can see that the port number is allocated 16 bits (2 bytes). In the second and third rows, we have the sequence number and the acknowledgement number. Each row has 32 bits (4 bytes) allocated, with six rows total, making up 24 bytes.

![image](https://github.com/MetricCode/Research/assets/99975622/60ef59d2-1b1b-4428-8545-55ad2ba57904)

In particular, we need to focus on the flags that Nmap can set or unset. We have highlighted the TCP flags in red. Setting a flag bit means setting its value to 1. From left to right, the TCP header flags are:

1. **URG**: Urgent flag indicates that the urgent pointer filed is significant. The urgent pointer indicates that the incoming data is urgent, and that a TCP segment with the URG flag set is processed immediately without consideration of having to wait on previously sent TCP segments.
2. **ACK**: Acknowledgement flag indicates that the acknowledgement number is significant. It is used to acknowledge the receipt of a TCP segment.
3. **PSH**: Push flag asking TCP to pass the data to the application promptly.
4. **RST**: Reset flag is used to reset the connection. Another device, such as a firewall, might send it to tear a TCP connection. This flag is also used when data is sent to a host and there is no service on the receiving end to answer.
5. **SYN**: Synchronize flag is used to initiate a TCP 3-way handshake and synchronize sequence numbers with the other host. The sequence number should be set randomly during TCP connection establishment.
6. **FIN**: The sender has no more data to send

- To run a connect tcp scan, we can use -sT(This works using the 3 way handshake)(This needs the root/sudoers user to run it.)
- As the connect tcp scan is limited, we can use a TCP SYN scan using -sS.(This is the default one run by nmap)

#### UDP scans
- UDP is a connectionless protocol, and hence it does not require any handshake for connection establishment.
- We cannot guarantee that a service listening on a UDP port would respond to our packets. However, if a UDP packet is sent to a closed port, an ICMP port unreachable error (type 3, code 3) is returned.
- We can scan for udp ports using -sU.

#### Timing

You can control the scan timing using `-T<0-5>`. `-T0` is the slowest (paranoid), while `-T5` is the fastest. According to Nmap manual page, there are six templates:

- paranoid (0)
- sneaky (1)
- polite (2)
- normal (3)
- aggressive (4)
- insane (5)

Alternatively, you can choose to control the packet rate using `--min-rate <number>` and `--max-rate <number>`. For example, `--max-rate 10` or `--max-rate=10` ensures that your scanner is not sending more than ten packets per second.

Moreover, you can control probing parallelization using `--min-parallelism <numprobes>` and `--max-parallelism <numprobes>`. Nmap probes the targets to discover which hosts are live and which ports are open; probing parallelization specifies the number of such probes that can be run in parallel. For instance, `--min-parallelism=512` pushes Nmap to maintain at least 512 probes in parallel; these 512 probes are related to host discovery and open ports.

![image](https://github.com/MetricCode/Research/assets/99975622/45acb9ad-8e51-4ff9-a5c1-85b6f9a8fd0b)

