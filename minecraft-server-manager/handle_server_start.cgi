#!/usr/bin/perl
# server_start.cgi
# Starts the specified server

require 'msm-lib.pl';
&ReadParse();

# Get the server input, and make sure it's valid.
my $server = $in{'name'};
if (!(grep { $_ eq $server } msm_server_list())) {
    error("No server with name: $server");
}

$err = &msm_server_start($server);
&webmin_log("server start");
&redirect("server.cgi?name=$server");