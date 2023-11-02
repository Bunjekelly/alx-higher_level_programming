//script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays
//the value of hello from that fetch in the HTML tag DIV#hello

const Url = "https://hellosalut.stefanbohacek.dev/?lang=fr";

$.get(Url, function(data){
    $("DIV#hello").html("<p>" + data.hello + "</p>");
});