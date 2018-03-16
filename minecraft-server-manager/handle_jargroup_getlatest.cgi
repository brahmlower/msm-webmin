#!/usr/bin/perl
# jargroup_getlatest.cgi
# Start the ssh daemon

require 'msm-lib.pl';
&ReadParse();

my $jargroup = $in{'jargroup'};
# Redirects to home if the jargroup does not exist
if (!(grep { $_ eq $jargroup } msm_jargroup_list())) {
    error("No jargroup with name: $jargroup");
}

&error_setup($text{'start_err'});
$err = &msm_jargroup_getlatest($jargroup);
&error($err) if ($err == 0);
&webmin_log("jargroup getlatest");
&redirect("jargroup.cgi?name=$jargroup");
