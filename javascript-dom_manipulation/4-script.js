const bouton = document.querySelector("#add_item");
const ul = document.querySelector("ul");

bouton.onclick = function () {
    const li = document.createElement("li");
    li.textContent = "Item";
    ul.appendChild(li);
}
