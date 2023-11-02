//script that fetches and prints how to say “Hello” depending on the language

$(document).ready(function() {
    $('INPUT#btn_translate').click(function() {
        let language = $('#language_code').value();
        $.get('https://www.fourtonfish.com/hellosalut/?lang=' + language, function(data) {
            $('DIV#hello').text(data.hello);
        });
    });
});
