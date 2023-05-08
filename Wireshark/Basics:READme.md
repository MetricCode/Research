
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

