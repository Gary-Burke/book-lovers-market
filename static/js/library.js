$(document).ready(function() {
    $(".card").hover(function() {
        $(this).find("button").toggleClass("hide");
    })
});