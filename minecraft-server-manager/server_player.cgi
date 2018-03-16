#!/usr/bin/perl
# server_player.cgi
# Modify the player

require 'msm-lib.pl';
&ReadParse();
my $server = $in{'name'};
my $player = $in{'player'};

$url_kick = "handle_server_player_kick.cgi?name=$server&player=$player";

$is_blacklisted = is_player_blacklisted($server, $player);
$url_blacklist_add = "handle_server_player_blacklist.cgi?name=$server&player=$player&action=add";
$url_blacklist_remove = "handle_server_player_blacklist.cgi?name=$server&player=$player&action=remove";

$is_whitelisted = is_player_whitelisted($server, $player);
$url_whitelist_add = "handle_server_player_whitelist.cgi?name=$server&player=$player&action=add";
$url_whitelist_remove = "handle_server_player_whitelist.cgi?name=$server&player=$player&action=remove";

$is_oped = is_player_oped($server, $player);
$url_oplist_add = "handle_server_player_op.cgi?name=$server&player=$player&action=add";
$url_oplist_remove = "handle_server_player_op.cgi?name=$server&player=$player&action=remove";

$url_survival = "handle_server_player_gamemode.cgi?name=$server&player=$player&mode=survival";
$url_creative = "handle_server_player_gamemode.cgi?name=$server&player=$player&mode=creative";

&ui_print_header(undef, "Player Management: \"$server\"", "", "options");

print "<h3> Managing player '$player'</h3>";

print ui_buttons_start();
print "<table style='border-collapse: separate;'>";

print "<tr><td>";
print ui_buttons_row($url_kick, "Kick", "");
print "</td><td>Forcibly disconnect the player from the server</td></tr>";

if ($is_blacklisted) {
    print "<tr><td>";
    print ui_buttons_row($url_blacklist_remove, "Un-blacklist Player", "");
    print "</td><td>Pardon the player from/for the server</td></tr>";
}
else {
    print "<tr><td>";
    print ui_buttons_row($url_blacklist_add, "Blacklist Player", "");
    print "</td><td>Ban the player from/for the server</td></tr>";
}

if ($is_whitelisted) {
    print "<tr><td>";
    print ui_buttons_row($url_whitelist_remove, "Un-whitelist Player", "Remove the player to/from the server's whitelist");
    print "</td><td>Remove the player to/from the server's whitelist</td></tr>";
}
else {
    print "<tr><td>";
    print ui_buttons_row($url_whitelist_add, "Whitelist Player", "");
    print "</td><td>Add the player to/from the server's whitelist</td></tr>";
}

if ($is_oped) {
    print "<tr><td>";
    print ui_buttons_row($url_oplist_remove, "Un-Op Player", "");
    print "</td><td>Remove operator status for the player on the server</td></tr>";
}
else {
    print "<tr><td>";
    print ui_buttons_row($url_oplist_add, "Op Player", "");
    print "</td><td>Add operator status for the player on the server</td></tr>";
}

print "<tr><td>";
print ui_buttons_row($url_survival, "Mode: Survival", "");
print "</td><td>Change the game mode to Survival for the player on the server</td></tr>";

print "<tr><td>";
print ui_buttons_row($url_creative, "Mode: Creative", "");
print "</td><td>Change the game mode to Creative for the player on the server</td></tr>";

print "</table>";
print ui_buttons_end();

&ui_print_footer("server.cgi?name=$server", "server");
