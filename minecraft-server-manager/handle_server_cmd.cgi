#!/usr/bin/perl
# handle_server_command.cgi
# Says something to the specified server

require 'msm-lib.pl';
&ReadParse();

# Get the server input, and make sure it's valid.
my $server = $in{'name'};
my $command = $in{'command'};

if (!(grep { $_ eq $server } msm_server_list())) {
    error("No server with name: $server");
}

$err = &msm_server_cmd($server, $command);
&webmin_log("server command");
&redirect("server.cgi?name=$server");