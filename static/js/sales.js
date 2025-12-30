$(document).ready(function () {
    const detailModal = new bootstrap.Modal($("#detailModal"));

    $(".book").on("click", function () {
        detailModal.show();
    })

});