$(document).ready(function () {
    const detailModal = new bootstrap.Modal($("#detailModal"));

    $(".book").on("click", function () {
        const url = $(this).data("url");

        $("#detailModalBody").load(url, function () {
            detailModal.show();
        });
    });

});