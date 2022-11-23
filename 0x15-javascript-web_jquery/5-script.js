/* script that adds a <li> element to a list when:
     tag DIV#add_item is clicked
    the new lement must be added to the UL.my_list
*/

$('DIV#add_item').click(() => {
  $('UL.my_list').append('<li>Item</li>');
});
