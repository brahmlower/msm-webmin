#!/usr/bin/perl
# global_stop.cgi
# Stops all minecraft servers

require 'msm-lib.pl';
&ReadParse();
$err = &msm_global_stop();
&webmin_log("global stop");
&redirect("");
