#!/usr/bin/perl
# server_backup.cgi
# Backs up the server

require 'msm-lib.pl';
&ReadParse();

# Get the server input, and make sure it's valid.
my $server = $in{'name'};
if (!(grep { $_ eq $server } msm_server_list())) {
    error("No server with name: $server");
}

$err = &msm_server_backup($server);
&webmin_log("server backup");
&redirect("server.cgi?name=$server");