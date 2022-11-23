/*
    script to update the color of HTML tag to red
    when a user clicks on a DIV#red_header
*/

$(document).ready(() => {
  $('DIV#red_header').click(() => {
    $('header').css('color', '#FF0000');
  });
});
