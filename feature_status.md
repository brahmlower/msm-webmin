
This is a status overview of MSM features that have been implemented in the
MSM wrapper library, and the Webmin user interface. Some features may take
more time and energy to accomplish, and will be delayed until later releases.

- ✅ Complete
- ⚠️ Partial
- ❌ Missing or broken

## Setup Commands

| Feature       | Library | Webmin UI |
|---------------|---------|-----------|
| Server List   | ✅ [docs](library#msm_server_list)   | ✅ |
| Server Create | ✅ [docs](library#msm_server_create) | ✅ |
| Server Delete | ✅ [docs](library#msm_server_delete) | ✅ |
| Server Rename | ✅ [docs](library#msm_server_rename) | ✅ |

## Server Management Commands

| Feature       | Library | Webmin UI |
|---------------|---------|-----------|
| Start         | ⚠️ [docs](library#msm_server_start)         | ✅ |
| Stop          | ✅ [docs](library#msm_server_stop)          | ✅ |
| Restart       | ⚠️ [docs](library#msm_server_start)         | ✅ |
| Status        | ✅ [docs](library#msm_server_status)        | ✅ |
| Connected     | ✅ [docs](library#msm_server_connected)     | ✅ |
| Worlds List   | ✅ [docs](library#msm_server_worlds_list)   | ❌ |
| Worlds Load   | ✅ [docs](library#msm_server_worlds_load)   | ❌ |
| Worlds Ram    | ✅ [docs](library#msm_server_worlds_ram)    | ❌ |
| Worlds Todisk | ✅ [docs](library#msm_server_worlds_todisk) | ❌ |
| Worlds Backup | ✅ [docs](library#msm_server_worlds_backup) | ❌ |
| Worlds On     | ✅ [docs](library#msm_server_worlds_on)     | ❌ |
| Worlds Off    | ✅ [docs](library#msm_server_worlds_off)    | ❌ |
| Logroll       | ✅ [docs](library#msm_server_logroll)       | ✅ |
| Backup        | ✅ [docs](library#msm_server_backup)        | ✅ |
| Jar           | ✅ [docs](library#msm_server_jar)           | ❌ |
| Console       | ❌ | ❌ |
| Config List   | ❌ | ❌ |
| Config Set    | ❌ | ❌ |

## Server Pass Through Commands

| Feature                 | Library | Webmin UI |
|-------------------------|---------|-----------|
| Whitelist On            | ✅ [docs](library#msm_server_start)          | ❌ |
| Whitelist Off           | ✅ [docs](library#msm_server_start)          | ❌ |
| Whitelist Add           | ✅ [docs](library#msm_server_start)          | ✅ |
| Whitelist Remove        | ✅ [docs](library#msm_server_start)          | ✅ |
| Whitelist List          | ✅ [docs](library#msm_server_start)          | ⚠️ (Possible MSM bug) |
| Blacklist Player Add    | ✅ [docs](library#msm_server_start)          | ✅ |
| Blacklist Player Remove | ✅ [docs](library#msm_server_start)          | ✅ |
| Blacklist IP Add        | ✅ [docs](library#msm_server_start)          | ❌ |
| Blacklist IP Remove     | ✅ [docs](library#msm_server_start)          | ❌ |
| Blacklist List          | ✅ [docs](library#msm_server_start)          | ⚠️ (Possible MSM bug) |
| Operator Add            | ✅ [docs](library#msm_server_start)          | ✅ |
| Operator Remove         | ✅ [docs](library#msm_server_start)          | ✅ |
| Operator List           | ✅ [docs](library#msm_server_start)          | ⚠️ [Possible MSM bug](https://github.com/bplower/webmin-minecraft-server-manager/issues/1) |
| Gamemode Survival       | ✅ [docs](library#msm_server_gm_survival)    | ❌ |
| Gamemode Creative       | ✅ [docs](library#msm_server_gm_creative)    | ❌ |
| Kick                    | ✅ [docs](library#msm_server_kick)           | ✅ |
| Say                     | ✅ [docs](library#msm_server_say)            | ✅ |
| Time Set                | ✅ [docs](library#msm_server_time_set)       | ✅ |
| Time Add                | ✅ [docs](library#msm_server_time_add)       | ✅ |
| Toggle Downfall         | ✅ [docs](library#msm_server_toggledownfall) | ✅ |
| Give                    | ✅ [docs](library#msm_server_give)           | ✅ |
| Xp                      | ✅ [docs](library#msm_server_xp)             | ✅ |
| Save On                 | ✅ [docs](library#msm_server_save_on)        | ❌ |
| Save Off                | ✅ [docs](library#msm_server_save_off)       | ❌ |
| Save All                | ✅ [docs](library#msm_server_save_all)       | ❌ |
| Cmd                     | ✅ [docs](library#msm_server_cmd)            | ✅ |
| Cmd Log                 | ✅ [docs](library#msm_server_cmdlog)         | ❌ |

## Jar Commands

| Feature             | Library | Webmin UI |
|---------------------|---------|-----------|
| Jargroup List       | ✅ [docs](library#msm_jargroup_list)      | ✅ |
| Jargroup Files      | ✅ [docs](library#msm_jargroup_files)     | ✅ |
| Jargroup Create     | ✅ [docs](library#msm_jargroup_create)    | ❌ |
| Jargroup Delete     | ✅ [docs](library#msm_jargroup_delete)    | ❌ |
| Jargroup Rename     | ✅ [docs](library#msm_jargroup_rename)    | ❌ |
| Jargroup Change URL | ✅ [docs](library#msm_jargroup_changeurl) | ❌ |
| Jargroup Get Latest | ✅ [docs](library#msm_jargroup_getlatest) | ⚠️ |

##  Global Commands

| Feature | Library | Webmin UI |
|---------|---------|-----------|
| Start   | ✅ [docs](library#msm_global_start) | ✅ |
| Stop    | ✅ [docs](library#msm_global_start) | ✅ |
| Restart | ✅ [docs](library#msm_global_start) | ✅ |
| Version | ✅ [docs](library#msm_global_start) | ✅ |
| Config  | ❌ [docs](library#msm_global_start) | ❌ |
| Update  | ✅ [docs](library#msm_global_start) | ❌ |
