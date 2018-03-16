#!/usr/bin/perl
# edit_options.cgi
# Display all MSM options

# require './msm-lib.pl';
require 'msm-lib.pl';

&ui_print_header(undef, $text{'options_title'}, "", "options");
$options = &get_msm_config();

print &ui_form_start("save_options.cgi");
print &ui_table_start($text{'options_header'}, "width=100%", 2);

# USERNAME
$username = &find_value("USERNAME", $options);
print &ui_table_row(
    $text{'options__username'},
	&ui_user_textbox("username", $username)
    );

# Directory Locations ##########################################################

# SERVER_STORAGE_PATH
$server_storage_path = &find_value("SERVER_STORAGE_PATH", $options);
print &ui_table_row(
    $text{'options__server_storage_path'},
    &ui_filebox("server_storage_path", $server_storage_path)
    );

# JAR_STORAGE_PATH
$jar_storage_path = &find_value("JAR_STORAGE_PATH", $options);
print &ui_table_row(
    $text{'options__jar_storage_path'},
    &ui_filebox("jar_storage_path", $jar_storage_path)
    );

# VERSIONING_STORAGE_PATH
$versioning_storage_path = &find_value("VERSIONING_STORAGE_PATH", $options);
print &ui_table_row(
    $text{'options__versioning_storage_path'},
    &ui_filebox("versioning_storage_path", $versioning_storage_path)
    );

# RAMDISK_STORAGE_ENABLED
$ramdisk_storage_enabled = &find_value("RAMDISK_STORAGE_ENABLED", $options);
print &ui_table_row(
    $text{'options__ramdisk_storage_enabled'},
    &ui_yesno_radio("ramdisk_storage_enabled", $ramdisk_storage_enabled, "true", "false")
    );

# RAMDISK_STORAGE_PATH
$ramdisk_storage_path = &find_value("RAMDISK_STORAGE_PATH", $options);
print &ui_table_row(
    $text{'options__ramdisk_storage_path'},
    &ui_filebox("ramdisk_storage_path", $ramdisk_storage_path)
    );

# Backup Options ###############################################################

# WORLD_ARCHIVE_ENABLED
$world_archive_enabled = &find_value("WORLD_ARCHIVE_ENABLED", $options);
print &ui_table_row(
    $text{'options__world_archive_enabled'},
    &ui_yesno_radio("world_archive_enabled", $world_archive_enabled, "true", "false")
    );

# WORLD_ARCHIVE_PATH
$world_archive_path = &find_value("WORLD_ARCHIVE_PATH", $options);
print &ui_table_row(
    $text{'options__world_archive_path'},
    &ui_filebox("world_archive_path", $world_archive_path)
    );

# LOG_ARCHIVE_PATH
$log_archive_path = &find_value("LOG_ARCHIVE_PATH", $options);
print &ui_table_row(
    $text{'options__log_archive_path'},
    &ui_filebox("log_archive_path", $log_archive_path)
    );

# BACKUP_ARCHIVE_PATH
$backup_archive_path = &find_value("BACKUP_ARCHIVE_PATH", $options);
print &ui_table_row(
    $text{'options__backup_archive_path'},
    &ui_filebox("backup_archive_path", $backup_archive_path)
    );

# RDIFF_BACKUP_ENABLED
$rdiff_backup_enabled = &find_value("RDIFF_BACKUP_ENABLED", $options);
print &ui_table_row(
    $text{'options__rdiff_backup_enabled'},
    &ui_yesno_radio("rdiff_backup_enabled", $rdiff_backup_enabled, "true", "false")
    );

# RDIFF_BACKUP_ROTATION
$rdiff_backup_rotation = &find_value("RDIFF_BACKUP_ROTATION", $options);
print &ui_table_row(
    $text{'options__rdiff_backup_rotation'},
    &ui_textbox("rdiff_backup_rotation", $rdiff_backup_rotation)
    );

# RDIFF_BACKUP_NICE
$rdiff_backup_nice = &find_value("RDIFF_BACKUP_NICE", $options);
print &ui_table_row(
    $text{'options__rdiff_backup_nice'},
    &ui_textbox("rdiff_backup_nice", $rdiff_backup_nice)
    );
