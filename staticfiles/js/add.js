$(document).ready(function () {
    $(".add-books").children("a").on("click", function () {
        var url = $(this).attr("data-url");
        if (!$(this).hasClass("selected")) {
            $(this).attr("href", url);
        }
    });
});