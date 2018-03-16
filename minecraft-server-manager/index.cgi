#!/usr/bin/perl
# Main Minecraft Server Manager index page

require 'msm-lib.pl';

$version = msm_global_version();

ui_print_header(undef, "$module_info{desc} (Version $version)", "", undef, 1, 1, 0,
                undef, undef, undef, "MSM Webmin plugin version: $module_info{version}");

# print ui_hr();

print ui_buttons_start();
print "<table style='border-collapse: separate;'>";

print "<tr><td>";
print ui_buttons_row("global_start.cgi", "Start Servers", "");
print "</td><td>Starts all active servers</td></tr>";

print "<tr><td>";
print ui_buttons_row('global_stop.cgi', "Stop Servers", "");
print "</td><td>Stops all running servers</td></tr>";

print "<tr><td>";
print ui_buttons_row('global_restart.cgi', "Restart Servers", "");
print "</td><td>Restarts all active servers</td></tr>";

print "<tr><td>";
print ui_buttons_row('global_edit.cgi', "Edit Config", "");
print "</td><td>Edit MSM configurations</td></tr>";

print "<tr><td>";
print ui_buttons_row('global_update.cgi', "Update", "");
print "</td><td>Replaces MSM files with the latest recommended versions</td></tr>";

print "</table>";
print ui_buttons_end();

print ui_hr();

# Servers list
print ui_buttons_start();
print ui_buttons_row('server_create.cgi',
                     "Create Server",
                     "Creates a new Minecraft server");
print ui_buttons_end();
my @servers = msm_server_list();
print ui_columns_start(["Server Name", "Status", "Connected"], undef, "noborder", undef, undef);
foreach (@servers) {
    $status = msm_server_status($_);
    $connected = 0;
    if ($status == "Running") {
        @users = msm_server_connected($_);
        $connected = @users;
    }
    print ui_columns_row( ["<a href='server.cgi?name=".urlize($_)."'>".html_escape($_)."</a>", $status, $connected] );
}
print ui_columns_end();
print "<br><br><br>";

# Jargroup list
print ui_buttons_start();
print ui_buttons_row('jargroup_create.cgi',
                     "Create Jargroup",
                     "Create a new jar group");
print ui_buttons_end();

my @jargroups = msm_jargroup_list();
print ui_columns_start(["Jargroup Name"], undef, "noborder", undef, undef);
foreach (@jargroups) {
    print ui_columns_row( ["<a href='jargroup.cgi?name=".urlize($_)."'>".html_escape($_)."</a>"] );
}
print ui_columns_end();

# Page footer

ui_print_footer('/', $text{'index'});
