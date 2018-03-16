#!/usr/bin/perl
# handle_server_worlds_save_onoff.cgi.cgi
# Turns world saving on or off

require 'msm-lib.pl';
&ReadParse();

# Get the server input, and make sure it's valid.
my $server = $in{'name'};
my $state = lc($in{'state'});

if ($state eq "on") {
    $err = &msm_server_save_on($server);
    &webmin_log("server save on");
}
elsif ($state eq "off") {
    $err = &msm_server_save_off($server);
    &webmin_log("server save off");
}

&redirect("server.cgi?name=$server");

