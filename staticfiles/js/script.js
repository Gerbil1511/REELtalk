// Community Forum posts list
document.addEventListener('DOMContentLoaded', function() {
// Pagination of forum posts
    const rowsPerPage = 10; // Number of rows to display per page
    const table = document.getElementById('forum-posts-table').getElementsByTagName('tbody')[0]; // Get the table body
    const rows = table.getElementsByTagName('tr'); // Get all rows in the table body
    const paginationControls = document.getElementById('pagination-controls').getElementsByTagName('ul')[0]; // Get the pagination controls container
    const totalPages = Math.ceil(rows.length / rowsPerPage); // Calculate the total number of pages

    // Function to display rows for the current page
    function displayRows(page) {
        const start = (page - 1) * rowsPerPage; // Calculate the start index
        const end = start + rowsPerPage; // Calculate the end index
        for (let i = 0; i < rows.length; i++) {
            rows[i].style.display = (i >= start && i < end) ? '' : 'none'; // Show rows within the range, hide others
        }
    }

    // Function to create pagination controls
    function createPaginationControls() {
        for (let i = 1; i <= totalPages; i++) {
            const li = document.createElement('li'); // Create a list item
            li.className = 'page-item'; // Add Bootstrap class for styling
            const a = document.createElement('a'); // Create a link
            a.className = 'page-link'; // Add Bootstrap class for styling
            a.href = '#'; // Set the href attribute
            a.innerText = i; // Set the link text to the page number
            a.addEventListener('click', function(e) {
                e.preventDefault(); // Prevent the default link behavior
                displayRows(i); // Display rows for the clicked page
                updateActivePage(i); // Update the active page link
            });
            li.appendChild(a); // Append the link to the list item
            paginationControls.appendChild(li); // Append the list item to the pagination controls
        }
    }

    // Function to update the active page link
    function updateActivePage(page) {
        const pageLinks = paginationControls.getElementsByTagName('a'); // Get all page links
        for (let i = 0; i < pageLinks.length; i++) {
            pageLinks[i].parentElement.classList.remove('active'); // Remove the active class from all links
        }
        pageLinks[page - 1].parentElement.classList.add('active'); // Add the active class to the clicked link
    }

    // Initialize pagination
    displayRows(1); // Display the first page of rows
    createPaginationControls(); // Create the pagination controls
    updateActivePage(1); // Set the first page link as active
});

// Community Forum post detail page - for the comments
const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/*
 * Initializes edit functionality for the provided edit buttons.
 * 
 * For each button in the `editButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Fetches the content of the corresponding comment.
 * - Populates the `commentText` input/textarea with the comment's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
 */

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
}

/*
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the 
 * deletion endpoint for the specific comment.
 * - Displays a confirmation modal (`deleteModal`) to prompt 
 * the user for confirmation before deletion.
 */
 for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        deleteConfirm.href = `/forum/comment/${commentId}/delete`;
        deleteModal.show();
    });
}

