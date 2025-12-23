$(document).ready(function () {
    const deleteModal = new bootstrap.Modal($("#deleteModal"));
    const deleteConfirm = $("#deleteConfirm");

    $(".card").hover(function () {
        $(this).find("a").toggleClass("hide");
    });

    $(".button-delete").on("click", function (e) {
        let bookId = $(this).attr("book_id");
        deleteConfirm.attr("href", `delete_book/${bookId}`);
        deleteModal.show();
    });
});