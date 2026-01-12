/* jshint esversion: 11 */

// Global Variables
let timer;
const delay = 500;
let detailModal;

// Wait for the DOM to load before executing functions
document.addEventListener("DOMContentLoaded", () => {

    detailModal = new bootstrap.Modal(document.getElementById("detailModal"));

    let books = document.querySelectorAll(".book");

    for (let book of books) {
        book.addEventListener("click", e => getURL(e));
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
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(`Server Status: ${response.status}`)
        }

        document.getElementById("detailModalBody").innerHTML = await response.text();
        detailModal.show();
    } catch (err) {
        console.error("Failed to load book details:", err);
    }
}