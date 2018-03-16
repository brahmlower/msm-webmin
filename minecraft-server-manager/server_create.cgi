#!/usr/bin/perl
# server_create.cgi
# Create a minecraft server

require 'msm-lib.pl';

&ui_print_header(undef, "Create Server", "", "options");

print &ui_form_start("handle_server_name.cgi");
print &ui_table_start("Create Server Form", "width=100%", 2);

print &ui_table_row("Server Name", &ui_textbox("name", ""));
print &ui_hidden("action", "create");

print &ui_table_end();
print &ui_form_end([ [ undef, $text{'save'} ] ]);

&ui_print_footer("", $text{'index_return'});
