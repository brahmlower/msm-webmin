#!/usr/bin/perl
# handle_server_name.cgi
# Creates or renames a server

require 'msm-lib.pl';
&ReadParse();

my $action = $in{'action'};
my $name = $in{'name'};
my $old_name = $in{'old_name'};

# $action should be either "create" or "rename"
if ($action eq "create" && $action eq "rename") {
    error ("Invalid action: $action");
}

# $name should not be an existing server name
@current_servers = msm_server_list();
if ((grep { $_ eq $name } @current_servers)) {
    error("Server already has name: $name");
}

# $old_name should be an existing server name
if (($action eq "rename") && (!(grep { $_ eq $old_name } @current_servers))) {
    error("No server with name: $old_name");
}

if ($action eq "rename") {
    &webmin_log("renaming");
    &msm_server_rename($old_name, $name);
}
else {
    &webmin_log("creating");
    &msm_server_create($name);
}

&redirect("server.cgi?name=$name");
