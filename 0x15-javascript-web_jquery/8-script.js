/*
    Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

    All movie titles must be list in the HTML tag UL#list_movies
    You can’t use document.querySelector to select the HTML tag
    You must use the JQuery API
*/

const source = 'https://swapi-api.hbtn.io/api/films/?format=json';

$(document).ready(() => {
  $.get(source, (data, textStatus) => {
    data.results.map((movie) => $('UL#list_movies').append('<li>' + movie.title + '</li>'));
  });
});
