# Kerberos
## _@Author : M3tr1c_r00t_

Kerberos is a network security protocol that authenticates service requests between trusted hosts across the internet(as it is considered unsecure). 

It uses secret-key cryptography and a trusted third party for authenticating client-server applications and verifying users' identities.

The protocol derives its name from the legendary three-headed dog Kerberos (also known as Cerberus) from Greek myths, the canine guardian to the entrance to the underworld. Kerberos had a snake tail and a particularly bad temper and, despite one notable exception, was a very useful guardian.

The three heads of the Kerberos protocol represent the following:
- the client or principal;
- the network resource, which is the application server that provides access to the network resource; and;
- a key distribution center (KDC), which acts as Kerberos' trusted third-party authentication service.

### How Kerberos works
Users, machines, and services that use Kerberos depend on the KDC alone, which works as a single process that provides two functions: authentication and ticket-granting. 
KDC "tickets" offer authentication to all parties, allowing nodes to verify their identity securely.

#### Traditional network protocols...
Before Kerberos, networked systems typically authenticated users with a user ID and password combination. The transmitted credentials were then transmitted over the unsafe and unsecure internet without any security/encryption. Therefore, attackers with access to the network could easily eavesdrop on network transmissions, intercept user credentials and then attempt to access systems.

To try and cater for this vulnerability, kerberos developers intended to provide system administrators a mechanism for authenticating access to systems over the internet.

 Kerberos is used in Posix authentication, and Active Directory, NFS, and Samba. It's also an alternative authentication system to SSH, POP, and SMTP.

#### Kerberos Authentication...