print &ui_table_span("The nice parameter \"-20\" to \"19\", -20 is the higher priority on the system, 19 is the lessest");
# ^ Not sure if there is a better way of including long descriptions with input fields

# WORLD_RDIFF_PATH
$world_rdiff_path = &find_value("WORLD_RDIFF_PATH", $options);
print &ui_table_row(
    $text{'options__world_rdiff_path'},
    &ui_filebox("world_rdiff_path", $world_rdiff_path)
    );

# RSYNC_BACKUP_ENABLED
$rsync_backup_enabled = &find_value("RSYNC_BACKUP_ENABLED", $options);
print &ui_table_row(
    $text{'options__rsync_backup_enabled'},
    &ui_yesno_radio("rsync_backup_enabled", $rsync_backup_enabled, "true", "false")
    );

# WORLD_RSYNC_PATH
$world_rsync_path = &find_value("WORLD_RSYNC_PATH", $options);
print &ui_table_row(
    $text{'options__world_rsync_path'},
    &ui_filebox("world_rsync_path", $world_rsync_path)
    );

# Server Defaults ##############################################################

# DEFAULT_USERNAME
$default_username = &find_value("DEFAULT_USERNAME", $options);
print &ui_table_row(
    $text{'options__default_username'},
    &ui_textbox("default_username", $default_username)
    );

# DEFAULT_SCREEN_NAME
$default_screen_name = &find_value("DEFAULT_SCREEN_NAME", $options);
print &ui_table_row(
    $text{'options__default_screen_name'},
    &ui_textbox("default_screen_name", $default_screen_name)
    );

# DEFAULT_WORLD_STORAGE_PATH
$default_world_storage_path = &find_value("DEFAULT_WORLD_STORAGE_PATH", $options);
print &ui_table_row(
    $text{'options__default_world_storage_path'},
    &ui_textbox("default_world_storage_path", $default_world_storage_path)
    );

# DEFAULT_WORLD_STORAGE_INACTIVE_PATH
$default_world_storage_inactive_path = &find_value("DEFAULT_WORLD_STORAGE_INACTIVE_PATH", $options);
print &ui_table_row(
    $text{'options__default_world_storage_inactive_path'},
    &ui_textbox("default_world_storage_inactive_path", $default_world_storage_inactive_path)
    );

# DEFAULT_COMPLETE_BACKUP_FOLLOW_SYMLINKS
$default_complete_backup_follow_symlinks = &find_value("DEFAULT_COMPLETE_BACKUP_FOLLOW_SYMLINKS", $options);
print &ui_table_row(
    $text{'options__default_complete_backup_follow_symlinks'},
    &ui_yesno_radio("default_complete_backup_follow_symlinks", $default_complete_backup_follow_symlinks, "true", "false")
    );

# DEFAULT_LOG_PATH
$default_log_path = &find_value("DEFAULT_LOG_PATH", $options);
print &ui_table_row(
    $text{'options__default_log_path'},
    &ui_textbox("default_log_path", $default_log_path)
    );

# DEFAULT_PROPERTIES_PATH
$default_properties_path = &find_value("DEFAULT_PROPERTIES_PATH", $options);
print &ui_table_row(
    $text{'options__default_properties_path'},
    &ui_textbox("default_properties_path", $default_properties_path)
    );

# DEFAULT_WHITELIST_PATH
$default_whitelist_path = &find_value("DEFAULT_WHITELIST_PATH", $options);
print &ui_table_row(
    $text{'options__default_whitelist_path'},
    &ui_textbox("default_whitelist_path", $default_whitelist_path)
    );

# DEFAULT_BANNED_PLAYERS_PATH
$default_banned_players_path = &find_value("DEFAULT_BANNED_PLAYERS_PATH", $options);
print &ui_table_row(
    $text{'options__default_banned_players_path'},
    &ui_textbox("default_banned_players_path", $default_banned_players_path)
    );

# DEFAULT_BANNED_IPS_PATH
$default_banned_ips_path = &find_value("DEFAULT_BANNED_IPS_PATH", $options);
print &ui_table_row(
    $text{'options__default_banned_ips_path'},
    &ui_textbox("default_banned_ips_path", $default_banned_ips_path)
    );

# DEFAULT_OPS_PATH
$default_ops_path = &find_value("DEFAULT_OPS_PATH", $options);
print &ui_table_row(
    $text{'options__default_ops_path'},
    &ui_textbox("default_ops_path", $default_ops_path)
    );

