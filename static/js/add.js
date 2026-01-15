/* jshint esversion: 11 */

// Wait for the DOM to load before executing functions
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".add-books > a").forEach(a => {
        a.addEventListener("click", function (e) {
            var url = this.getAttribute("data-url");

            if (!this.classList.contains("selected")) {
                this.setAttribute("href", url);
            }
        });
    });

});