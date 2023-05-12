## Uses of Wireshark
-   Detecting and troubleshooting network problems, such as network load failure points and congestion.
-   Detecting security anomalies, such as rogue hosts, abnormal port usage, and suspicious traffic.
-   Investigating and learning protocol details, such as response codes and payload data.


#### The GUI

![image](https://user-images.githubusercontent.com/99975622/236710326-e4928e7c-9716-4213-acf0-48ba94bac503.png)


#### Colouring Packets  

Along with quick packet information, Wireshark also colour packets in order of different conditions and the protocol to spot anomalies and protocols in captures quickly (this explains why almost everything is green in the given screenshots). This glance at packet information can help track down exactly what you're looking for during analysis. You can create custom colour rules to spot events of interest by using display filters, and we will cover them in the next room. Now let's focus on the defaults and understand how to view and use the represented data details.

Wireshark has two types of packet colouring methods: 
- temporary rules that are only available during a program session and 
- permanent rules that are saved under the preference file (profile) and available for the next program session. 

You can use the "right-click menu" or "View --> Coloring Rules" menu to create permanent colouring rules. The "Colourise Packet List" menu activates/deactivates the colouring rules. Temporary packet colouring is done with the "right-click menu" or "View --> Conversation Filter" menu, which is covered in TASK-5.

The default permanent colouring is shown below.

![image](https://user-images.githubusercontent.com/99975622/236710616-db966b86-c288-43cb-b1f4-53d9083f84b0.png)


### Sniffing Traffic
Press the blue shark button to start network sniffing/capturing traffic then press the red button to drop the sniffing. 

The green shark button will restart the sniffing process.

The status bar will also provide the used sniffing interface and the number of collected packets.

#### Merging PCAP Files

You can merge 2 pcap files into one using 'File -> Merge'. This will merge the current file with the one you will select.

You can view the details of a pcap file using 'Statistics --> Capture File Properties'

#### Packet/protocol Dissection

Is where we investigate packet details by decoding available protocols and fields.


**Note:** This section covers how Wireshark uses OSI layers to break down packets and how to use these layers for analysis. It is expected that you already have background knowledge of the OSI model and how it works.

Packets consist of 5 to 7 layers based on the OSI model. We will go over all of them in an HTTP packet from a sample capture.

![Wireshark - packet details](https://tryhackme-images.s3.amazonaws.com/user-uploads/6131132af49360005df01ae3/room-content/22a21052465fedc91fc4d1ec3beb6bd6.png)

**The Frame (Layer 1):** This will show you what frame/packet you are looking at and details specific to the Physical layer of the OSI model.

**Source [MAC] (Layer 2):** This will show you the source and destination MAC Addresses; from the Data Link layer of the OSI model.

**Source [IP] (Layer 3):** This will show you the source and destination IPv4 Addresses; from the Network layer of the OSI model.

**Protocol (Layer 4):** This will show you details of the protocol used (UDP/TCP) and source and destination ports; from the Transport layer of the OSI model.

**Protocol Errors:** This continuation of the 4th layer shows specific segments from TCP that needed to be reassembled.

![Wireshark - protocol error](https://tryhackme-images.s3.amazonaws.com/user-uploads/6131132af49360005df01ae3/room-content/23bbe6ae6e8168cd0662998ff444b067.png)  

**Application Protocol (Layer 5):** This will show details specific to the protocol used, such as HTTP, FTP,  and SMB. From the Application layer of the OSI model.

**Application Data:** This extension of the 5th layer can show the application-specific data.
![Wireshark - application data](https://tryhackme-images.s3.amazonaws.com/user-uploads/6131132af49360005df01ae3/room-content/c2d9c3ce498c6f9044413b68df287c14.png)  


### Packet Analysis

#### Packet Numbers

Wireshark calculates the number of investigated packets and assigns a of unique number for each packet.

#### Go to Packet

This feature not only navigates between packets up and down; it also provides in-frame packet tracking and finds the next packet in the particular part of the conversation. You can use the **"Go"** menu and toolbar to view specific packets.

#### Find Packets

We can find packets using their packet content. You can use the **"Edit --> Find Packet"** menu to make a search inside the packets for a particular event of interest.

There are two crucial points in finding packets;
- knowing the input type which accepts four types of inputs (Display filter, Hex, String and Regex) and 
- choosing the search field. You can conduct searches in the three panes (packet list, packet details, and packet bytes), and it is important to know the available information in each pane to find the event of interest.


#### Marking Packets

You can mark a packet for further investigation by right clicking on the packet and then mark/unmark it. or in the edit tab.

#### Commenting Packets

you can add comments to packets by using the edit tab on your selected packet.

#### Exporting Packets

You can export specific packets from thier unique packet number in the file tab.

#### Exporting Objects/files

We can extract files transffered through the wire.

We can do this on the file tab. (The present files in the pcap file zitatokea)


#### Investigating Packets using Formats

We can arrange the packets for better analysis by time/date format in the view tab.


![image](https://user-images.githubusercontent.com/99975622/236713843-291a0811-54d7-49ec-9d40-1c7f08579fbb.png)


### Packet Filtering

There are 2 filtering approaches;
- capture filters ( are used for **"capturing"** only the packets valid for the used filter.)
- display filters (are used for **"viewing"** the packets valid for the used filter.)



#### Apply as filter
you can right click on Analyse tab and then select apply as Filter option.

You can apply filters using the ip, protocol e.t.c

#### Conversation Filters

Suppose you want to investigate a specific packet number and all linked packets by focusing on IP addresses and port numbers.

This helps us to view related packets to the selected packet.

To do this, right click and  select conversation filter. It is also on the analyse tab.

#### Colourize Conversation

This option is similar to the "Conversation Filter" with one difference.

It highlights the linked packets without applying a display filter and decreasing the number of viewed packets.

It works with the colouring rules option and changes the packet colours without considering the previously applied colour rule.

To use this, right click / use the view tab --> Colourize Conversation.

#### Prepare as Filter

It is almost similar to 'Apply as Filter'.
This option helps analysts create display filters.
This model doesn't apply the filters after the choice.

It adds the required query to the pane and waits for the execution command (enter) or another chosen filtering option by using the **".. and/or.."** from the "right-click menu".

![Wireshark - prepare as filter](https://tryhackme-images.s3.amazonaws.com/user-uploads/6131132af49360005df01ae3/room-content/0291e6095277eaebf8f9a8f8df0f1ec6.png)


#### Apply as Column

By default, the packet list pane provides basic information about each packet. You can use the "right-click menu" or "Analyse **-->**  Apply as Column" menu to add columns to the packet list pane. Once you click on a value and apply it as a column, it will be visible on the packet list pane. This function helps analysts examine the appearance of a specific value/field across the available packets in the capture file. You can enable/disable the columns shown in the packet list pane by clicking on the top of the packet list pane.

![Wireshark - apply as column](https://tryhackme-images.s3.amazonaws.com/user-uploads/6131132af49360005df01ae3/room-content/8eac68abb9c10fccce114f6ad803a5dd.png)

#### Follow Stream

Following the protocol, streams help analysts recreate the application-level data and understand the event of interest. It is also possible to view the unencrypted protocol data like usernames, passwords and other transferred data.

You can use the"right-click menu" or  **"Analyse** **--> Follow TCP/UDP/HTTP Stream"** menu to follow traffic streams. Streams are shown in a separate dialogue box; packets originating from the server are highlighted with blue, and those originating from the client are highlighted with red.

  
![Wireshark - follow stream](https://tryhackme-images.s3.amazonaws.com/user-uploads/6131132af49360005df01ae3/room-content/d578e89a1f4a526fb8ede6fdf1a5f1b5.png)

