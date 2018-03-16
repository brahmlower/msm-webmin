#!/usr/bin/perl
# Show a form to create or edit a website

require 'msm-lib.pl';
ReadParse();

my $jargroup = $in{'name'};
# Redirects to home if the jargroup does not exist
if (!(grep { $_ eq $jargroup } msm_jargroup_list())) {
    error("No jargroup with name: $jargroup");
}

ui_print_header(undef, "Jargroup: \"$jargroup\"", "");

print ui_buttons_start();
print ui_buttons_row("handle_jargroup_getlatest.cgi?jargroup=$jargroup",
                     $text{'jargroup_getlatest'},
                     "Download the latest jar file for the jar group");
print ui_buttons_row('handle_jargroup_delete.cgi',
                     $text{'jargroup_delete'},
                     "Delete the jar group");
print ui_buttons_end();

# Jargroup list
my @jargroups = msm_jargroup_files($jargroup);
my @jargroups_table = ( );
foreach my $s (@jargroups) {
    push(@jargroups_table, [ html_escape($s) ]);
}

# Show the table with add links
print ui_form_columns_table(
    undef,
    undef,
    0,
    undef,
    undef,
    [ $text{'jargroup_table_name'} ],
    50,
    \@jargroups_table,
    undef,
    0,
    undef,
    $text{'jargroup_table_empty'},
    );

ui_print_footer('', $text{'index_return'});
