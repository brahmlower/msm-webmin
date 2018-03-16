#!/usr/bin/perl
# server_cmd.cgi
# Executes a command ingame

require 'msm-lib.pl';
&ReadParse();
my $server = $in{'name'};

&ui_print_header(undef, "Command: \"$server\"", "", "options");

print &ui_form_start("handle_server_cmd.cgi");
print &ui_table_start("", "width=100%", 2);

print &ui_table_row("Command", &ui_textbox("command", ""));
print &ui_hidden("name", "$server");

print &ui_table_end();
print &ui_form_end([ [ undef, $text{'save'} ] ]);

&ui_print_footer("server.cgi?name=$server", "server");
