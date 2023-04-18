Packets and frames are small pieces of data that, when forming together, make a larger piece of information or message.

A packet usually has the IP address in the Internet Protocol while a frame doesnt

Though in the OSI model, a frame is at layer 2 - the data link layer, meaning there is no such information as IP addresses.

For example, when loading an image from a website, this image is not sent to your computer as a whole, but rather small pieces where it is reconstructed on your computer. Take the image below as an illustration of this process. The dog's picture is divided into three packets, where it is reconstructed when it reaches the computer to form the final image.

Packets have different structures that are dependant upon the type of packet that is being sent


### Three Way Handshake(TCP/IP)

The TCP/IP protocol consists of four layers. These layers are:

-   Application
-   Transport
-   Internet
-   Network Interface

Information is added to each layer of the TCP model as the piece of data (or packet) traverses it.

One defining feature of TCP is that it is **connection-based**, which means that TCP must establish a connection between both a client and a device acting as a server **before** data is sent. Because of this, TCP guarantees that any data sent will be received on the other end.

#### Pros of TCP
- Guarantees data integrity
- Is capable of snycing 2 devices to prevent each other from being flooded with data in the wrong order.
- Performs a lot more processes for reliability

#### Cons of TCP
- Requires a reliable connection between the two devices. If one small chunk of data is not received, then the entire chunk of data cannot be used and must be re-sent.
- A slow connection can bottleneck another device as the connection will be reserved on the other device the whole time.
- TCP is significantly slower than UDP because more work (computing) has to be done by the devices using this protocol.

#### Information found in a TCP packet
![image](https://user-images.githubusercontent.com/99975622/232794975-07ee6df6-563e-4b74-b85b-92b340d43fd8.png)


#### Three way handshake

![image](https://user-images.githubusercontent.com/99975622/232795346-7d81fb45-be98-410e-af62-cdb4e6c0382c.png)


#### Closing the TCP connection
- Fin
- Fin/Ack
- Ack


#### UDP/IP
User Datagram Protocol

UDP is a **stateless** protocol that doesn't require a constant connection between the two devices for data to be sent.

In this, the three way handshake does not occur and no syncing occurs.

#### Pros of UDP
- Is faster than TCP
- Leaves the application (user software) to decide if there is any control over how quickly packets are sent.
- Does not reserve a continuous connection on a device as TCP does.

##### Cons of UDP
- doesnt care if data is recieved or not
- is quite flexible to software developers in this sense
- This means that unstable connections result in a terrible experience for the user. 

UDP packets are much simpler than TCP packets and have fewer headers.

We should recall that UDP is **stateless**. No acknowledgement is sent during a connection.

#### UDP headers
![[Pasted image 20230418170323.png]]
