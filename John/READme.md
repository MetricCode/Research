# John-The-Ripper!
## @Author : M3tr1c_r00t

we can use hash-id if we dont know the hash type.

### Format specific cracking
```
john --format=[format] --wordlist=[path to wordlist] [path to file]
```

we can search for format's using...
```
john --list=formats | grep -iF "md5"
```

### Cracking Windows Hashes
##### nthash/ntlm
NThash is the hash format that modern Windows Operating System machines will store user and service passwords in. It's also commonly referred to as "NTLM" which references the previous version of Windows format for hashing passwords known as "LM", thus "NT/LM".

You can acquire NTHash/NTLM hashes by dumping the SAM database on a Windows machine, by using a tool like Mimikatz or from the Active Directory database: NTDS.dit. You may not have to crack the hash to continue privilege escalation- as you can often conduct a "pass the hash" attack instead, but sometimes hash cracking is a viable option if there is a weak password policy.

#### Cracking Hashes from /etc/shadow
#### Unshadowing

John can be very particular about the formats it needs data in to be able to work with it, for this reason- in order to crack /etc/shadow passwords, you must combine it with the /etc/passwd file in order for John to understand the data it's being given. To do this, we use a tool built into the John suite of tools called unshadow. The basic syntax of unshadow is as follows:
```
unshadow [path to passwd] [path to shadow]

`unshadow` - Invokes the unshadow tool  

`[path to passwd]` - The file that contains the copy of the /etc/passwd file

`[path to shadow]` - The file that contains the copy of the /etc/shadow file

unshadow local_passwd local_shadow > unshadowed.txt
```

Its not a must to provide a format but if john complains...
```
john --wordlist=/usr/share/wordlists/rockyou.txt --format=sha512crypt unshadowed.txt
```

#### Single Crack Mode
In this mode, John uses only the information provided in the username, to try and work out possible passwords heuristically, by slightly changing the letters and numbers contained within the username.

##### Word Mangling  

The best way to show what Single Crack mode is,  and what word mangling is, is to actually go through an example:

If we take the username: Markus

Some possible passwords could be:

-   Markus1, Markus2, Markus3 (etc.)
-   MArkus, MARkus, MARKus (etc.)
-   Markus!, Markus$, Markus* (etc.)

This technique is called word mangling. John is building it's own dictionary based on the information that it has been fed and uses a set of rules called "mangling rules" which define how it can mutate the word it started with to generate a wordlist based off of relevant factors for the target you're trying to crack. This is exploiting how poor passwords can be based off of information about the username, or the service they're logging into.  

##### Using Single Crack Mode

To use single crack mode, we use roughly the same syntax that we've used to so far, for example if we wanted to crack the password of the user named "Mike", using single mode, we'd use:  

`john --single --format=[format] [path to file]`

**Example Usage:**

john --single --format=raw-sha256 hashes.txt

**A Note on File Formats in Single Crack Mode:**

If you're cracking hashes in single crack mode, you need to change the file format that you're feeding john for it to understand what data to create a wordlist from. You do this by prepending the hash with the username that the hash belongs to, so according to the above example- we would change the file hashes.txt

**From:**  

1efee03cdcb96d90ad48ccc7b8666033

**To**

mike:1efee03cdcb96d90ad48ccc7b8666033

### Custom Rules
They help us exploit Password complexity predictability
In this, you can define your own sets of rules, which John will use to dynamically create passwords. This is especially useful when you know more information about the password structure of whatever your target is.

#### Creating Custom rules
Custom rules are defined in the `john.conf` file, usually located in `/etc/john/john.conf`

he first line:

`[List.Rules:THMRules]` - Is used to define the name of your rule, this is what you will use to call your custom rule as a John argument.

`Az` - Takes the word and appends it with the characters you define  

`A0` - Takes the word and prepends it with the characters you define  

`c` - Capitalises the character positionally
  
These can be used in combination to define where and what in the word you want to modify.

Lastly, we then need to define what characters should be appended, prepended or otherwise included, we do this by adding character sets in square brackets `[ ]` in the order they should be used. These directly follow the modifier patterns inside of double quotes `" "`. Here are some common examples:
  
`[0-9]` - Will include numbers 0-9  

`[0]` - Will include only the number 0  

`[A-z]` - Will include both upper and lowercase  

`[A-Z]` - Will include only uppercase letters  

`[a-z]` - Will include only lowercase letters  

`[a]` - Will include only a  

`[!£$%@]` - Will include the symbols !£$%@  
 
Putting this all together, in order to generate a wordlist from the rules that would match the example password "Polopassword1!" (assuming the word polopassword was in our wordlist) we would create a rule entry that looks like this:

`[List.Rules:PoloPassword]`

`cAz"[0-9] [!£$%@]"`

In order to:
- Capitalise the first  letter - `c`
- Append to the end of the word - `Az`
- A number in the range 0-9 - `[0-9]`
- Followed by a symbol that is one of `[!£$%@]`

After defining your rule, we can use it ...
```
john --wordlist=[path to wordlist] --rule=PoloPassword [path to file]
```

### Cracking zip files
#### zip2john 
```zip2john [options] [zip file] > [output file]```

```john --wordlist=/usr/share/wordlists/rockyou.txt zip_hash.txt```

### Cracking RAR files
```
rar2john [rar file] > [output file]
```

```
john --wordlist=/usr/share/wordlists/rockyou.txt rar_hash.txt
```

to open rar files
```
apt install rar
apt install unrar
unrar e FILE
```

### Cracking SSH keys

```
ssh2john [id_rsa private key file] > [output file]
```
```
john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa_hash.txt
```

### Cracking keepass database

```
keepass2john file.kdbx > hash

john --wordlist=/usr/share/wordlists/rockyou.txt ihash.txt
```

## My socials:
<br>@ twitter: https://twitter.com/M3tr1c_root
<br>@ instagram: https://instagram.com/m3tr1c_r00t/
