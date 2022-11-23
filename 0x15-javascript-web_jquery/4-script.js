/*
    javascript script to toggle the class of the header:
        classes: red and green
    Must use JQuery API
*/

const header = $('header');
const toggler = $('DIV#toggle_header');

if (!header.hasClass('red') && !header.hasClass('green')) {
  header.addClass('red');
  header.removeClass('green');
}

toggler.click(() => {
  if (header.hasClass('red')) {
    header.addClass('green');
    header.removeClass('red');
  } else {
    header.addClass('red');
    header.removeClass('green');
  }
});
