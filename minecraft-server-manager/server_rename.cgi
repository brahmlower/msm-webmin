#!/usr/bin/perl
# server_rename.cgi
# Rename a minecraft server

require 'msm-lib.pl';
&ReadParse();
my $server = $in{'name'};

&ui_print_header(undef, "Rename Server: \"$server\"", "", "options");

print &ui_form_start("handle_server_name.cgi");
print &ui_table_start("Rename Server Form", "width=100%", 2);

print &ui_table_row("Server Name", &ui_textbox("name", "$server"));
print &ui_hidden("action", "rename");
print &ui_hidden("old_name", "$server");

print &ui_table_end();
print &ui_form_end([ [ undef, $text{'save'} ] ]);

&ui_print_footer("server.cgi?name=$server", "server");
