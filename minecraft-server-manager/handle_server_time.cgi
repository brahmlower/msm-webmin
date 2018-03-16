#!/usr/bin/perl
# handle_server_time.cgi
# Modifies the time of day

require 'msm-lib.pl';
&ReadParse();

# Get the server input, and make sure it's valid.
my $server = $in{'name'};
my $action = lc($in{'action'});
my $amount = $in{'amount'};

if (!(grep { $_ eq $server } msm_server_list())) {
    error("No server with name: $server");
}

if ($action ne "set" && $action ne "add") {
    error ("Invalid action");
}

# Execute the specified action
if ($action eq "set") {
    $err = &msm_server_time_set($server, $amount);
    &webmin_log("server time set");
}
else {
    $err = &msm_server_time_add($server, $amount);
    &webmin_log("server time add");
}
&redirect("server.cgi?name=$server");
