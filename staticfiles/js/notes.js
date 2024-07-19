const editButtons = document.getElementsByClassName("btn-edit");
const noteText = document.getElementById("id_body");
const noteForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");


for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let noteId = e.target.getAttribute("note_id");
    let noteContent = document.getElementById(`note${noteId}`).innerText;
    noteText.value = noteContent;
    submitButton.innerText = "Update";
    noteForm.setAttribute("action", `edit_note/${noteId}`);
  });
}


for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let noteId = e.target.getAttribute("note_id");
    deleteConfirm.href = `delete_note/${noteId}`;
    deleteModal.show();
  });
}
