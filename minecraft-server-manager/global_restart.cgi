#!/usr/bin/perl
# global_restart.cgi
# Restarts all minecraft servers

require 'msm-lib.pl';
&ReadParse();
$err = &msm_global_restart();
&webmin_log("global restart");
&redirect("");
