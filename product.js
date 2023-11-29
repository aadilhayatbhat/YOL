// Get the book ID from the URL
const urlParams = new URLSearchParams(window.location.search);
const bookId = urlParams.get('bookID');  // This will get the bookID value passed in the URL

// Function to fetch book details from the database
function fetchBookDetails(bookId) {
    fetchBook(bookId)
        .then(data => {
            // Populate the HTML elements with the fetched data
            document.getElementById('book-title').innerText = data.title;
            document.getElementById('book-author').innerText = 'Author: ' + data.author;
            document.getElementById('book-description').innerText = 'Description: ' + data.description;
            document.getElementById('book-image').src = data.imageSrc;
            document.getElementById('availability').innerText = data.available ? 'Available' : 'Not Available';

            // Set up the action buttons
            const readOnlineLink = document.getElementById('read-online');
            const listenOnlineLink = document.getElementById('listen-online');
            const borrowLink = document.getElementById('borrow');

            if (data.pdfUrl) {
                readOnlineLink.href = data.pdfUrl;
                readOnlineLink.style.display = 'block';  // Show the link if a PDF URL is available
            } else {
                readOnlineLink.style.display = 'none';  // Hide the link if no PDF URL is available
            }

            if (data.audioUrl) {
                listenOnlineLink.href = data.audioUrl;
                listenOnlineLink.style.display = 'block';  // Show the link if an audio URL is available
            } else {
                listenOnlineLink.style.display = 'none';  // Hide the link if no audio URL is available
            }

            if (!data.pdfUrl && !data.audioUrl) {
                borrowLink.style.display = 'block';  // Show the Borrow link if neither a PDF nor an audio URL is available
            } else {
                borrowLink.style.display = 'none';  // Hide the Borrow link otherwise
            }

        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Fetch and display the book details
fetchBookDetails(bookId);

// Example fetchBook function
function fetchBook(bookId) {
    return fetch(`http://127.0.0.1:5000/books/${bookId}`)
        .then(response => response.json());
}
