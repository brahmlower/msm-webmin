#!/usr/bin/perl
# server_xp.cgi
# Give XP to a player

require 'msm-lib.pl';
&ReadParse();
my $server = $in{'name'};

my @players = msm_server_connected($server);
my $player_len = @players;

if ($players_len == 0) {
    error("There are no players to give XP to.");
}

&ui_print_header(undef, "Player XP: \"$server\"", "", "options");

print &ui_form_start("handle_server_xp.cgi");
print &ui_table_start("", "width=100%", 2);

print &ui_table_row("Player", &ui_select("player", "", \@players));
print &ui_table_row("Amount", &ui_textbox("amount", ""));
print &ui_hidden("name", "$server");

print &ui_table_end();
print &ui_form_end([ [ undef, $text{'save'} ] ]);

&ui_print_footer("server.cgi?name=$server", "server");
