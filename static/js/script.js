function toggleCreatePostForm(event) {
    event.preventDefault();
    var formDiv = document.getElementById("create-post-form");
    formDiv.style.display = formDiv.style.display === "none" ? "block" : "none";
}

function toggleCreatePostForm(event) {
  event.preventDefault();
  var formDiv = document.getElementById("repply-form");
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


var dropdowns = document.getElementsByClassName("dropdown");
for (var i = 0; i < dropdowns.length; i++) {
  dropdowns[i].addEventListener("click", function(event) {
    var dropdownContent = this.querySelector(".dropdown-content");
    dropdownContent.classList.toggle("show");
    event.stopPropagation();
  });
}
document.addEventListener("click", function(event) {
  var dropdownContents = document.getElementsByClassName("dropdown-content");
  for (var i = 0; i < dropdownContents.length; i++) {
    var openDropdown = dropdownContents[i];
    if (openDropdown.classList.contains("show")) {
      var dropdown = openDropdown.parentNode;
      var dropdownBtn = dropdown.querySelector(".dropbtn");
      if (!dropdownBtn.contains(event.target)) {
        openDropdown.classList.remove("show");
      }
    }
  }
});
