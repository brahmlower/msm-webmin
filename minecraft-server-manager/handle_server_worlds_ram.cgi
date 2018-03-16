#!/usr/bin/perl
# handle_server_worlds_ram.cgi
# Toggles a world being loaded in RAM. Can only be applied while server is stopeed.

require 'msm-lib.pl';
&ReadParse();

# Get the server input, and make sure it's valid.
my $server = $in{'name'};
my $world = un_urlize($in{'world'});

if (!(grep { $_ eq $server } msm_server_list())) {
    error("No server with name: $server");
}

if (msm_server_status() eq "running") {
    error("Server must be stopped.");
}

$err = &msm_server_worlds_ram($server, $world);
&webmin_log("server world ram");
&redirect("server.cgi?name=$server");
