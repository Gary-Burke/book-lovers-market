$(document).ready(function () {
    const deleteModal = new bootstrap.Modal($("#deleteModal"));

    /**
     * Shows/Hides edit and delete icons when individual cards are hovered on
     */
    $(".card").hover(function () {
        $(this).find("a").toggleClass("hide");
    });

    /**
     * When clicked, gets book ID from delete button attribute
     * Builds dynamic href/URL for selected book
     * Triggers bootstrap delete modal confirmation before deleting book
     */
    $(".button-delete").on("click", function () {
        let bookId = $(this).attr("book_id");
        $("#deleteConfirm").attr("href", `delete_book/${bookId}`);
        deleteModal.show();
    });
});