$(document).ready(function () {
    $(".card").hover(function () {
        $(this).find("a").toggleClass("hide");
    });

    $(".button-delete").on("click", function (e) {
        let bookId = $(this).attr("book_id");
        $(this).attr("href", `delete_book/${bookId}`);
    });
});