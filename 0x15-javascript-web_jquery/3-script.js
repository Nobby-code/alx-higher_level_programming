/*
    javascript script to add a class called red to the <header> tag
    Must use JQuery API
*/

$(document).ready(() => {
  $('DIV#red_header').click(() => {
    $('header').addClass('red');
  });
});
