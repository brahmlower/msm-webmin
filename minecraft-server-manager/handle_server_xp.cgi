#!/usr/bin/perl
# handle_server_xp.cgi
# Gives xp to a player

require 'msm-lib.pl';
&ReadParse();

# Get the server input, and make sure it's valid.
my $server = $in{'name'};
my $player = $in{'player'};
my $amount = $in{'amount'};

if (!(grep { $_ eq $server } msm_server_list())) {
    error("No server with name: $server");
}

$err = &msm_server_xp($server, $player, $amount);
&webmin_log("server xp");
&redirect("server.cgi?name=$server");