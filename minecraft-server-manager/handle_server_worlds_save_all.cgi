#!/usr/bin/perl
# handle_server_worlds_save_all.cgi
# Saves all worlds (even those that are deactivated)

require 'msm-lib.pl';
&ReadParse();

# Get the server input, and make sure it's valid.
my $server = $in{'name'};
if (!(grep { $_ eq $server } msm_server_list())) {
    error("No server with name: $server");
}

$err = &msm_server_save_all($server);
&webmin_log("server delete");
&redirect("");