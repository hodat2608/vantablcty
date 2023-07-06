function toggleCreatePostForm(event) {
    event.preventDefault();
    var formDiv = document.getElementById("create-post-form");
    formDiv.style.display = formDiv.style.display === "none" ? "block" : "none";
}