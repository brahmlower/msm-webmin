#!/usr/bin/perl
# handle_server_player_gamemode.cgi.cgi
# Sets the server to Survival/Creative mode

require 'msm-lib.pl';
&ReadParse();

# Get the server input, and make sure it's valid.
my $server = $in{'name'};
my $player = $in{'player'};
my $mode = lc($in{'mode'});

if ($mode eq "survival") {
    $err = &msm_server_gamemode_survival($server, $player);
    &webmin_log("server survival mode");
}
elsif ($mode eq "creative") {
    $err = &msm_server_gamemode_creative($server, $player);
    &webmin_log("server creative mode");
}

&redirect("server.cgi?name=$server");

