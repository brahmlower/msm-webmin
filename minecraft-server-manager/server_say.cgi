#!/usr/bin/perl
# server_say.cgi
# Say something in a minecraft server

require 'msm-lib.pl';
&ReadParse();
my $server = $in{'name'};

&ui_print_header(undef, "Say: \"$server\"", "", "options");

print &ui_form_start("handle_server_say.cgi");
print &ui_table_start("Rename Server Form", "width=100%", 2);

print &ui_table_row("Say", &ui_textbox("message", ""));
print &ui_hidden("name", "$server");

print &ui_table_end();
print &ui_form_end([ [ undef, $text{'save'} ] ]);

&ui_print_footer("server.cgi?name=$server", "server");
