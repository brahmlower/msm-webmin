#!/usr/bin/perl
# handle_server_whitelist_onoff.cgi.cgi
# Turns the whitelist on/off

require 'msm-lib.pl';
&ReadParse();

# Get the server input, and make sure it's valid.
my $server = $in{'name'};
my $state = lc($in{'state'});

if ($state eq "on") {
    $err = &msm_server_whitelist_on($server);
    &webmin_log("server whitelist on");
}
else {
    $err = &msm_server_whitelist_off($server);
    &webmin_log("server whitelist off");
}

&redirect("server.cgi?name=$server");