# DEFAULT_OPS_LIST
$default_ops_list = &find_value("DEFAULT_OPS_LIST", $options);
print &ui_table_row(
    $text{'options__default_ops_list'},
    &ui_textbox("default_ops_list", $default_ops_list)
    );

# DEFAULT_JAR_PATH
$default_jar_path = &find_value("DEFAULT_JAR_PATH", $options);
print &ui_table_row(
    $text{'options__default_jar_path'},
    &ui_textbox("default_jar_path", $default_jar_path)
    );

# DEFAULT_RAM
$default_ram = &find_value("DEFAULT_RAM", $options);
print &ui_table_row(
    $text{'options__default_ram'},
    &ui_textbox("default_ram", $default_ram)
    );

# DEFAULT_INVOCATION
$default_invocation = &find_value("DEFAULT_INVOCATION", $options);
print &ui_table_row(
    $text{'options__default_invocation'},
    &ui_textbox("default_invocation", $default_invocation)
    );

# DEFAULT_STOP_DELAY
$default_stop_delay = &find_value("DEFAULT_STOP_DELAY", $options);
print &ui_table_row(
    $text{'options__default_stop_delay'},
    &ui_textbox("default_stop_delay", $default_stop_delay)
    );

# DEFAULT_RESTART_DELAY
$default_restart_delay = &find_value("DEFAULT_RESTART_DELAY", $options);
print &ui_table_row(
    $text{'options__default_restart_delay'},
    &ui_textbox("default_restart_delay", $default_restart_delay)
    );

# DEFAULT_MESSAGE_STOP
$default_message_stop = &find_value("DEFAULT_MESSAGE_STOP", $options);
print &ui_table_row(
    $text{'options__default_message_stop'},
    &ui_textbox("default_message_stop", $default_message_stop)
    );

# DEFAULT_MESSAGE_RESTART
$default_message_restart = &find_value("DEFAULT_MESSAGE_RESTART", $options);
print &ui_table_row(
    $text{'options__default_message_restart'},
    &ui_textbox("default_message_restart", $default_message_restart)
    );

# DEFAULT_MESSAGE_RESTART_ABORT
$default_message_restart_abort = &find_value("DEFAULT_MESSAGE_RESTART_ABORT", $options);
print &ui_table_row(
    $text{'options__default_message_restart_abort'},
    &ui_textbox("default_message_restart_abort", $default_message_restart_abort)
    );

# DEFAULT_MESSAGE_WORLD_BACKUP_STARTED
$default_message_world_backup_started = &find_value("DEFAULT_MESSAGE_WORLD_BACKUP_STARTED", $options);
print &ui_table_row(
    $text{'options__default_message_world_backup_started'},
    &ui_textbox("default_message_world_backup_started", $default_message_world_backup_started)
    );

# DEFAULT_MESSAGE_WORLD_BACKUP_FINISHED
$default_message_world_backup_finished = &find_value("DEFAULT_MESSAGE_WORLD_BACKUP_FINISHED", $options);
print &ui_table_row(
    $text{'options__default_message_world_backup_finished'},
    &ui_textbox("default_message_world_backup_finished", $default_message_world_backup_finished)
    );

# DEFAULT_MESSAGE_COMPLETE_BACKUP_STARTED
$default_message_complete_backup_started = &find_value("DEFAULT_MESSAGE_COMPLETE_BACKUP_STARTED", $options);
print &ui_table_row(
    $text{'options__default_message_complete_backup_started'},
    &ui_textbox("default_message_complete_backup_started", $default_message_complete_backup_started)
    );

# DEFAULT_MESSAGE_COMPLETE_BACKUP_FINISHED
$default_message_complete_backup_finished = &find_value("DEFAULT_MESSAGE_COMPLETE_BACKUP_FINISHED", $options);
print &ui_table_row(
    $text{'options__default_message_complete_backup_finished'},
    &ui_textbox("default_message_complete_backup_finished", $default_message_complete_backup_finished)
    );

# UPDATE_URL

print &ui_table_end();
print &ui_form_end([ [ undef, $text{'save'} ] ]);

&ui_print_footer("", $text{'index_return'});
