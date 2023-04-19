## File System
- Windows uses NTFS(New Technology File System ) in its modern versions.
- Before NTFS there was FAT16/FAT32(File Allocation Table) and HPFS(High Performance File System)

NTFS is known as a journaling file system. In case of a failure, the file system can automatically repair the folders/files on disk using information stored in a log file which is not available in FAT.

NTFS addresses many of the limitations of the previous file systems; such as: 

-   Supports files larger than 4GB
-   Set specific permissions on folders and files
-   Folder and file compression
-   Encryption ([Encryption File System](https://docs.microsoft.com/en-us/windows/win32/fileio/file-encryption) or **EFS**)

On NTFS volumes, you can set permissions that grant or deny access to files and folders.
The permissions are:

-   **Full control**
-   **Modify**
-   **Read & Execute**
-   **List folder contents**
-   **Read**
-   **Write**

  
![](https://assets.tryhackme.com/additional/win-fun1/ntfs-permissions1.png)


Another feature of NTFS is **Alternate Data Streams** (**ADS**).  

Alternate Data Streams (ADS) is a file attribute specific to Windows NTFS (New Technology File System).

Every file has at least one data stream (`$DATA`), and ADS allows files to contain more than one stream of data. Natively [Window Explorer](https://support.microsoft.com/en-us/windows/what-s-changed-in-file-explorer-ef370130-1cca-9dc5-e0df-2f7416fe1cb1) doesn't display ADS to the user. There are 3rd party executables that can be used to view this data, but [Powershell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1) gives you the ability to view ADS for files.
