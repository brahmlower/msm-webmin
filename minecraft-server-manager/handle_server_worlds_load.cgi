#!/usr/bin/perl
# handle_server_world_load.cgi
# Loads worlds for a server

require 'msm-lib.pl';
&ReadParse();

# Get the server input, and make sure it's valid.
my $server = $in{'name'};
if (!(grep { $_ eq $server } msm_server_list())) {
    error("No server with name: $server");
}

$err = &msm_server_worlds_load($server);
&webmin_log("server worlds load");
&redirect("server.cgi?name=$server");
