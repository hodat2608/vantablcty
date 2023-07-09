function toggleCreatePostForm(event) {
    event.preventDefault();
    var formDiv = document.getElementById("create-post-form");
    formDiv.style.display = formDiv.style.display === "none" ? "block" : "none";
}

document.addEventListener("DOMContentLoaded", function() {
    var dropdown = document.querySelector(".dropdown");
    var dropdownContent = document.querySelector(".dropdown-content");

    dropdown.addEventListener("click", function() {
      dropdownContent.style.display = (dropdownContent.style.display === "block") ? "none" : "block";
    });
  });

function validateInput1() {
var input = document.getElementById("searchInput");
var button = document.getElementById("searchBtn");

if (input.value.trim() === "") {
    button.disabled = true;
} else {
    button.disabled = false;
}
}

function validateInput2() {
    var input = document.getElementById("createbox");
    var button = document.getElementById("createbox_btn");
    
    if (input.value.trim() === "") {
        button.disabled = true;
    } else {
        button.disabled = false;
    }
    }

function validateInput3() {
var input = document.getElementById("commentbox");
var button = document.getElementById("commentbox_btn");

if (input.value.trim() === "") {
    button.disabled = true;
} else {
    button.disabled = false;
}
}