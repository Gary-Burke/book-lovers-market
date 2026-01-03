$(document).ready(function () {
    const deleteModal = new bootstrap.Modal($("#deleteModal"));
    let timer;
    const delay = 500;

    /**
     * Shows/Hides edit and delete icons when individual cards are hovered on
     */
    $(".book").hover(function () {
        $(this).find("a").toggleClass("hide");
    });

    /**
     * When clicked, gets book ID from delete button attribute
     * Builds dynamic href/URL for selected book
     * Triggers bootstrap delete modal confirmation before deleting book
     */
    $(".button-delete").on("click", function () {
        let bookId = $(this).attr("data-book-id");
        $("#deleteConfirm").attr("href", `delete_book/${bookId}`);
        deleteModal.show();
    });

    /**
     * When clicked, gets book ID from edit button attribute
     * Builds dynamic href/URL for selected book
     * builds url for action attribute of post form
     */
    $(".button-edit").on("click", function () {
        let bookId = $(this).attr("data-book-id");
        $(".button-edit").attr("href", `edit_book/${bookId}`);
        $("#editBookForm").attr("action", `edit_book/${bookId}`);
    });

    /**
     * Timer function to auto submit search input after keyboard inactivity
     */
    $("#search-input").on("input", function () {
        clearTimeout(timer);

        timer = setTimeout(function () {
            $("#form-search").submit();
        }, delay);
    });

});