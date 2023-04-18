## Port Forwarding
Port forwarding is an essential component in connecting applications and services to the Internet. Without port forwarding, applications and services such as web servers are only available to devices within the same direct network.

Port forwarding is configured at the router of a network.

## Firewall

A firewall is a device within a network responsible for determining what traffic is allowed to enter and exit

An administrator can configure a firewall to **permit** or **deny** traffic from entering or exiting a network based on numerous factors such as:
- Where the traffic is coming from? (has the firewall been told to accept/deny traffic from a specific network?)
- Where is the traffic going to? (has the firewall been told to accept/deny traffic destined for a specific network?)
- What port is the traffic for? (has the firewall been told to accept/deny traffic destined for port 80 only?)
- What protocol is the traffic using? (has the firewall been told to accept/deny traffic that is UDP, TCP or both?)

Firewalls perform packet inspection to determine the answers to these questions.

Firewalls come in all shapes and sizes. From dedicated pieces of hardware (often found in large networks like businesses) that can handle a magnitude of data to residential routers (like at your home!) or software such as [Snort](https://www.snort.org/), firewalls can be categorised into 2 to 5 categories.

### Types of Firewalls

![image](https://user-images.githubusercontent.com/99975622/232858545-634fdfb5-82dc-44d6-bb90-5cf3f72e0183.png)

Firewalls operate on layer 3 and 4.

## VPN (Virtual Private Network)
is a technology that allows devices on separate networks to communicate securely by creating a dedicated path between each other over the Internet (known as a tunnel). Devices connected within this tunnel form their own private network.

#### Benefits of a VPN
![image](https://user-images.githubusercontent.com/99975622/232860121-b4dc323f-83e0-49ef-905a-d0e7dc4a8c6f.png)


### VPN technology
![image](https://user-images.githubusercontent.com/99975622/232860372-bdcfad2d-a18f-4738-8ae2-f79f5441813c.png)

## LAN Networking Devices
### Routing
It's a router's job to connect networks and pass data between them. It does this by using routing (hence the name router!).

Routing is the label given to the process of data travelling across networks. Routing involves creating a path between networks so that this data can be successfully delivered. Routers operate at Layer 3 of the OSI model. They often feature an interactive interface (such as a website or a console) that allows an administrator to configure various rules such as port forwarding or firewalling.

Routers are dedicated devices and do not perform the same functions as switches.

### Switch
A switch is a dedicated networking device responsible for providing a means of connecting to multiple devices. Switches can facilitate many devices (from 3 to 63) using Ethernet cables.

Switches can operate at both layer 2 and layer 3 of the OSI model. However, these are exclusive in the sense that Layer 2 switches cannot operate at layer 3.

Take, for example, a layer 2 switch in the diagram below. These switches will forward frames (remember these are no longer packets as the IP protocol has been stripped) onto the connected devices using their MAC address.

  

![](https://assets.tryhackme.com/additional/networking-fundamentals/extending-your-network/layer2switch.png)

These switches are solely responsible for sending frames to the correct device.

Now, let's move onto layer 3 switches. These switches are more sophisticated than layer 2, as they can perform _some_ of the responsibilities of a router. Namely, these switches will send frames to devices (as layer 2 does) and route packets to other devices using the IP protocol. 

  

Let's take a look at the diagram below of a layer 3 switch in action. We can see that there are two IP addresses: 

-   192.168.1.1
-   192.168.2.1

A technology called **VLAN** (**V**irtual **L**ocal **A**rea **N**etwork) allows specific devices within a network to be virtually split up. This split means they can all benefit from things such as an Internet connection but are treated separately. This network separation provides security because it means that rules in place determine how specific devices communicate with each other. This segregation is illustrated in the diagram below:

![](https://assets.tryhackme.com/additional/networking-fundamentals/extending-your-network/vlans.png)  

In the context of the diagram above, the "Sales Department" and "Accounting Department" will be able to access the Internet, but not able to communicate with each other (although they are connected to the same switch).
