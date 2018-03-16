#!/usr/bin/env perl

# Utils and configs ############################################################

use lib '/usr/share/webmin';
use WebminCore;

&init_config();

my %module_config = %WebminCore::config;
my %msm_config = get_msm_config();

# Helper function
sub contains {
    my ($target, $sub) = @_;
    if (index($target, $sub) != -1) {
        return 1;
    }
    return 0;
}

sub get_msm_config {
    my %c;
    open(CONF, $module_config{'msm_config'});
    while(<CONF>) {
        s/\r|\n//g;
        s/^\s*#.*$//g;
        my ($name, $value) = split(/=/, $_);
        if ($name ne "") {
            if (substr($value, 0, 1) eq "\"") {
                $value = substr($value, 1, -1);
            }
            $c{$name} = $value;
        }
    }
    close(CONF);
    return %c;
}

sub msm_exec {
    my ($command) = @_;
    my $bin = $module_config{'msm_bin'};
    my $user = $msm_config{'USERNAME'};
    &webmin_log("Running command: $bin $command");
    &webmin_log("Running as user: $user");
    my $out = `su -c '$bin $command' $user`;
    &webmin_log("Result: $out");
    return $out;
}

sub msm_input_exec {
    my ($command, $input) = @_;
    my $bin = $module_config{'msm_bin'};
    my $user = $msm_config{'USERNAME'};
    &webmin_log("Running command: $bin $command");
    &webmin_log("Running as user: $user");
    my $out = `echo $input | su -c '$bin $command' $user`;
    &webmin_log("Result: $out");
    return $out;
}

sub is_player_blacklisted {
    my ($server, $player) = @_;
    my @blacklist = msm_server_blacklist_list($server);
    if (grep { $_ eq $player } @blacklist) {
        return 1;
    }
    return 0;
}

sub is_player_whitelisted {
    my ($server, $player) = @_;
    my @whitelist = msm_server_whitelist_list($server);
    if (grep { $_ eq $player } @whitelist) {
        return 1;
    }
    return 0;
}

sub is_player_oped {
    my ($server, $player) = @_;
    my @oplist = msm_server_op_list($server);
    if (grep { $_ eq $player } @oplist) {
        return 1;
    }
    return 0;
}

sub is_world_ram {
    my ($server_name, $world) = @_;
    my $command = "$server_name worlds list";
    my $out = msm_exec($command);
    foreach (split(/\n/, $out)) {
        if (contains($_, $world) && contains($_, "RAM")) {
            return 1;
        }
        elsif (contains($_, $world)) {
            return 0;
        }
    }
    return 0;
}

# Server List ##################################################################

sub parse_servername {
    my ($list_line) = @_;
    my $start = index($list_line, " \"") + 2;
    my $end = index($list_line, "\" ");
    return substr($list_line, $start, ($end - $start));
}

sub msm_server_list {
    my $command = "server list";
    my $out = msm_exec($command);
    return map(parse_servername($_), split(/\n/, $out));
}

# Server Create ################################################################

