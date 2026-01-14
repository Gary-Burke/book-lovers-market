/* jshint esversion: 11 */

// Global Variables
let timer;
const delay = 500;
const detailModal = new bootstrap.Modal(document.getElementById("detailModal"));

// Wait for the DOM to load before executing functions
document.addEventListener("DOMContentLoaded", () => {

    let books = document.querySelectorAll(".book");

    for (let book of books) {
        book.addEventListener("click", getURL);
    }

    /**
     * Timer function to auto submit search input after keyboard inactivity
     */
    document.getElementById("search-input").addEventListener("input", () => {

        clearTimeout(timer);
        timer = setTimeout(() => {
            document.getElementById("form-search").requestSubmit();
        }, delay);
    });

});

/**
 * Loads Bootstrap modal with book details when clicked via partial template
 */
async function getURL(e) {
    try {
        const url = e.currentTarget.getAttribute("data-url");
        
        const response = await fetch(url, {
            headers: {
                "X-Requested-With": "XMLHttpRequest" // Code from chatGPT to restrict access for users to the partial template by typing the url directly
            }
        });

        if (!response.ok) {
            throw new Error(`Server Status: ${response.status}`);
        }

        document.getElementById("detailModalBody").innerHTML = await response.text();
        detailModal.show();

        document.getElementById("seller").addEventListener("click", function () {
            this.nextElementSibling.classList.toggle("hide");
        });

    } catch (err) {
        console.error("Failed to load book details:", err);
    }
}