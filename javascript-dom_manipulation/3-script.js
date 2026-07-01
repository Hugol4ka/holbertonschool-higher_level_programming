const bouton = document.querySelector("#toggle_header");
const leHeader = document.querySelector("header");

bouton.onclick = function () {
    leHeader.classList.toggle("red");
    leHeader.classList.toggle("green");
}
