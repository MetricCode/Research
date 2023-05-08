Forensics is the application of science to investigate crimes and establish facts. With the use and spread of digital systems, such as computers and smartphones, a new branch of forensics was born to investigate related crimes: computer forensics, which later evolved into, _digital forensics_.

More formally, digital forensics is the application of computer science to investigate digital evidence for a legal purpose. Digital forensics is used in two types of investigations:

1.  **Public-sector investigations** refer to the investigations carried out by government and law enforcement agencies. They would be part of a crime or civil investigation.
2.  **Private-sector investigations** refer to the investigations carried out by corporate bodies by assigning a private investigator, whether in-house or outsourced. They are triggered by corporate policy violations.

### Digital Forensics Process

After getting the proper legal authorization, the basic plan goes as follows:

1.  Acquire the evidence: Collect the digital devices such as laptops, storage devices, and digital cameras. (Note that laptops and computers require special handling if they are turned on; however, this is outside the scope of this room.)
2.  Establish a chain of custody: Fill out the related form appropriately ([Sample form](https://www.nist.gov/document/sample-chain-custody-formdocx)). The purpose is to ensure that only the authorized investigators had access to the evidence and no one could have tampered with it.
3.  Place the evidence in a secure container: You want to ensure that the evidence does not get damaged. In the case of smartphones, you want to ensure that they cannot access the network, so they don’t get wiped remotely.
4.  Transport the evidence to your digital forensics lab.

At the lab, the process goes as follows:

1.  Retrieve the digital evidence from the secure container.
2.  Create a forensic copy of the evidence: The forensic copy requires advanced software to avoid modifying the original data.
3.  Return the digital evidence to the secure container: You will be working on the copy. If you damage the copy, you can always create a new one.
4.  Start processing the copy on your forensics workstation.

The above steps have been adapted from [Guide to Computer Forensics and Investigations, 6th Edition](https://www.cengage.uk/shop/isbn/9781337568944).

More generally, according to the former director of the Defense Computer Forensics Laboratory, Ken Zatyko, digital forensics includes:

-   Proper search authority: Investigators cannot commence without the proper legal authority.
-   Chain of custody: This is necessary to keep track of who was holding the evidence at any time.
-   Validation with mathematics: Using a special kind of mathematical function, called a hash function, we can confirm that a file has not been modified.
-   Use of validated tools: The tools used in digital forensics should be validated to ensure that they work correctly. For example, if you are creating an image of a disk, you want to ensure that the forensic image is identical to the data on the disk.
-   Repeatability: The findings of digital forensics can be reproduced as long as the proper skills and tools are available.
-   Reporting: The digital forensics investigation is concluded with a report that shows the evidence related to the case that was discovered.


When you create a text file, `TXT`, some metadata gets saved by the Operating System, such as file creation date and last modification date. However, much information gets kept within the file’s metadata when you use a more advanced editor, such as MS Word. There are various ways to read the file metadata; you might open them within their official viewer/editor or use a suitable forensic tool. Note that exporting the file to other formats, such as `PDF`, would maintain most of the metadata of the original document, depending on the PDF writer used.


We can try to read the metadata using the program `pdfinfo`. Pdfinfo displays various metadata related to a PDF file, such as title, subject, author, creator, and creation date.

## Security Operations

### Intro To Security Operations

A _Security Operations Center_ (SOC) is a _team_ of IT security professionals tasked with monitoring a company’s network and systems 24 hours a day, seven days a week. Their purpose of monitoring is to:

-   **Find vulnerabilities on the network**: A _vulnerability_ is a weakness that an attacker can exploit to carry out things beyond their permission level. A vulnerability might be discovered in any device’s software (operating system and programs) on the network, such as a server or a computer. For instance, the SOC might discover a set of MS Windows computers that must be patched against a specific published vulnerability. Strictly speaking, vulnerabilities are not necessarily the SOC’s responsibility; however, unfixed vulnerabilities affect the security level of the entire company.
  
-   **Detect unauthorized activity**: Consider the case where an attacker discovered the username and password of one of the employees and used it to log in to the company system. It is crucial to detect this kind of unauthorized activity quickly before it causes any damage. Many clues can help us detect this, such as geographic location.
  
-   **Discover policy violations**: A _security policy_ is a set of rules and procedures created to help protect a company against security threats and ensure compliance. What is considered a violation would vary from one company to another; examples include downloading pirated media files and sending confidential company files insecurely.
  
-   **Detect intrusions**: _Intrusions_ refer to system and network intrusions. One example scenario would be an attacker successfully exploiting our web application. Another example scenario would be a user visiting a malicious site and getting their computer infected.
  
-   **Support with the incident response**: An _incident_ can be an observation, a policy violation, an intrusion attempt, or something more damaging such as a major breach. Responding correctly to a severe incident is not an easy task. The SOC can support the incident response team handle the situation.


### Data Sources

The SOC uses many data sources to monitor the network for signs of intrusions and to detect any malicious behaviour. Some of these sources are:

-   **Server logs**: There are many types of servers on a network, such as a mail server, web server, and domain controller on MS Windows networks. Logs contain information about various activities, such as successful and failed login attempts, among many others. There is a trove of information that can be found in the server logs.
-   **DNS activity**: DNS stands for Domain Name System, and it is the protocol responsible for converting a domain name, such as `tryhackme.com`, to an IP address, such as `10.3.13.37`, among other domain name related queries. One analogy of the DNS query is asking, “How can I reach TryHackMe?” and someone replying with the postal address. In practice, if someone tries to browse `tryhackme.com`, the DNS server has to resolve it and can log the DNS query to monitoring. The SOC can gather information about domain names that internal systems are trying to communicate with by merely inspecting DNS queries.
-   **Firewall logs**: A firewall is a device that controls network packets entering and leaving the network mainly by letting them through or blocking them. Consequently, firewall logs can reveal much information about what packets passed or tried to pass through the firewall.
-   **DHCP logs**: DHCP stands for Dynamic Host Configuration Protocol, and it is responsible for assigning an IP address to the systems that try to connect to a network. One analogy of the DHCP request would be when you enter a fancy restaurant, and the waiter welcomes you and guides you to an empty table. Know that DHCP has automatically provided your device with the network settings whenever you can join a network without manual configuration. By inspecting DHCP transactions, we can learn about the devices that joined the network.


### SOC Services

SOC services include reactive and proactive services in addition to other services.

Reactive services refer to the tasks initiated after detecting an intrusion or a malicious event. Example reactive services include:

-   **Monitor security posture**: This is the primary role of the SOC, and it includes monitoring the network and computers for security alerts and notifications and responding to them as the need dictates.
-   **Vulnerability management**: This refers to finding vulnerabilities in the company systems and patching (fixing) them. The SOC can assist with this task but not necessarily execute it.
-   **Malware analysis**: The SOC might recover malicious programs that reached the network. The SOC can do basic analysis by executing it in a controlled environment. However, more advanced analysis requires sending it to a dedicated team.
-   **Intrusion detection**: An _intrusion detection system_ (IDS) is used to detect and log intrusions and suspicious packets. The SOC’s job is to maintain such a system, monitor its alerts, and go through its logs as the need dictates.
-   **Reporting**: It is essential to report incidents and alarms. Reporting is necessary to ensure a smooth workflow and to support compliance requirements.

Proactive services refer to the tasks handled by the SOC without any indicator of an intrusion. Example proactive services carried out by the SOC include:

-   **Network security monitoring (NSM)**: This focuses on monitoring the network data and analyzing the traffic to detect signs of intrusions.
-   **Threat hunting**: With _threat hunting_, the SOC assumes an intrusion has already taken place and begins its hunt to see if they can confirm this assumption.
-   **Threat Intelligence**: Threat intelligence focuses on learning about potential adversaries and their tactics and techniques to improve the company’s defences. The purpose would be to establish a _threat-informed defence_.

Other services by the SOC include **cyber security training**. Many data breaches and intrusions can be avoided by raising users’ security awareness and arming them with solid security training.
