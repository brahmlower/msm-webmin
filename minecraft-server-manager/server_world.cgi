#!/usr/bin/perl
# server_world.cgi
# Monage worlds on the server

require 'msm-lib.pl';
&ReadParse();
my $server = $in{'name'};

&ui_print_header(undef, "World Management: \"$server\"", "", "options");

# Whitelist on/off buttons
print ui_buttons_start();
print "<table style='border-collapse: separate;'>";

print "<tr><td>";
print ui_buttons_row("handle_server_worlds_load.cgi?name=$server", "Load", "");
print "</td><td>Creates links to worlds in storage for a server</td></tr>";

print "<tr><td>";
print ui_buttons_row("handle_server_worlds_todisk.cgi?name=$server", "To Disk", "");
print "</td><td>Synchronises any 'in RAM' worlds to disk</td></tr>";

print "<tr><td>";
print ui_buttons_row("handle_server_worlds_backup.cgi?name=$server", "Backup", "");
print "</td><td>Makes a backup of all worlds a server has</td></tr>";

print "<tr><td>";
print ui_buttons_row("handle_server_worlds_save_onoff.cgi?name=$server&state=on", "Save: On", "");
print "</td><td>Turns world saving on</td></tr>";

print "<tr><td>";
print ui_buttons_row("handle_server_worlds_save_onoff.cgi?name=$server&state=off", "Save: Off", "");
print "</td><td>Turns world saving off</td></tr>";

print "<tr><td>";
print ui_buttons_row("handle_server_worlds_save_all.cgi?name=$server", "Save All", "");
print "</td><td>Saves all worlds</td></tr>";

print "</table>";
print ui_buttons_end();

my @worlds = &msm_server_worlds_list($server);

$worlds_len = @worlds;
print "<h3> Worlds List </h3>";
if ($worlds_len == 0) {
    print "<strong>You have no worlds on this server.</strong>";
}
else {
    print ui_columns_start(["World Name", "Acions", "", ""], undef, "noborder", undef, undef);
    foreach (@worlds) {
        my $u_ = urlize($_);
        $ram_message = "RAM On";
        if (&is_world_ram($server, $_)) {
            $ram_message = "RAM Off";
        }
        $toggle_ram = ui_buttons_row("handle_server_worlds_ram.cgi?name=$server&world=$u_", $ram_message, "");
        $activate = ui_buttons_row("handle_server_worlds_onoff.cgi?name=$server&world=$u_&state=on", "Activate", "");
        $deactivate = ui_buttons_row("handle_server_worlds_onoff.cgi?name=$server&world=$u_&state=off", "Deactivate", "");
        print ui_columns_row([html_escape($_), $toggle_ram, $activate, $deactivate]);
    }
    print ui_columns_end();
}

&ui_print_footer("server.cgi?name=$server", "server");

