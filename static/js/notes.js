const editButtons = document.getElementsByClassName("btn-edit");
const noteText = document.getElementById("id_body");
const noteForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));  /* DELETE */
const deleteButtons = document.getElementsByClassName("btn-delete");  /* DELETE */
const deleteConfirm = document.getElementById("deleteConfirm");  /* DELETE */

/**
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
    let noteId = e.target.getAttribute("note_id");
    let noteContent = document.getElementById(`note${noteId}`).innerText;
    noteText.value = noteContent;
    submitButton.innerText = "Update";
    noteForm.setAttribute("action", `edit_note/${noteId}`);
  });
}

/* DELETE */
/**
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
    deleteConfirm.href = `delete_comment/${commentId}`;
    deleteModal.show();
  });
}
/* DELETE */