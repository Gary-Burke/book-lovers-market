$(document).ready(function () {
    const detailModal = new bootstrap.Modal($("#detailModal"));
    let timer;
    const delay = 500;

    /**
     * Loads Bootstrap modal with book details when clicked
     */
    $(".book").on("click", function () {
        const url = $(this).data("url");

        $("#detailModalBody").load(url, function () {
            detailModal.show();
        });
    });

    /**
     * Timer function to auto submit search input after keyboard inactivity
     */
    $("#search-input").on("input", function () {
        clearTimeout(timer);

        timer = setTimeout(() => {
            document.getElementById("form-search").requestSubmit();
        }, delay);
    });

});