#!/usr/bin/perl
# server_player_kick.cgi
# Kicks a player from the server

require 'msm-lib.pl';
&ReadParse();

# Get the server input, and make sure it's valid.
my $server = $in{'name'};
my $player = $in{'player'};
if (!(grep { $_ eq $server } msm_server_list())) {
    error("No server with name: $server");
}
if (!(grep { $_ eq $player } msm_server_connected($server))) {
    error("Player is not connected: $player");
}

$err = &msm_server_kick($server, $player);
&webmin_log("server kick. Result $err");
&redirect("server.cgi?name=$server");