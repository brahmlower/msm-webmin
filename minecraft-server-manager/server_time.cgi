#!/usr/bin/perl
# server_time.cgi
# Modify the time of day

require 'msm-lib.pl';
&ReadParse();
my $server = $in{'name'};

&ui_print_header(undef, "Time: \"$server\"", "", "options");

print &ui_form_start("handle_server_time.cgi");
print &ui_table_start("", "width=100%", 2);

print &ui_table_row("Action", &ui_select("action", "", ["Add", "Set"]));
print &ui_table_row("Amount", &ui_textbox("amount", ""));
print &ui_hidden("name", "$server");

print &ui_table_end();
print &ui_form_end([ [ undef, $text{'save'} ] ]);

&ui_print_footer("server.cgi?name=$server", "server");
