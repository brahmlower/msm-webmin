#!/usr/bin/perl
# global_update.cgi
# Updates JARs I think

require 'msm-lib.pl';
&ReadParse();
$err = &msm_global_update();
&webmin_log("global update");
&redirect("");
