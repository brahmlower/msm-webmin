#!/usr/bin/perl
# handle_server_world_todisk.cgi

require 'msm-lib.pl';
&ReadParse();

# Get the server input, and make sure it's valid.
my $server = $in{'name'};
if (!(grep { $_ eq $server } msm_server_list())) {
    error("No server with name: $server");
}

$err = &msm_server_worlds_todisk($server);
&webmin_log("server worlds todisk");
&redirect("server.cgi?name=$server");
