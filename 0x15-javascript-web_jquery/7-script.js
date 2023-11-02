//script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json

const Url = "https://swapi-api.alx-tools.com/api/people/5/?format=json";
$.get(Url, function(data){
    $("DIV#character").text(data.name);
});