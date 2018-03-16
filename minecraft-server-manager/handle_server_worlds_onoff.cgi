#!/usr/bin/perl
# handle_server_worlds_onoff.cgi.cgi

require 'msm-lib.pl';
&ReadParse();

# Get the server input, and make sure it's valid.
my $server = $in{'name'};
my $world = $in{'world'};
my $state = lc($in{'state'});

if ($state eq "on") {
    $err = &msm_server_worlds_on($server, $world);
    &webmin_log("server world on");
}
else {
    $err = &msm_server_worlds_off($server, $world);
    &webmin_log("server world off");
}

&redirect("server.cgi?name=$server");

