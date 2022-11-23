/*
    JQuery that updates header text to new header
*/

$(document).ready(() => {
  $('DIV#update_header').click(() => {
    $('header').text('New Header!!!');
  });
});
