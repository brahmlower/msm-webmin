#!/usr/bin/perl
# server_player_op.cgi
# Ops the player on the server

require 'msm-lib.pl';
&ReadParse();

# Get the server input, and make sure it's valid.
my $server = $in{'name'};
my $player = $in{'player'};
my $action = $in{'action'};
if (!(grep { $_ eq $server } msm_server_list())) {
    error("No server with name: $server");
}

if ($action eq "add") {
    $err = &msm_server_op_add($server, $player);
}
else {
    $err = &msm_server_op_remove($server, $player);
}

&webmin_log("server op $action");
&redirect("server.cgi?name=$server");