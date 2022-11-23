/*
    script that
        adds an element to a list
        removes an element
        clears the list
*/

$(document).ready(() => {
  $('DIV#add_item').click(() => {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(() => {
    $('UL.my_list LI').slice(-1).remove();
  });
  $('DIV#clear_list').click(() => {
    $('UL.my_list LI').remove();
  });
});
