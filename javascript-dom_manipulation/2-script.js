const bouton = document.querySelector("#red_header");
const leHeader = document.querySelector("header");

bouton.onclick = function () {
    leHeader.classList.add("red");
};
