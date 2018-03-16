#!/usr/bin/perl
# global_start.cgi
# Starts all minecraft servers

require 'msm-lib.pl';
&ReadParse();
$err = &msm_global_start();
&webmin_log("global start");
&redirect("");
