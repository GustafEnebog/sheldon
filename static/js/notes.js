const editButtons = document.getElementsByClassName("btn-edit");
const noteText = document.getElementById("id_body");
const noteForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

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