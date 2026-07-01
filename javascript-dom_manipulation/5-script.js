const bouton = document.querySelector("#update_header");
const newHeader = document.querySelector("header");

bouton.onclick = function () {
    newHeader.textContent = "New Header!!!";
}
