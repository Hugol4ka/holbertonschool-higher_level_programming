
document.addEventListener("DOMContentLoaded", function() {
    const fetchHello = document.querySelector("#hello");
    fetch("https://hellosalut.stefanbohacek.com/?lang=fr")
    .then(response => response.json())
    .then(data => {
        const helloText = data.hello;
        fetchHello.textContent = helloText;
    });
});
