#!/usr/bin/perl
# Show a form to create or edit a website

require 'msm-lib.pl';
ReadParse();

my $server = $in{'name'};
# Redirects to home if the jargroup does not exist
if (!(grep { $_ eq $server } msm_server_list())) {
    error("No server with name: $server");
}

ui_print_header(undef, "Server: \"$server\"", "");

$status = msm_server_status($server);

print "<h2> Service Controls & Status</h2>";

print ui_buttons_start();
print "<table style='border-collapse: separate;'>";

if ($status eq "Running") {
    # Show stop button
    print "<tr><td>";
    print ui_buttons_row("handle_server_stop.cgi?name=$server", "Stop", "");
    print "</td><td>Stops a server after warning players</td></tr>";
    # Show restart button
    print "<tr><td>";
    print ui_buttons_row("handle_server_restart.cgi?name=$server", "Restart", "");
    print "</td><td>Restarts a server after warning players</td></tr>";
}
else {
    # Show start button
    print "<tr><td>";
    print ui_buttons_row("handle_server_start.cgi?name=$server", "Start", "");
    print "</td><td>Starts the server</td></tr>";
}

print "<tr><td>";
print ui_buttons_row("handle_server_logroll.cgi?name=$server", "Roll Logs", "");
print "</td><td>Move a server log to a gziped archive, to reduce lag</td></tr>";

print "<tr><td>";
print ui_buttons_row("server_world.cgi?name=$server", "World Management", "");
print "</td><td>Manage various worlds for this server</td></tr>";

print "<tr><td>";
print ui_buttons_row("handle_server_backup.cgi?name=$server", "Backup", "");
print "</td><td>Makes a backup of an entire server directory</td></tr>";

print "<tr><td>";
print ui_buttons_row("server_rename.cgi?name=$server", "Rename", "");
print "</td><td>Renames the Minecraft server</td></tr>";

print "<tr><td>";
print ui_buttons_row("handle_server_delete.cgi?name=$server", "Delete", "");
print "</td><td>Deletes the existing Minecraft server</td></tr>";

print "</table>";
print ui_buttons_end();

print "<h2> Game Controls </h2>";

print ui_buttons_start();
print "<table style='border-collapse: separate;'>";

print "<tr><td>";
print ui_buttons_row("server_say.cgi?name=$server", "Say", "");
print "</td><td>Broadcast a (pink) message to all players on a server</td></tr>";

print "<tr><td>";
print ui_buttons_row("handle_server_toggledownfall.cgi?name=$server", "Toggle Downfall", "");
print "</td><td>Toggles rain and snow on a server</td></tr>";

print "<tr><td>";
print ui_buttons_row("server_time.cgi?name=$server", "Modify Time", "");
print "</td><td>Set/increment time on a server (0-24000)</td></tr>";

print "<tr><td>";
print ui_buttons_row("server_give.cgi?name=$server", "Give Item", "");
print "</td><td>Gives an entity to a player</td></tr>";

print "<tr><td>";
print ui_buttons_row("server_xp.cgi?name=$server", "Give XP", "");
print "</td><td>Gives XP to, or takes away (when negative) XP from, a player</td></tr>";

print "<tr><td>";
print ui_buttons_row("server_cmd.cgi?name=$server", "Server Command", "");
print "</td><td>Send a command string to the server and return</td></tr>";

print "</table>";
print ui_buttons_end();

print "<h2> Player Controls </h2>";

print ui_buttons_start();
print "<table style='border-collapse: separate;'>";

print "<tr><td>";
print ui_buttons_row("server_whitelist.cgi?name=$server", "Whitelist", "");
print "</td><td>Manage the servers whitelist</td></tr>";

print "<tr><td>";
print ui_buttons_row("server_blacklist.cgi?name=$server", "Blacklist", "");
print "</td><td>Manage the servers blacklist</td></tr>";

print "<tr><td>";
print ui_buttons_row("server_ops.cgi?name=$server", "Ops List", "");
print "</td><td>Manage the servers Ops</td></tr>";

print "</table>";
print ui_buttons_end();

# Get connected players, ops list, whitelist and blacklist
my @players = msm_server_connected($server);

# Players
$players_len = @players;
print "<h3> Active Players </h3>";
if ($players_len == 0) {
    print "<strong>There are currently no players.</strong>";
}
else {
    print ui_columns_start(["Player Name", ""], undef, "noborder", undef, undef);
    foreach (@players) {
        $manage = ui_buttons_row("server_player.cgi?name=$server&player=$_", "Manage", "");
        print ui_columns_row([html_escape($_), $manage]);
    }
    print ui_columns_end();
}

ui_print_footer('', $text{'index_return'});
