# MSM Webmin Module

## Todo

- Possibly `accept_eula` function to msm.

## UI Functionality Implementation Status

This is a to do list for functionality on the Webmin interface.

(**TODO:** Build the todo list)

## Library Functionality Implementation Status

This is a to do list of functionality implemented at the library level of this
module. An item being checked off here means there is a library function to
handle the action, but there may not be a way to trigger that library function
from the Webmin interface.

### Setup Commands
- [x] Server List (`msm_server_list`)
- [x] Server Create
- [x] Server Delete
- [x] Server Rename

### Server Management Commands

- [x] <server> Start (**has todo** See remaining to do items)
- [x] <server> Stop
- [x] <server> Restart (**has todo** Potentially important error)
- [x] <server> Status
- [x] <server> Connected
- [x] <server> Worlds List
- [x] <server> Worlds Load
- [x] <server> Worlds Ram
- [x] <server> Worlds Todisk
- [x] <server> Worlds Backup
- [x] <server> Worlds On <world>
- [x] <server> Worlds Off <world>
- [x] <server> Logroll
- [x] <server> Backup
- [x] <server> Jar
- [ ] <server> Console
- [ ] <server> Config List
- [ ] <server> Config Set

### Server Pass Through Commands

- [x] <server> Whitelist On
- [x] <server> Whitelist Off
- [x] <server> Whitelist Add
- [x] <server> Whitelist Remove
- [x] <server> Whitelist List
- [x] <server> Blacklist Player Add
- [x] <server> Blacklist Player Remove
- [x] <server> Blacklist IP Add
- [x] <server> Blacklist IP Remove
- [x] <server> Blacklist List
- [x] <server> Operator Add
- [x] <server> Operator Remove
- [x] <server> Operator List
- [x] <server> Gamemode Survival
- [x] <server> Gamemode Creative
- [x] <server> Kick
- [x] <server> Say
- [x] <server> Time Set
- [x] <server> Time Add
- [x] <server> Toggledownfall
- [x] <server> Give
- [x] <server> Xp
- [x] <server> Save On
- [x] <server> Save Off
- [x] <server> Save All
- [x] <server> Cmd
- [x] <server> Cmdlog
 
### Jar Commands

- [x] Jargroup List
- [x] Jargroup Files
- [x] Jargroup Create
- [x] Jargroup Delete
- [x] Jargroup Rename
- [x] Jargroup Changeurl
- [x] Jargroup Getlatest

### Global Commands

- [x] Start
- [x] Stop
- [x] Restart
- [x] Version
- [x] Config
- [x] Update
