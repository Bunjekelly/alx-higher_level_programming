//script that fetches and lists the title for all movies by using this
//URL: https://swapi-api.alx-tools.com/api/films/?format=json

const Url = "https://swapi-api.alx-tools.com/api/films/?format=json";

$.get(Url, function(data){
    data.results.forEach(function(film) {
        $("UL#list_movies").append("<li>" + film.title + "</li>");
    });
});