sub msm_server_create {
    my ($server_name) = @_;
    my $command = "server create $server_name";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# Server Delete ################################################################

sub msm_server_delete {
    my ($server_name) = @_;
    my $command = "server delete $server_name";
    my $out = msm_input_exec($command, "y");
    return split(/\n/, $out);
}

# Server Rename ################################################################

sub msm_server_rename {
    my ($server_name, $server_new_name) = @_;
    my $command = "server rename $server_name $server_new_name";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Start ###############################################################

sub msm_server_start {
    # TODO: Handle missing Java. $out == "Could not start server as Java is not installed."
    # TODO: Report error if Eula hasn't been signed yet.
    my ($server_name) = @_;
    my $command = "$server_name start";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Stop ################################################################

sub msm_server_stop {
    my ($server_name) = @_;
    my $command = "$server_name stop";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Restart #############################################################

sub msm_server_restart {
    # TODO: While running this, I get the following error. Does it require
    # additional attention?
    # Error: Could not create link for world "world". The file "/opt/msm/servers/new_test/world" already exists, and should not be overwritten automatically. Either remove this file, or rename "world"
    my ($server_name) = @_;
    my $command = "$server_name restart";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Status ##############################################################

sub msm_server_status {
    my ($server_name) = @_;
    my $command = "$server_name status";
    my $out = msm_exec($command);
    if (contains($out, "is running")) {
        return "Running"
    }
    return "Stopped"
}

# <Server> Connected ###########################################################

sub msm_server_connected {
    my ($server_name) = @_;
    my $command = "$server_name connected";
    my $out = msm_exec($command);
    # If there are no users, return an empty list. First string is displayed
    # when there are no users, but the server is running. Second string is
    # displayed when there are no users, and the server is stopped.
    # TODO: Maybe open a PR to make MSM verbiage consistent?
    if ((contains($out, "No players are connected")) || (contains($out, "No users are connected"))) {
        return ();
    }
    # If there are some users, count them
    my @users = split(/\n/, $out);
    # Remove warning if it's there
    if (contains($users[0], "MSM Info:")) {
        shift(@users)
    }
    return @users;
}

# <Server> Worlds List #########################################################

sub parse_world_name {
    my ($list_line) = @_;
    my @parts = split(' ', $list_line);
    return $parts[-1];
}

sub msm_server_worlds_list {
    my ($server_name) = @_;
    my $command = "$server_name worlds list";
    my $out = msm_exec($command);
    return map(parse_world_name($_), split(/\n/, $out));
}

# <Server> Worlds Load #########################################################

sub msm_server_worlds_load {
    my ($server_name) = @_;
    my $command = "$server_name worlds load";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Worlds Ram <World> ##################################################

sub msm_server_worlds_ram {
    my ($server_name, $world_name) = @_;
    my $command = "$server_name worlds ram $world_name";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Worlds Todisk #######################################################

sub msm_server_worlds_todisk {
    my ($server_name) = @_;
    my $command = "$server_name worlds todisk";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Worlds Backup #######################################################

sub msm_server_worlds_backup {
    my ($server_name) = @_;
    my $command = "$server_name worlds backup";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Worlds On <World> ###################################################

sub msm_server_worlds_on {
    my ($server_name, $world_name) = @_;
    my $command = "$server_name worlds on $world_name";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Worlds Off <World> ##################################################

sub msm_server_worlds_off {
    my ($server_name, $world_name) = @_;
    my $command = "$server_name worlds off $world_name";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Logroll #############################################################

sub msm_server_logroll {
    my ($server_name) = @_;
    my $command = "$server_name logroll";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Backup ##############################################################

sub msm_server_backup {
    my ($server_name) = @_;
    my $command = "$server_name backup";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Jar #################################################################

sub msm_server_jar {
    my ($server_name, $jar_group, $jar_file) = @_;
    my $command = "$server_name jar $jar_group";
    if (defined $jar_file) { $command = "$command $jar_file" }
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Console #############################################################
# TODO Possibly weird implementation

# <Server> Config ##############################################################
# TODO Possibly weird implementation

# <Server> Whitelist On ########################################################

sub msm_server_whitelist_on {
    my ($server_name) = @_;
    my $command = "$server_name whitelist on";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Whitelist Off #######################################################

sub msm_server_whitelist_off {
    my ($server_name) = @_;
    my $command = "$server_name whitelist off";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Whitelist Add #######################################################
# TODO: There appears to be a bug with MSM where the player isn't added to the
# whitelist. That or the whitelist isn't being properly reported
sub msm_server_whitelist_add {
    my ($server_name, $player) = @_;
    my $command = "$server_name whitelist add $player";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Whitelist Remove ####################################################

sub msm_server_whitelist_remove {
    my ($server_name, $player) = @_;
    my $command = "$server_name whitelist remove $player";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Whitelist List ######################################################

sub msm_server_whitelist_list {
    my ($server_name) = @_;
    my $command = "$server_name whitelist list";
    my $out = msm_exec($command);
    if (contains($out, "No players are whitelisted.")) {
        return ();
    }
    # If there are some users, count them
    my @users = split(/\n/, $out);
    # Remove warning if it's there
    if (contains($users[0], "MSM Info:")) {
        shift(@users)
    }
}

# <Server> Blacklist Player Add ################################################

sub msm_server_blacklist_player_add {
    my ($server_name, $player) = @_;
    my $command = "$server_name blacklist player add $player";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Blacklist Player Remove #############################################

sub msm_server_blacklist_player_remove {
    my ($server_name, $player) = @_;
    my $command = "$server_name blacklist player remove $player";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Blacklist Ip Add ####################################################

sub msm_server_blacklist_ip_add {
    my ($server_name, $address) = @_;
    my $command = "$server_name blacklist ip add $address";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Blacklist Ip Remove #################################################

sub msm_server_blacklist_ip_remove {
    my ($server_name, $address) = @_;
    my $command = "$server_name blacklist ip remove $address";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Blacklist List ######################################################

sub msm_server_blacklist_list {
    my ($server_name) = @_;
    my $command = "$server_name blacklist list";
    my $out = msm_exec($command);
    if (contains($out, "The blacklist is empty.")) {
        return ();
    }
    # If there are some users, count them
    my @users = split(/\n/, $out);
    # Remove warning if it's there
    if (contains($users[0], "MSM Info:")) {
        shift(@users)
    }
    return @users;
}

# <Server> Op Add ##############################################################

sub msm_server_op_add {
    my ($server_name, $player) = @_;
    my $command = "$server_name op add $player";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Op Remove ###########################################################

sub msm_server_op_remove {
    my ($server_name, $player) = @_;
    my $command = "$server_name op remove $player";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Op List #############################################################

sub msm_server_op_list {
    my ($server_name) = @_;
    my $command = "$server_name op list";
    my $out = msm_exec($command);
    if (contains($out, "No players are operators.")) {
        return ();
    }
    # If there are some users, count them
    my @users = split(/\n/, $out);
    # Remove warning if it's there
    if (contains($users[0], "MSM Info:")) {
        shift(@users)
    }
    return @users;
}

# <Server> Gamemode Survival ###################################################

sub msm_server_gamemode_survival {
    my ($server_name, $player) = @_;
    my $command = "$server_name gm survival $player";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Gamemode Creative ###################################################

sub msm_server_gamemode_creative {
    my ($server_name, $player) = @_;
    my $command = "$server_name gm creative $player";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Kick ################################################################

sub msm_server_kick {
    my ($server_name, $player) = @_;
    my $command = "$server_name kick $player";
    my $out = msm_exec($command);
    return contains($out, "Kicked");
}

# <Server> Say #################################################################

sub msm_server_say {
    my ($server_name, $message) = @_;
    my $command = "$server_name say $message";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Time Set ############################################################

sub msm_server_time_set {
    my ($server_name, $time) = @_;
    my $command = "$server_name time set $time";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Time Add ############################################################

sub msm_server_time_add {
    my ($server_name, $time) = @_;
    my $command = "$server_name time add $time";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Toggledownfall ######################################################

sub msm_server_toggledownfall {
    my ($server_name) = @_;
    my $command = "$server_name toggledownfall";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Give ################################################################
# Building the optional parameters in the command is done in a relatively niave
# manner, but it gets the job done. Feel free to open a PR if this drives you
# crazy :)
sub msm_server_give {
    my ($server_name, $player, $item, $amount, $data) = @_;
    my $command = "$server_name give $player $item";
    if (defined $amount) { $command = "$command $amount" }
    if (defined $amount && defined $data) { $command = "$command $data" }
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Xp ##################################################################

sub msm_server_xp {
    my ($server_name, $player, $amount) = @_;
    my $command = "$server_name xp $player $amount";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Save On #############################################################

sub msm_server_save_on {
    my ($server_name) = @_;
    my $command = "$server_name save on";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Save Off ############################################################

sub msm_server_save_off {
    my ($server_name) = @_;
    my $command = "$server_name save off";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Save All ############################################################

sub msm_server_save_all {
    my ($server_name) = @_;
    my $command = "$server_name save all";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Cmd #################################################################

sub msm_server_cmd {
    my ($server_name, $cmd) = @_;
    my $command = "$server_name cmd $cmd";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# <Server> Cmdlog ##############################################################

sub msm_server_cmdlog {
    my ($server_name, $cmd) = @_;
    my $command = "$server_name cmdlog $cmd";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# Jargroup List ################################################################

sub msm_jargroup_list {
    my $command = "jargroup list";
    my $out = msm_exec($command);
    my @out_lines;
    foreach (split(/\n/, $out)) {
        if (!(contains($_, "    "))) {
            push(@out_lines, $_);
        } 
    }
    return @out_lines;
}

# Jargroup Files ###############################################################

sub msm_jargroup_files {
    my ($jar_name) = @_;
    my $command = "jargroup list";
    my $out = msm_exec($command);
    my @lines = split(/\n/, $out);
    splice(@lines, 0, index(@lines, $jar_name)); # Remove items before the files for the specified jargroup
    my @out_lines;
    while (contains($lines[0], "    ")) {
        my $jar = shift(@lines);
        $jar =~ s/^\s+//;
        push(@out_lines, $jar);
    }
    return @out_lines;
}

# Jargroup Create ##############################################################

sub msm_jargroup_create {
    my ($jar_name, $jar_download_url) = @_;
    my $command = "jargroup create $jar_name $jar_download_url";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# Jargroup Delete ##############################################################

sub msm_jargroup_delete {
    my ($jar_name) = @_;
    my $command = "jargroup delete $jar_name";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# Jargroup Rename ##############################################################

sub msm_jargroup_rename {
    my ($jar_name, $jar_new_name) = @_;
    my $command = "jargroup rename $jar_name $jar_new_name";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# Jargroup Changeurl ###########################################################

sub msm_jargroup_changeurl {
    my ($jar_name, $jar_download_url) = @_;
    my $command = "jargroup changeurl $jar_name $jar_download_url";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# Jargroup Getlatest ###########################################################

sub msm_jargroup_getlatest {
    my ($jar_name) = @_;
    my $command = "jargroup getlatest $jar_name";
    my $out = msm_exec($command);
    return contains($out, "Done");
}

# Global Start #################################################################

sub msm_global_start {
    my $command = "start";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# Global Stop ##################################################################

sub msm_global_stop {
    my ($now) = @_;
    my $command = "stop";
    if (defined $now && $now == "now") { $command = "$command now" }
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# Global Restart ###############################################################

sub msm_global_restart {
    my ($now) = @_;
    my $command = "restart";
    if (defined $now && $now == "now") { $command = "$command now" }
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# Global Version ###############################################################

sub msm_global_version {
    my $command = "version";
    my $out = msm_exec($command);
    $out =~ s/Minecraft Server Manager //;
    return $out;
}

# Global Config ################################################################

sub msm_global_config {
    my $command = "config";
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

# Global Update ################################################################

sub msm_global_update {
    my ($noinput) = @_;
    my $command = "update";
    if (defined $noinput && $noinput == "noinput") { $command = "$command --noinput" }
    my $out = msm_exec($command);
    return split(/\n/, $out);
}

1;