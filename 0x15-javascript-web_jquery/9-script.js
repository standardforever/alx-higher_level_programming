url = "https://fourtonfish.com/hellosalut/?lang=fr";

$('document').ready(function() {
    $.get(url, function(data, textStatus) {
        $("#hello").html(data.hello);
    });
})