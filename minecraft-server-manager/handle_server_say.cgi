#!/usr/bin/perl
# handle_server_say.cgi
# Says something to the specified server

require 'msm-lib.pl';
&ReadParse();

# Get the server input, and make sure it's valid.
my $server = $in{'name'};
my $message = $in{'message'};

if (!(grep { $_ eq $server } msm_server_list())) {
    error("No server with name: $server");
}

$err = &msm_server_say($server, $message);
&webmin_log("server say");
&redirect("server.cgi?name=$server");