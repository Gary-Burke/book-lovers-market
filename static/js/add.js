/* jshint esversion: 11 */

// Wait for the DOM to load before executing functions
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".add-books > a").forEach(a => {
        a.addEventListener("click", function (e) {
            var url = this.getAttribute("data-url");

            // Loads form based on user selected button
            if (!this.classList.contains("selected")) {
                this.setAttribute("href", url);
            } else {
                e.preventDefault();
            }
        });
    });

});