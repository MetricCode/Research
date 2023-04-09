## AD Functionality
![image](https://user-images.githubusercontent.com/99975622/230773324-7ce0079c-6ff1-4cf9-aaff-a8aee910a276.png)

### Domain and Forest Functional Levels
Functional levels are used to determine the various features and capabilities available in Active Directory Domain Services (AD DS) at the domain and forest level.

They are also used to specify which Windows Server operating systems can run a Domain Controller in a domain or forest.

Below is a quick overview of the differences in `domain functional levels` from Windows 2000 native up to Windows Server 2016, aside from all default Active Directory Directory Services features from the level just below it (or just the default AD DS features in the case of Windows 2000 native.)

![image](https://user-images.githubusercontent.com/99975622/230773517-c50c00aa-34b7-4fef-8fee-53650a27308d.png)

A new functional level was not added with the release of Windows Server 2019. However, Windows Server 2008 functional level is the minimum requirement for adding Server 2019 Domain Controllers to an environment. Also, the target domain has to use [DFS-R](https://docs.microsoft.com/en-us/windows-server/storage/dfs-replication/dfsr-overview) for SYSVOL replication.

![image](https://user-images.githubusercontent.com/99975622/230773578-5144ce82-a681-4e49-8e47-8fc614d52edf.png)

---

### Trusts

A trust is used to establish `forest-forest` or `domain-domain` authentication, allowing users to access resources in (or administer) another domain outside of the domain their account resides in. A trust creates a link between the authentication systems of two domains.

![image](https://user-images.githubusercontent.com/99975622/230773699-c6299530-4d77-498c-b8a4-3a77ad6d54ff.png)
#### Trust Example
![[Pasted image 20230409155506.png]]

Trusts can be transitive or non-transitive.

-   A transitive trust means that trust is extended to objects that the child domain trusts.
-   In a non-transitive trust, only the child domain itself is trusted.

Trusts can be set up to be one-way or two-way (bidirectional).

-   In bidirectional trusts, users from both trusting domains can access resources.
-   In a one-way trust, only users in a trusted domain can access resources in a trusting domain, not vice-versa. The direction of trust is opposite to the direction of access.
